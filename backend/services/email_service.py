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
        self.smtp_host = os.getenv("SMTP_HOST", "sandbox.smtp.mailtrap.io")
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
            message["Subject"] = "Verification Code"
            message["From"] = f"{self.from_name} <{self.from_email}>"
            message["To"] = email

            # Create HTML content
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Verification Code</title>
            </head>
            <body style="margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <!-- Header -->
                    <div style="background: linear-gradient(135deg, #007BFF 0%, #0056b3 100%); padding: 40px 20px; text-align: center;">
                        <svg viewBox="0 0 142 98" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M5.66363 95.2209C3.90374 94.293 2.49584 92.981 1.5039 91.3172C0.479967 89.6533 0 87.7334 0 85.6215C0 83.5097 0.511965 81.6218 1.5039 79.9259C2.52783 78.262 3.90374 76.9501 5.66363 76.0222C7.42351 75.0942 9.40738 74.6143 11.6472 74.6143C13.5991 74.6143 15.327 74.9662 16.8949 75.6382C18.4628 76.3101 19.7427 77.3021 20.7666 78.614L16.9269 82.0698C15.551 80.4059 13.8871 79.5739 11.9352 79.5739C10.7833 79.5739 9.75936 79.8299 8.86342 80.3419C7.96748 80.8538 7.26352 81.5578 6.78355 82.4857C6.30359 83.4137 6.0476 84.4696 6.0476 85.6535C6.0476 86.8375 6.30359 87.8934 6.78355 88.8213C7.26352 89.7493 7.96748 90.4532 8.86342 90.9652C9.75936 91.4771 10.7833 91.7331 11.9352 91.7331C13.8871 91.7331 15.551 90.9012 16.9269 89.2373L20.7346 92.6931C19.7107 93.973 18.3988 94.9649 16.8629 95.6689C15.295 96.3408 13.5671 96.6928 11.6152 96.6928C9.43938 96.6288 7.42351 96.1808 5.66363 95.2209Z" fill="white"/>
                            <path d="M37.5335 92.0851H28.5741L26.9102 96.2129H20.7986L30.142 75.0303H36.0296L45.405 96.2129H39.1654L37.5335 92.0851ZM35.7736 87.6694L33.0538 80.8859L30.334 87.6694H35.7736Z" fill="white"/>
                            <path d="M62.1079 75.9897C63.5158 76.6296 64.6038 77.5256 65.3717 78.7095C66.1397 79.8934 66.5236 81.2693 66.5236 82.8692C66.5236 84.4691 66.1397 85.845 65.3717 87.029C64.6038 88.2129 63.5158 89.1088 62.1079 89.7488C60.7 90.3887 59.0361 90.7087 57.1162 90.7087H53.4365V96.2444H47.4529V75.0618H57.1482C59.0361 75.0298 60.7 75.3497 62.1079 75.9897ZM59.5481 85.1411C60.188 84.5971 60.476 83.8292 60.476 82.8692C60.476 81.8773 60.1561 81.1094 59.5481 80.5654C58.9401 80.0214 57.9802 79.7334 56.7643 79.7334H53.4365V85.941H56.7643C57.9802 85.973 58.9081 85.6851 59.5481 85.1411Z" fill="white"/>
                            <path d="M69.4995 75.0303H75.4831V96.2129H69.4995V75.0303Z" fill="white"/>
                            <path d="M85.5624 79.7982H79.0668V75.0625H98.0416V79.7982H91.578V96.2131H85.5944V79.7982H85.5624Z" fill="white"/>
                            <path d="M112.952 92.0851H103.993L102.329 96.2129H96.2176L105.561 75.0303H111.449L120.824 96.2129H114.584L112.952 92.0851ZM111.193 87.6694L108.473 80.8859L105.753 87.6694H111.193Z" fill="white"/>
                            <path d="M122.84 75.0303H128.824V91.4452H138.935V96.1809H122.84V75.0303Z" fill="white"/>
                            <path d="M139.447 60.4385H0.640015V65.7821H139.447V60.4385Z" fill="white"/>
                            <path d="M138.167 13.2099C135.799 9.4341 132.503 6.4903 128.216 4.41044C123.928 2.36257 119.032 1.30664 113.529 1.30664H89.6901V6.20231C91.546 8.50616 92.4739 11.29 92.4739 14.4898C92.4739 17.2416 91.802 19.7054 90.4261 21.9133C90.2021 22.2973 89.9461 22.6492 89.6901 22.9692V26.585C90.586 27.3209 91.386 28.1209 92.0899 29.0488C93.9778 31.5127 94.9058 34.4885 94.9058 37.9122C94.9058 42.5519 93.1459 46.2957 89.6901 48.9835V51.7353H113.529C119.064 51.7353 123.96 50.7114 128.216 48.6315C132.503 46.5837 135.799 43.6399 138.167 39.8321C140.503 36.0244 141.687 31.6086 141.687 26.521C141.687 21.4333 140.503 17.0176 138.167 13.2099ZM123.352 36.6963C120.728 39.1601 117.272 40.3761 112.953 40.3761H103.961V12.7299H112.953C117.272 12.7299 120.728 13.9458 123.352 16.4096C125.976 18.8735 127.288 22.2333 127.288 26.553C127.288 30.8727 125.976 34.2325 123.352 36.6963ZM48.4768 39.8641C50.8127 36.0564 51.9966 31.6406 51.9966 26.553C51.9966 21.4653 50.8127 17.0176 48.4768 13.2419C46.109 9.4661 42.8132 6.52229 38.5255 4.44243C34.2377 2.39457 29.3421 1.33864 23.8384 1.33864H0V51.7353H23.8384C29.3741 51.7353 34.2697 50.7114 38.5255 48.6315C42.8132 46.5837 46.141 43.6399 48.4768 39.8641ZM33.6938 36.6963C31.07 39.1601 27.6142 40.3761 23.2945 40.3761H14.3031V12.7299H23.2945C27.6142 12.7299 31.07 13.9458 33.6938 16.4096C36.3176 18.8735 37.6295 22.2333 37.6295 26.553C37.6295 30.8727 36.3176 34.2325 33.6938 36.6963ZM90.65 30.1687C89.0181 28.0249 86.7463 26.457 83.8665 25.4651C86.0423 24.3451 87.7062 22.8732 88.8581 20.9533C90.0421 19.0655 90.618 16.9216 90.618 14.5218C90.618 10.49 88.9221 7.29024 85.5624 4.9224C82.2026 2.55455 77.3069 1.37064 70.8753 1.37064H45.085V6.58629C47.0049 8.25018 48.6688 10.1381 50.0127 12.3139C52.5405 16.3776 53.8205 21.1773 53.8205 26.617C53.8205 32.0566 52.5405 36.8243 50.0127 40.92C48.6688 43.0959 47.0049 44.9838 45.085 46.6477V51.8633H72.3152C79.0348 51.8633 84.1865 50.6794 87.7382 48.2475C91.29 45.8477 93.0819 42.4239 93.0819 38.0082C93.0819 34.8724 92.2819 32.3126 90.65 30.1687ZM59.2281 11.61H69.0195C73.8191 11.61 76.219 13.2099 76.219 16.4416C76.219 19.7054 73.8191 21.3373 69.0195 21.3373H59.2281V11.61ZM71.1953 41.432H59.2281V31.1927H71.1953C76.187 31.1927 78.6828 32.8886 78.6828 36.3123C78.6828 39.7361 76.187 41.432 71.1953 41.432Z" fill="white"/>
                        </svg>
                    </div>
                    <!-- Content -->
                    <div style="padding: 20px;">
                        <h2 style="color: #333333; margin: 0 0 20px 0; font-size: 24px; font-weight: 600;">Your Verification Code</h2>
                        <p style="color: #666666; font-size: 16px; line-height: 1.6; margin: 0 0 30px 0;">
                            We received a request to verify your email address. Please use the verification code below to complete your authorization:
                        </p>
                        <div style="background-color: #f8f9fa; border: 2px solid #007BFF; border-radius: 10px; padding: 30px; text-align: center; margin: 30px 0;">
                            <span style="font-size: 36px; font-weight: bold; color: #007BFF; letter-spacing: 2px;">{code}</span>
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
