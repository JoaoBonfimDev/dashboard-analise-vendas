import pandas as pd


df = pd.read_csv("dados/vendas.csv")


df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")


df["Categoria"] = df["Categoria"].str.strip()

df["Categoria"] = df["Categoria"].str.title()


df.loc[df["Produto"] == "Webcam HD", "Categoria"] = "Acessórios"


print(df[df["Categoria"].isna()])

print(df[df["Produto"] == "Teclado Mecânico"])