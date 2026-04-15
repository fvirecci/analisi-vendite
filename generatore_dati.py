import pandas as pd
import random
from datetime import datetime, timedelta

dati = []
data_inizio = datetime.now() - timedelta(days=30)

for i in range(30):
    giorno = data_inizio + timedelta(days=i)
    meteo = random.randint(0, 1) # 0 = Sole, 1 = Pioggia
    # Simuliamo che se piove si venda meno
    base_vendite = random.randint(2000, 5000)
    vendite = base_vendite - 1000 if meteo == 1 else base_vendite
    
    dati.append({"Data": giorno.strftime("%Y-%m-%d"), "Vendite_Euro": vendite, "Pioggia": meteo})

df = pd.DataFrame(dati)
df.to_csv("vendite_meteo.csv", index=False)
print("Creato 'vendite_meteo.csv' con dati meteo!")
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
