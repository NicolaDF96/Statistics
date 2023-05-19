#pip install pandas
#pip install openpyxl

import pandas as pd

def leggi_file_excel(nome_file):
    try:
        dati = pd.read_excel(nome_file)
        array_dati = dati.values.tolist()
        return array_dati
    except FileNotFoundError:
        print(f"Il file '{nome_file}' non è stato trovato.")
        return []
    except Exception as e:
        print("Si è verificato un errore durante la lettura del file.")
        print(e)
        return []

# Specifico nome file excel
nome_file_excel = "Throughput553.xlsx"  # Percorso del file Excel

#Carico i dati nell'array
dati_array = leggi_file_excel(nome_file_excel)

# Stampo l'array dei dati caricati in precedenza
for riga in dati_array:
    print(riga)