import smtplib
from email.message import EmailMessage
from datetime import datetime

# Sample customer data
customers = [
    {"name": "Alice Johnson", "email": "alice@example.com", "birthday": "06-19"},
    {"name": "michel tuckson", "email": "michel@proton.me", "birthday": "07-19"},
    {"name": "Alice Johnson", "email": "alicejohnson@gmail.com", "birthday": "06-19"}
]

# Email server config
# SMTP : Simple Mail Transfer Protocol
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "erfanbaghchedan@gmail.com"
EMAIL_PASSWORD = "vryo zdhe ykcj uwku" # Use app password for Gmail

# Today's date
today = datetime.now().strftime("%m-%d")

# Loop through customers
for customer in customers:
    if customer["birthday"] == today:
        # Create the email
        msg = EmailMessage()
        msg["Subject"] = "Happy Birthday, {}!".format(customer["name"].split()[0])
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = customer["email"]

        # Email content
        msg.set_content(f"""
Hi {customer['name'].split()[0]} 🎉,

Wishing you a fantastic birthday filled with joy, success, and happiness! 🥳

Thank you for being a valued customer.

Best regards,  
Your Company Team
""")

        # Send the email
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
                # TLS (Transport Layer Security)
                smtp.starttls()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print(f"Sent birthday email to {customer['name']}")
        except Exception as e:
            print(f"Failed to send email to {customer['name']}: {e}")
