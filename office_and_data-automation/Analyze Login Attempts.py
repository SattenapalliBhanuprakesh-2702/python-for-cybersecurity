import pandas as pd

df=pd.read_csv("auth_logs.docx")
failed=df[df["status"]=="failed"]
# print(failed)
attackers=failed.groupby("ip").size().sort_values(ascending=False)
attackers=attackers[attackers>2]
print(attackers)