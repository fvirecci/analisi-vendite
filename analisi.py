import pandas as pd

# 1. Carichiamo i dati dal file che abbiamo creato prima
df = pd.read_csv("vendite.csv")

# 2. Calcoliamo un po' di statistiche (Insight)
media = df["Vendite_Euro"].mean()
totale = df["Vendite_Euro"].sum()
giorno_migliore = df.loc[df["Vendite_Euro"].idxmax()]

# 3. Stampiamo i risultati a video
print("--- INSIGHT VENDITE ---")
print(f"Totale incassato: {totale} €")
print(f"Media giornaliera: {media:.2f} €")
print(f"Giorno record: {giorno_migliore['Data']} con {giorno_migliore['Vendite_Euro']} €")

# 4. Una piccola "previsione" molto semplice
print(f"\nPrevisione mese prossimo (basata su media): {media * 30:.2f} €")
