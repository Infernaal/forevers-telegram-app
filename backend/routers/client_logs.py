from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
from typing import Literal, List, Any
import logging

logger = logging.getLogger("clientlogs")

router = APIRouter(prefix="/logs", tags=["Client Logs"])

LogLevel = Literal['log','info','debug','warn','error']

class LogEntry(BaseModel):
    level: LogLevel = Field(..., description="Console level")
    message: str = Field(..., description="Rendered text message (already joined)")
    ts: str = Field(..., description="Client time (ISO or partial)")
    context: dict | None = Field(None, description="Optional structured context")
    source: str | None = Field(None, description="Source hint (e.g. tonconnect)")

class LogBatch(BaseModel):
    entries: List[LogEntry]
    session: str | None = Field(None, description="Client session id/hash")
    user_id: str | None = Field(None, description="Telegram user id if available")
    app_version: str | None = Field(None, description="Frontend version / commit hash")

LEVEL_MAP = {
    'log': logging.INFO,
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'warn': logging.WARNING,
    'error': logging.ERROR,
}

@router.post('', summary="Ingest batch of client console logs")
async def ingest_logs(batch: LogBatch, request: Request):
    client_ip = request.client.host if request.client else 'unknown'
    count = 0
    for e in batch.entries:
        lvl = LEVEL_MAP.get(e.level, logging.INFO)
        logger.log(lvl, f"CLIENTLOG level={e.level} ts={e.ts} ip={client_ip} session={batch.session} user={batch.user_id} src={e.source} msg={e.message}")
        count += 1
    return {"status": "ok", "ingested": count}
