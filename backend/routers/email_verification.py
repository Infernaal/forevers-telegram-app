from fastapi import APIRouter, HTTPException
from schemas.email_verification import (
    SendVerificationCodeRequest, 
    VerifyCodeRequest, 
    SendCodeResponseWrapper, 
    VerifyCodeResponseWrapper
)
from services.email_service import email_service
import asyncio

router = APIRouter(prefix="/email", tags=["Email Verification"])

@router.post("/send-verification-code", response_model=SendCodeResponseWrapper, summary="Send verification code to email")
async def send_verification_code(request: SendVerificationCodeRequest):
    """
    Send a 5-digit verification code to the provided email address.
    The code expires in 10 minutes and can be used only once.
    """
    try:
        # Clean up expired codes
        email_service.cleanup_expired_codes()
        
        # Generate verification code
        code = email_service.generate_verification_code()
        
        # Store the code
        email_service.store_verification_code(request.email, code)
        
        # Send email
        success, message = await email_service.send_verification_email(request.email, code)
        
        if success:
            return SendCodeResponseWrapper(
                status="success",
                message="Verification code sent successfully",
                expires_in_minutes=email_service.code_expiry_minutes
            )
        else:
            # Remove the stored code if email sending failed
            if request.email in email_service.verification_codes:
                del email_service.verification_codes[request.email]
            
            raise HTTPException(
                status_code=500,
                detail=f"Failed to send verification code: {message}"
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@router.post("/verify-code", response_model=VerifyCodeResponseWrapper, summary="Verify email verification code")
async def verify_verification_code(request: VerifyCodeRequest):
    """
    Verify the 5-digit verification code for the provided email address.
    Returns success if the code is valid and not expired.
    """
    try:
        # Clean up expired codes
        email_service.cleanup_expired_codes()
        
        # Verify the code
        is_valid, message = email_service.verify_code(request.email, request.code)
        
        if is_valid:
            return VerifyCodeResponseWrapper(
                status="success",
                message=message,
                valid=True
            )
        else:
            return VerifyCodeResponseWrapper(
                status="error",
                message=message,
                valid=False
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@router.post("/resend-verification-code", response_model=SendCodeResponseWrapper, summary="Resend verification code to email")
async def resend_verification_code(request: SendVerificationCodeRequest):
    """
    Resend a new 5-digit verification code to the provided email address.
    This will invalidate any previously sent codes for this email.
    """
    try:
        # Clean up expired codes
        email_service.cleanup_expired_codes()
        
        # Remove any existing code for this email
        if request.email in email_service.verification_codes:
            del email_service.verification_codes[request.email]
        
        # Generate new verification code
        code = email_service.generate_verification_code()
        
        # Store the new code
        email_service.store_verification_code(request.email, code)
        
        # Send email
        success, message = await email_service.send_verification_email(request.email, code)
        
        if success:
            return SendCodeResponseWrapper(
                status="success",
                message="New verification code sent successfully",
                expires_in_minutes=email_service.code_expiry_minutes
            )
        else:
            # Remove the stored code if email sending failed
            if request.email in email_service.verification_codes:
                del email_service.verification_codes[request.email]
            
            raise HTTPException(
                status_code=500,
                detail=f"Failed to resend verification code: {message}"
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
