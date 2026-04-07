from twilio.rest import Client
import os

# ✅ Simple working location (change if needed)
def get_location():
    return "https://maps.google.com/?q=13.0827,80.2707"  # Chennai example

# 🔐 Secure credentials (set in terminal)
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")

# ❌ Safety check
if not account_sid or not auth_token:
    print("❌ Twilio credentials not set")
    exit()

client = Client(account_sid, auth_token)

# 🔥 TEST TRIGGER (replace later with sensor)
accident = True

if accident:
    location_link = get_location()

    message = client.messages.create(
        body=f"""🚨 ACCIDENT ALERT 🚨

Victim needs immediate help!

📍 Location:
{location_link}

⚠ Please respond quickly""",
        from_="+12604002962",   # your Twilio number
        to="+919677699624"      # your verified number
    )

    print("✅ SMS sent:", message.sid)