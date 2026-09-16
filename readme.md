# Dashboard de Análise de Vendas

Projeto desenvolvido com foco em **Análise de Dados utilizando Python e Pandas**, aplicando conceitos de exploração, limpeza, tratamento e análise de uma base de vendas.

O projeto faz parte do meu processo de aprendizado e construção de portfólio na área de **Dados**.

## Sobre o projeto

A proposta é desenvolver um dashboard de análise de vendas a partir de uma base de dados fictícia contendo informações como:

* Data da venda
* Produto
* Categoria
* Vendedor
* Quantidade
* Preço unitário

Antes da construção do dashboard, os dados passam por uma etapa de **Data Wrangling**, na qual são investigados possíveis problemas como valores ausentes, inconsistências de texto, duplicidades e tipos de dados incorretos.

## Etapas já desenvolvidas

Até o momento foram realizadas:

* Importação da base de dados com Pandas
* Análise inicial da estrutura do DataFrame
* Verificação dos tipos das colunas
* Conversão da coluna `Data` para datetime
* Padronização dos valores da coluna `Categoria`
* Investigação e correção de categorias inconsistentes
* Identificação de valores ausentes
* Recuperação de preços unitários ausentes
* Análise estatística das colunas numéricas
* Uso de filtros com máscaras booleanas
* Uso de múltiplas condições com `&`
* Correções direcionadas utilizando `.loc[]`

## Estrutura atual

```text
projeto dashboard de vendas/
│
├── analise.py
├── .gitignore
│
└── dados/
    └── vendas.csv
```

## Tecnologias utilizadas

* Python
* Pandas
* Git
* GitHub

Tecnologias planejadas para as próximas etapas:

* Plotly
* Streamlit

## Base de dados

A base utilizada neste projeto é **fictícia** e foi criada exclusivamente para fins de estudo.

Ela contém 503 registros de vendas realizadas entre janeiro e agosto de 2026.

Algumas inconsistências foram inseridas propositalmente na base para permitir a prática de limpeza e tratamento de dados.

Entre os problemas trabalhados estão:

* Valores ausentes
* Variações na escrita de categorias
* Espaços desnecessários
* Registros duplicados
* Dados que precisam ser investigados antes da correção

## Objetivo das próximas etapas

Após concluir o tratamento e validação dos dados, o projeto seguirá para a etapa de análise, incluindo a criação de indicadores como:

* Faturamento total
* Quantidade de vendas
* Produtos mais vendidos
* Categorias com maior faturamento
* Desempenho por vendedor
* Evolução das vendas ao longo do tempo

Posteriormente, esses indicadores serão apresentados em um **dashboard interativo utilizando Streamlit e Plotly**.

## Aprendizados

O projeto está sendo desenvolvido de forma incremental, buscando não apenas chegar ao resultado final, mas também compreender o processo de análise.

Entre os principais conceitos praticados estão:

* DataFrames
* Filtros
* Máscaras booleanas
* Valores ausentes
* Padronização de dados
* Estatísticas descritivas
* Data Wrangling
* Investigação de inconsistências
* Tratamento de dados
* Versionamento com Git e GitHub

## Status do projeto

**Em desenvolvimento**

Atualmente o projeto está na etapa de **exploração, limpeza e tratamento dos dados**.

As próximas etapas envolverão análise exploratória, criação de KPIs, gráficos e desenvolvimento do dashboard.
