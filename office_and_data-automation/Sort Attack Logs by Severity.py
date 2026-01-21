import pandas as pd 

df=pd.read_csv("auth_logs.csv")
df["severity"]=df["status"].apply(
    lambda x: "HIGH" if x=="failed" else "LOW"
)
sort_logs=df.sort_values(by="severity")
sort_logs.to_csv("sorted_logs.csv", index=False)