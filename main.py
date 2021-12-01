
import pandas as pd
import matplotlib.pyplot as plt

url = 'covid_22_noviembre.csv'
df = pd.read_csv(url, low_memory=False)

df.rename(columns={'ID de caso': 'ID'}, inplace=True)

df['Ubicación del caso'].replace('CASA', 'Casa', inplace=True)
df['Recuperado'].replace('fallecido', 'Fallecido', inplace=True)
df['Tipo de contagio'].replace('relacionado', 'Relacionado', inplace=True)
df['Tipo de contagio'].replace('RELACIONADO', 'Relacionado', inplace=True)
df['Tipo de contagio'].replace('EN ESTUDIO', 'En estudio', inplace=True)
df['Tipo de contagio'].replace('En Estudio', 'En estudio', inplace=True)
df['Sexo'].replace('m', 'M', inplace=True)
df['Sexo'].replace('f', 'F', inplace=True)

print('\n-------EJERCICIO1-------')
print('numero de casos de contagio: ' + str(len(df)))

print('\n-------EJERCICIO2-------')
municipios = df['Nombre municipio'].unique()
print('numero de municipios afectados: ' + str(len(municipios)))

print('\n-------EJERCICIO3-------')
print('municipios afectados: \n' + str(df['Nombre municipio'].unique()))

print('\n-------EJERCICIO4-------')
atencion_casa = df[df['Ubicación del caso'] == 'Casa']
print('numero de personas en casa: ' + str(len(atencion_casa)))

print('\n-------EJERCICIO5-------')
recuperados = df[df['Recuperado'] == 'Recuperado']
print('numero de personas recuperadas: ' + str(len(recuperados)))

print('\n-------EJERCICIO6-------')
fallecidas = df[df['Ubicación del caso'] == 'Fallecido']
print('numero de personas fallecidas: ' + str(len(fallecidas)))