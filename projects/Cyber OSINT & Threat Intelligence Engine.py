import requests
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException, Timeout

TARGET = "https://example.com"
OUTPUT_FILE = "osint_report.txt"
TIMEOUT = 10


def collect_data(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        html = response.text
    except Timeout:
        raise RuntimeError("request timeout")
    except RequestException as e:
        raise RuntimeError(f"http error: {e}")

    try:
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html)
        ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", html)
    except re.error as e:
        raise RuntimeError(f"regex error: {e}")

    try:
        soup = BeautifulSoup(html, "html.parser")
        links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
    except Exception as e:
        raise RuntimeError(f"parse error: {e}")

    return list(set(emails)), list(set(ips)), list(set(links))


def save_report(emails, ips, links, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("EMAILS\n")
            for e in emails:
                f.write(e + "\n")

            f.write("\nIPS\n")
            for i in ips:
                f.write(i + "\n")

            f.write("\nLINKS\n")
            for l in links:
                f.write(l + "\n")
    except IOError as e:
        raise RuntimeError(f"write error: {e}")


def main():
    try:
        emails, ips, links = collect_data(TARGET)
        save_report(emails, ips, links, OUTPUT_FILE)
        print("report generated")
    except RuntimeError as e:
        print("error:", e)


if __name__ == "__main__":
    main()
