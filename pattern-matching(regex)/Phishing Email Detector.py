import re

email = "Click http://paypa1.com to verify your account"

phishing_patterns = [
    r"paypa1",
    r"verify your account",
    r"click here",
    r"http://"
]

for p in phishing_patterns:
    if re.search(p, email, re.IGNORECASE):
        print("PHISHING DETECTED")
