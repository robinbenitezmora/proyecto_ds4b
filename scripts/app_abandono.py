# Script para analizar abandondo de clientes
# Todo por desarrollar

import pandas as pd

# Cargar datos de clientes
df = pd.read_csv("data/clientes.csv")


df["segmento_valor"] = pd.qcut(df["valor"], 3, labels=["bajo", "medio", "alto"])
