import pandas as pd
def dameStatus(carga, entregado):
    percentage = entregado / carga
    if ( (percentage <= 0.9) or (percentage >= 1.1) ):
        return 'DEFECTO'
    return 'OK'
df = pd.read_csv('datos.csv')
df['status'] = df.apply( lambda row: dameStatus(row['Carga'], row['entregado']), axis=1 )
df.to_csv('procesado.csv')