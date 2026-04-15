import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("vendite_meteo.csv")

# Input: Pioggia (0 o 1)
X = df[['Pioggia']] 
y = df['Vendite_Euro']

modello = LinearRegression()
modello.fit(X, y)

# Prepariamo i dati per la previsione come una tabella con i nomi corretti
dati_sole = pd.DataFrame([[0]], columns=['Pioggia'])
dati_pioggia = pd.DataFrame([[1]], columns=['Pioggia'])

# Estraiamo il primo valore [0] del risultato per poterlo stampare
prev_sole = modello.predict(dati_sole)[0]
prev_pioggia = modello.predict(dati_pioggia)[0]

print(f"Previsione se domani c'è SOLE: {prev_sole:.2f} €")
print(f"Previsione se domani PIOVE: {prev_pioggia:.2f} €")
