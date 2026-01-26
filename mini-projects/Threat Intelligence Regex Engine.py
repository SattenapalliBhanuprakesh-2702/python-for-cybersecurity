import re

def scan_file(filename):
    threats = {
        "IPs": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "URLs": r"https?://[a-zA-Z0-9./_-]+",
        "SQLi": r"'.*?='| OR |;",
        "XSS": r"<script>",
        "Passwords": r"(pass|password)=\w+"
    }

    results = {}

    with open(filename) as f:
        data = f.read()

        for name, pattern in threats.items():
            matches = re.findall(pattern, data, re.IGNORECASE)
            if matches:
                results[name] = matches

    return results


def generate_report(results):
    with open("threat_report.txt", "w") as f:
        for k, v in results.items():
            f.write(k + "\n")
            for item in v:
                f.write("  " + str(item) + "\n")
            f.write("\n")


def main():
    data = scan_file("input.txt")
    generate_report(data)
    print("Threat report generated.")

main()
