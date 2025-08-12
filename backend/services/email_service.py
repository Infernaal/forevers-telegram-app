import aiosmtplib
import random
import asyncio
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class EmailService:
    def __init__(self):
        self.smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_username = os.getenv("SMTP_USERNAME")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.from_email = os.getenv("FROM_EMAIL")
        self.from_name = os.getenv("FROM_NAME", "DBDC Verification")
        
        # In-memory storage for verification codes (for single use)
        # Format: {email: {"code": "12345", "expires": datetime, "attempts": 0}}
        self.verification_codes: Dict[str, Dict] = {}
        self.max_attempts = 3
        self.code_expiry_minutes = 10

    def generate_verification_code(self) -> str:
        """Generate a 5-digit verification code"""
        return f"{random.randint(10000, 99999)}"

    def store_verification_code(self, email: str, code: str) -> None:
        """Store verification code with expiry time"""
        self.verification_codes[email] = {
            "code": code,
            "expires": datetime.now() + timedelta(minutes=self.code_expiry_minutes),
            "attempts": 0
        }

    def verify_code(self, email: str, code: str) -> tuple[bool, str]:
        """Verify the provided code against stored code"""
        if email not in self.verification_codes:
            return False, "No verification code found for this email"
        
        stored_data = self.verification_codes[email]
        
        # Check if code has expired
        if datetime.now() > stored_data["expires"]:
            del self.verification_codes[email]
            return False, "Verification code has expired"
        
        # Check attempts limit
        if stored_data["attempts"] >= self.max_attempts:
            del self.verification_codes[email]
            return False, "Too many verification attempts. Please request a new code"
        
        # Increment attempts
        stored_data["attempts"] += 1
        
        # Check if code matches
        if stored_data["code"] == code:
            # Code is correct, remove it from storage
            del self.verification_codes[email]
            return True, "Verification successful"
        else:
            return False, "Invalid verification code"

    def cleanup_expired_codes(self) -> None:
        """Remove expired verification codes"""
        current_time = datetime.now()
        expired_emails = [
            email for email, data in self.verification_codes.items()
            if current_time > data["expires"]
        ]
        for email in expired_emails:
            del self.verification_codes[email]

    async def send_verification_email(self, email: str, code: str) -> tuple[bool, str]:
        """Send verification code via email"""
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = "Your DBDC Verification Code"
            message["From"] = f"{self.from_name} <{self.from_email}>"
            message["To"] = email

            # Create HTML content
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>DBDC Verification Code</title>
            </head>
            <body style="margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <!-- Header -->
                    <div style="background: linear-gradient(135deg, #FF6800 0%, #FF8A3D 100%); padding: 40px 20px; text-align: center;">
                        <h1 style="color: #ffffff; margin: 0; font-size: 28px; font-weight: bold;">DBDC</h1>
                        <p style="color: #ffffff; margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">Email Verification</p>
                    </div>
                    
                    <!-- Content -->
                    <div style="padding: 40px 30px;">
                        <h2 style="color: #333333; margin: 0 0 20px 0; font-size: 24px; font-weight: 600;">Your Verification Code</h2>
                        
                        <p style="color: #666666; font-size: 16px; line-height: 1.6; margin: 0 0 30px 0;">
                            We received a request to verify your email address. Please use the verification code below to complete your authorization:
                        </p>
                        
                        <!-- Verification Code -->
                        <div style="background-color: #f8f9fa; border: 2px solid #FF6800; border-radius: 10px; padding: 30px; text-align: center; margin: 30px 0;">
                            <div style="font-size: 36px; font-weight: bold; color: #FF6800; letter-spacing: 8px; font-family: 'Courier New', monospace;">
                                {code}
                            </div>
                        </div>
                        
                        <p style="color: #666666; font-size: 14px; line-height: 1.6; margin: 30px 0 0 0;">
                            <strong>Important:</strong><br>
                            • This code will expire in {self.code_expiry_minutes} minutes<br>
                            • For security reasons, please do not share this code with anyone<br>
                            • If you didn't request this verification, please ignore this email
                        </p>
                    </div>
                    
                    <!-- Footer -->
                    <div style="background-color: #f8f9fa; padding: 20px 30px; border-top: 1px solid #e9ecef;">
                        <p style="color: #999999; font-size: 12px; margin: 0; text-align: center;">
                            © 2025 DBDC. All rights reserved.<br>
                            This is an automated message, please do not reply to this email.
                        </p>
                    </div>
                </div>
            </body>
            </html>
            """

            # Create plain text version
            text_content = f"""
            DBDC Email Verification
            
            Your verification code: {code}
            
            This code will expire in {self.code_expiry_minutes} minutes.
            
            For security reasons, please do not share this code with anyone.
            If you didn't request this verification, please ignore this email.
            
            © 2025 DBDC. All rights reserved.
            """

            # Attach parts
            text_part = MIMEText(text_content, "plain")
            html_part = MIMEText(html_content, "html")
            
            message.attach(text_part)
            message.attach(html_part)

            # Send email
            await aiosmtplib.send(
                message,
                hostname=self.smtp_host,
                port=self.smtp_port,
                username=self.smtp_username,
                password=self.smtp_password,
                use_tls=True,
            )
            
            return True, "Email sent successfully"
            
        except Exception as e:
            return False, f"Failed to send email: {str(e)}"

# Global instance
email_service = EmailService()
