import re

payloads = [
    "admin' OR '1'='1",
    "<script>alert(1)</script>",
    "cat /etc/passwd"
]

attack_patterns = [
    r"'.*?='",
    r"<script>",
    r"/etc/passwd",
    r"\bOR\b",
    r";"
]

for p in payloads:
    for pattern in attack_patterns:
        if re.search(pattern, p, re.IGNORECASE):
            print("ATTACK DETECTED:", p)
