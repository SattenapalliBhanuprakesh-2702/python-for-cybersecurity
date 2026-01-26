from engine.log_parser import load_logs
from engine.detection import detect_bruteforce
from engine.regex_engine import extract_ips
from engine.file_scanner import scan_files, quarantine_files, backup_files
from engine.network_scanner import scan_host, risk_score
from engine.packet_analyzer import analyze_pcap
from engine.alerting import generate_alerts
from engine.reporting import generate_csv_summary, generate_word_report, generate_pdf_impact_report
import os

def main():
    os.makedirs("reports", exist_ok=True)

    logs = load_logs("logs/auth.log")
    attacks = detect_bruteforce(logs)

    infected = scan_files("system", ["malware.exe", "virus.exe"])
    quarantine_files(infected)
    backup_files(["important/file.txt"])

    ports = scan_host("127.0.0.1")
    threat = risk_score(ports)

    suspicious_packets = analyze_pcap("pcaps/traffic.pcap")

    generate_alerts(attacks, threat, suspicious_packets)

    generate_csv_summary(logs, attacks)
    generate_word_report(logs, attacks)
    generate_pdf_impact_report(logs, attacks, threat)

    print("SOC Automation Run Completed")

if __name__ == "__main__":
    main()
