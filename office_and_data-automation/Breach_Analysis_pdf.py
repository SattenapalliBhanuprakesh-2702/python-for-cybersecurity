# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# import pandas as pd 


# df=pd.read_csv("auth_logs.csv")
# failed=df[df["status"]=="failed"]

# c=canvas.Canvas("Bread Analysis pdf",pagesize=A4)
# c.drawString(50,800,"Breach Impact Analysis")

# y=760
# for ip,count in failed.groupby("ip").size().items():
#     c.drawString(50,y,f"{ip} -> {count} failed logins")
#     y-=20

# c.save()


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd

# Load CSV
df = pd.read_csv("auth_logs.csv")
failed = df[df["status"] == "failed"]

# Create PDF
c = canvas.Canvas("simple_breach_report.pdf", pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, "Breach Impact Analysis Report")

# Summary
c.setFont("Helvetica", 12)
c.drawString(50, height - 80, f"Total login attempts: {len(df)}")
c.drawString(50, height - 100, f"Failed login attempts: {len(failed)}")

# List attacker IPs
y = height - 140
c.drawString(50, y, "IP Address → Failed Attempts")
y -= 20

for ip, count in failed.groupby("ip").size().items():
    c.drawString(50, y, f"{ip} → {count}")
    y -= 20
    if y < 50:  # start new page if needed
        c.showPage()
        y = height - 50

# Save PDF
c.save()
print("PDF report generated: simple_breach_report.pdf")
