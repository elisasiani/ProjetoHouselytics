import kaggle
import zipfile
import pandas as pd

kaggle.api.authenticate()

#função para descompactar o arquivo com os datasets para o projeto
#with zipfile.ZipFile('housepricestraintestfe.zip', 'r') as zip_ref:
#   zip_ref.extractall('notebooks') #pasta destino escolhida para salvar os arqs

df = pd.read_csv('notebooks/Xtest.csv', sep=',')

# Visualizar as primeiras linhas
'''print("Primeiras linhas do dataset:")
print(df.head())
print("\n")

# Informações gerais (tipos e dados nulos)
print("Informações do dataset:")
df.info()
print("\n")

# Verificar valores ausentes por coluna
print("Valores vazios por coluna:")
print(df.isnull().sum())
print("\n")

print("Tamanho do dataset:")
print(df.shape)
print("\n")

print("Tipos de dados das colunas na Tab:")
print(df.dtypes.value_counts())
print("\n")

print("Identificar colunas com 1 valor, poucos, etc:")
print(df.nunique().sort_values())
print("\n")'''

'''print("Nomes das coluns:")
for col in df.columns:
    print(col)
print("\n")'''

colunas_iniciais = [
    "LotFrontage", "LotArea", "GrLivArea", "TotalBsmtSF",
    "OverallQual", "OverallCond", "Total_Home_Quality",
    "YearBuilt", "Age", "Renovate",
    "FullBath", "HalfBath", "Total_Bathrooms",
    "BedroomAbvGr", "KitchenAbvGr", "TotRmsAbvGrd",
    "GarageCars", "GarageArea",
    "Fireplaces", "WoodDeckSF", "OpenPorchSF", "PoolArea",
    "SqFtPerRoom", "HighQualSF"
]

df_base = df[colunas_iniciais]

df_base = df_base.rename(columns={
    "LotFrontage": "Largura da frente do terreno",
    "LotArea": "Área total do terreno",
    "GrLivArea": "Área construída acima do solo",
    "TotalBsmtSF": "Área total do porão",
    "OverallQual": "Qualidade geral do imóvel",
    "OverallCond": "Condição geral do imóvel",
    "Total_Home_Quality": "Qualidade total combinada",
    "YearBuilt": "Ano de construção",
    "Age": "Idade do imóvel",
    "Renovate": "Indica se houve reforma",
    "FullBath": "Banheiros completos",
    "HalfBath": "Lavabos",
    "Total_Bathrooms": "Total de banheiros",
    "BedroomAbvGr": "Número de quartos",
    "KitchenAbvGr": "Número de cozinhas",
    "TotRmsAbvGrd": "Total de cômodos",
    "GarageCars": "Capacidade da garagem",
    "GarageArea": "Área da garagem",
    "Fireplaces": "Número de lareiras",
    "WoodDeckSF": "Área de deck",
    "OpenPorchSF": "Área de varanda aberta",
    "PoolArea": "Área da piscina",
    "SqFtPerRoom": "Área média por cômodo",
    "HighQualSF": "Área de alta qualidade"
})

print(df_base.head())