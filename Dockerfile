FROM python:3.12-slim

WORKDIR /app

# Copiamo solo i file necessari
COPY requirements.txt .
COPY previsione_meteo.py .
COPY vendite_meteo.csv .

# Installiamo le librerie
RUN pip install pandas scikit-learn

# Comando per avviare l'analisi
CMD ["python", "previsione_meteo.py"]
