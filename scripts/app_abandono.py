# Script para analizar abandondo de clientes
# Todo por desarrollar

import pandas as pd

# Cargar datos de clientes
df = pd.read_csv("datos/clientes.csv")


df["segmento_valor"] = pd.qcut(df["valor"], 3, labels=["bajo", "medio", "alto"])

# Filtrar clientes que han abandonado
df_abandono = df[df["abandono"] == 1]
