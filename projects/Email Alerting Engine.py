import smtplib
from email.message import EmailMessage
from datetime import datetime

SMTP = "smtp.gmail.com"
PORT = 587
FROM = "soc@example.com"
TO = "analyst@example.com"

def send_email(subject, body):
    try:
        msg = EmailMessage()
        msg["From"] = FROM
        msg["To"] = TO
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP(SMTP, PORT) as s:
            s.starttls()
            s.login(FROM, "APP_PASSWORD")
            s.send_message(msg)

    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication failed")

    except smtplib.SMTPException:
        print("SMTP communication error")

    except Exception:
        print("Unexpected error while sending email")

def alert_attack(ip, count):
    try:
        body = f"""
Time: {datetime.now()}
Attack: Brute Force
IP: {ip}
Attempts: {count}
"""
        send_email("SOC Alert: Brute Force Detected", body)

    except Exception:
        print("Failed to generate alert")

attack_data = {
    "192.168.1.10": 6,
    "10.0.0.5": 2
}

try:
    for ip, count in attack_data.items():
        if count >= 5:
            alert_attack(ip, count)

    print("SOC alerts processed")

except Exception:
    print("Attack processing failed")
