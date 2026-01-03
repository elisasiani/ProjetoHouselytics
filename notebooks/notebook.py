import kaggle
import zipfile
import pandas as pd

kaggle.api.authenticate()

#função para descompactar o arquivo com os datasets para o projeto
#with zipfile.ZipFile('housepricestraintestfe.zip', 'r') as zip_ref:
#   zip_ref.extractall('notebooks') #pasta destino escolhida para salvar os arqs

df = pd.read_csv('notebooks/Xtest.csv', sep=',')

print("Informações: ", df.info) # infos tipo de dados, se a muitos dados ausentes e etc
print("\n")

print("Valores vazios", df.isnull().sum())