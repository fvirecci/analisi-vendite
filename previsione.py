import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Carichiamo i dati
df = pd.read_csv("vendite.csv")
df['Giorno_Num'] = np.arange(len(df)).reshape(-1, 1) # Trasformiamo le date in numeri (0, 1, 2...)

# 2. Addestriamo l'AI (Modello di Regressione)
X = df[['Giorno_Num']] # Input: il tempo
y = df['Vendite_Euro'] # Output: i soldi
modello = LinearRegression()
modello.fit(X, y)

# 3. Prevediamo le vendite per domani (Giorno 31)
prossimo_giorno = np.array([[30]]) 
previsione = modello.predict(prossimo_giorno)

print(f"--- ANALISI PREDITTIVA ---")
print(f"Previsione vendite per domani: {previsione[0]:.2f} €")

# Calcoliamo la tendenza (se cresce o cala)
if modello.coef_[0] > 0:
    print("Trend: In crescita! 🚀")
else:
    print("Trend: In calo. 📉")
