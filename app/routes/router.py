from fastapi import APIRouter, HTTPException
from schema.schema import EmailRequest
from utils.email_sender import send_email

router = APIRouter()

@router.post("/send-email/")
async def send_email_endpoint(request: EmailRequest):
    """
    Endpoint to send an email with the provided details.
    """
    try:
        # Email configuration
        sender_email = "hendrisyuwavi01@gmail.com"
        sender_password = "katasandi123"
        recipient_email = "hendrisyuwavi12@gmail.com"

        # Prepare email content
        subject = f"New Registration from {request.name}"
        body = (
            f"Name: {request.name}\n"
            f"Phone: {request.phone}\n"
            f"Email: {request.email}\n"
            f"Message: {request.message}\n"
        )

        # Call utility function to send email
        send_email(sender_email, sender_password, recipient_email, subject, body)

        return {"message": "Email sent successfully!"}
    except Exception as e:
        # Raise an HTTPException for errors
        raise HTTPException(status_code=500, detail=str(e))
