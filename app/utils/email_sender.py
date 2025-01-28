import smtplib

def send_email(sender_email: str, sender_password: str, recipient_email: str, subject: str, body: str):
    """
    Utility function to send an email using SMTP.
    """
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(
                sender_email,
                recipient_email,
                f"Subject: {subject}\n\n{body}"
            )
    except smtplib.SMTPException as e:
        raise RuntimeError(f"SMTP error occurred: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while sending the email: {e}")
