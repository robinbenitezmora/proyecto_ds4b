# Script para analizar abandondo de clientes
# Todo por desarrollar

df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto']) 
