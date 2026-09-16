import pandas as pd


df = pd.read_csv("dados/vendas.csv")


df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")


df["Categoria"] = df["Categoria"].str.strip()

df["Categoria"] = df["Categoria"].str.title()


df.loc[df["Produto"] == "Webcam HD", "Categoria"] = "Acessórios"

df.loc[df["Produto"] == "Teclado Mecânico", "Categoria"] = "Acessórios"

df.loc[df["Produto"] == "Headset Gamer", "Categoria"] = "Acessórios"


df.loc[(df["Produto"] == "Webcam HD") & (df["Preco_Unitario"].isna()), "Preco_Unitario"] = 219.90

df.loc[(df["Produto"] == "Cadeira Office") & (df["Preco_Unitario"].isna()), "Preco_Unitario"] = 899.90