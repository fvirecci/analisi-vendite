import pandas as pd
import random
from datetime import datetime, timedelta

# Creiamo dati finti per gli ultimi 30 giorni
dati = []
data_inizio = datetime.now() - timedelta(days=30)

for i in range(30):
    giorno = data_inizio + timedelta(days=i)
    vendite = random.randint(1000, 5000)  # Euro venduti al giorno
    dati.append({"Data": giorno.strftime("%Y-%m-%d"), "Vendite_Euro": vendite})

# Trasformiamo tutto in una tabella (DataFrame) e salviamo in CSV
df = pd.DataFrame(dati)
df.to_csv("vendite.csv", index=False)
print("File 'vendite.csv' creato con successo!")
