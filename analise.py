import pandas as pd


# =========================
# CARREGAMENTO DOS DADOS
# =========================

df = pd.read_csv("dados/vendas.csv")


# =========================
# TRATAMENTO DOS DADOS
# =========================

df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

df["Categoria"] = df["Categoria"].str.strip()
df["Categoria"] = df["Categoria"].str.title()

df.loc[df["Produto"] == "Webcam HD", "Categoria"] = "Acessórios"
df.loc[df["Produto"] == "Teclado Mecânico", "Categoria"] = "Acessórios"
df.loc[df["Produto"] == "Headset Gamer", "Categoria"] = "Acessórios"

df.loc[
    (df["Produto"] == "Webcam HD") &
    (df["Preco_Unitario"].isna()),
    "Preco_Unitario"
] = 219.90

df.loc[
    (df["Produto"] == "Cadeira Office") &
    (df["Preco_Unitario"].isna()),
    "Preco_Unitario"
] = 899.90

df["Vendedor"] = df["Vendedor"].str.strip()

df = df.drop_duplicates()


# =========================
# NOVAS COLUNAS
# =========================

df["Total_Vendas"] = df["Preco_Unitario"] * df["Quantidade"]

df["Mes"] = df["Data"].dt.to_period("M")


# =========================
# KPIs GERAIS
# =========================

faturamento_total = df["Total_Vendas"].sum()

quantidade_total = df["Quantidade"].sum()

valor_medio_por_registro = round(
    faturamento_total / len(df),
    2
)


# =========================
# ANÁLISE POR PRODUTO
# =========================

vendas_por_produto = (
    df.groupby("Produto")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
)

produto_mais_vendido = vendas_por_produto.idxmax()
quantidade_produto_mais_vendido = vendas_por_produto.max()


faturamento_por_produto = (
    df.groupby("Produto")["Total_Vendas"]
    .sum()
    .sort_values(ascending=False)
)

produto_maior_faturamento = faturamento_por_produto.idxmax()
maior_faturamento_produto = faturamento_por_produto.max()


participacao_produto = (
    faturamento_por_produto
    / faturamento_total
    * 100
).round(2)


# =========================
# ANÁLISE POR CATEGORIA
# =========================

vendas_por_categoria = (
    df.groupby("Categoria")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
)

faturamento_por_categoria = (
    df.groupby("Categoria")["Total_Vendas"]
    .sum()
    .sort_values(ascending=False)
)

participacao_categoria = (
    faturamento_por_categoria
    / faturamento_total
    * 100
).round(2)


# =========================
# ANÁLISE POR VENDEDOR
# =========================

faturamento_por_vendedor = (
    df.groupby("Vendedor")["Total_Vendas"]
    .sum()
    .sort_values(ascending=False)
)

quantidade_por_vendedor = (
    df.groupby("Vendedor")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
)

valor_medio_por_vendedor = (
    faturamento_por_vendedor
    / quantidade_por_vendedor
).round(2).sort_values(ascending=False)


# =========================
# ANÁLISE TEMPORAL
# =========================

faturamento_por_mes = (
    df.groupby("Mes")["Total_Vendas"]
    .sum()
    .sort_index()
)

melhor_mes = faturamento_por_mes.idxmax()
maior_faturamento_mensal = faturamento_por_mes.max()

pior_mes = faturamento_por_mes.idxmin()
menor_faturamento_mensal = faturamento_por_mes.min()


quantidade_por_mes = (
    df.groupby("Mes")["Quantidade"]
    .sum()
    .sort_index()
)

valor_medio_por_mes = (
    faturamento_por_mes
    / quantidade_por_mes
).round(2)

variacao_mensal = (
    faturamento_por_mes
    .pct_change()
    .mul(100)
    .round(2)
)