import re

IP_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
URL_PATTERN = r"https?://[^\s]+"

SQLI_PATTERN = r"(\bUNION\b|\bSELECT\b.*\bFROM\b|\bOR\b\s+1=1|--|;--|\bDROP\b\s+\bTABLE\b)"
XSS_PATTERN = r"(<script.*?>.*?</script>|onerror=|onload=|javascript:)"
LFI_PATTERN = r"(\.\./\.\./|\.\.\\\.\.\\|/etc/passwd)"
CMD_INJECTION_PATTERN = r"(\|\||&&|;|\bwhoami\b|\bcat\s+/etc/passwd\b)"
BRUTE_PATTERN = r"(failed login|authentication failure|invalid password)"
CRED_PATTERN = r"(username|user|login|password|pass)\s*[:=]\s*\S+"


def extract_ips(text):
    return re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)

def find_sqli(text):
    return re.findall(SQLI_PATTERN, text, re.IGNORECASE)

def find_xss(text):
    return re.findall(XSS_PATTERN, text, re.IGNORECASE)

def find_lfi(text):
    return re.findall(LFI_PATTERN, text, re.IGNORECASE)

def find_cmd_injection(text):
    return re.findall(CMD_INJECTION_PATTERN, text, re.IGNORECASE)

def find_bruteforce(text):
    return re.findall(BRUTE_PATTERN, text, re.IGNORECASE)

def find_credentials(text):
    return re.findall(CRED_PATTERN, text, re.IGNORECASE)

def analyze_text(text):
    report = {
        "sql_injection": find_sqli(text),
        "xss_attempts": find_xss(text),
        "lfi_attempts": find_lfi(text),
        "command_injection": find_cmd_injection(text),
        "bruteforce_indicators": find_bruteforce(text),
        "credential_leaks": find_credentials(text)
    }

    score = sum(len(v) for v in report.values())

    if score > 10:
        report["risk"] = "CRITICAL"
    elif score > 5:
        report["risk"] = "HIGH"
    elif score > 1:
        report["risk"] = "MEDIUM"
    else:
        report["risk"] = "LOW"

    return report
