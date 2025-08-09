from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import httpx
import os

router = APIRouter(prefix="/ton", tags=["TON Payments"])

TON_API_BASE = os.getenv("TON_API_BASE", "https://tonapi.io")

class TonVerifyRequest(BaseModel):
    tx_hash: str = Field(..., description="Transaction hash (hex)")
    destination: str = Field(..., description="Expected destination user-friendly address")
    amount: int = Field(..., description="Expected amount in nanoTON")
    comment_prefix: str | None = Field(None, description="Expected comment prefix")

class TonVerifyResponse(BaseModel):
    status: str
    confirmed: bool
    message: str
    blockchain_amount: int | None = None
    comment: str | None = None

@router.post('/verify', response_model=TonVerifyResponse, summary="Verify TON transaction on-chain")
async def verify_ton_transaction(payload: TonVerifyRequest):
    tx_hash = payload.tx_hash.replace('\n','').strip()
    if not all(c in '0123456789abcdefABCDEF' for c in tx_hash):
        return TonVerifyResponse(status="failed", confirmed=False, message="tx_hash must be hex")

    url = f"{TON_API_BASE}/v2/blockchain/transactions/{tx_hash}"
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(url)
            if r.status_code == 404:
                return TonVerifyResponse(status="ok", confirmed=False, message="Transaction not found")
            r.raise_for_status()
            data = r.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Upstream TON API error: {e}")

    out_msgs = data.get('out_msgs') or []
    matched_amount = None
    matched_comment = None
    for m in out_msgs:
        addr = m.get('destination') or ''
        amt = int(m.get('value', 0))
        if addr == payload.destination and amt == payload.amount:
            matched_amount = amt
            msg_data = m.get('msg_data') or {}
            if msg_data.get('@type') == 'msg.dataText':
                matched_comment = msg_data.get('text') or ''
            break

    if matched_amount is None:
        return TonVerifyResponse(status="ok", confirmed=False, message="No matching transfer to destination with expected amount")

    if payload.comment_prefix and (not matched_comment or not matched_comment.startswith(payload.comment_prefix)):
        return TonVerifyResponse(status="ok", confirmed=False, message="Comment prefix mismatch", blockchain_amount=matched_amount, comment=matched_comment)

    return TonVerifyResponse(status="success", confirmed=True, message="Transaction verified", blockchain_amount=matched_amount, comment=matched_comment)
