import pandas as pd 

df=pd.read_csv("auth_logs.csv")

print(df["status"].value_counts())