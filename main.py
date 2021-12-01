
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

print('\n-------EJERCICIO7-------')
tipos_casos = df.groupby('Tipo de contagio').count()
print(tipos_casos['ID'].sort_values(ascending=False))

print('\n-------EJERCICIO8-------')
departamentos = df['Nombre departamento'].unique()
print('numero de departamentos afectados: ' + str(len(departamentos)))

print('\n-------EJERCICIO9-------')
print('departamentos afectados: \n' + str(df['Nombre departamento'].unique()))

print('\n-------EJERCICIO10-------')
tipos_casos = df.groupby('Ubicación del caso').count()
print(tipos_casos['ID'].sort_values(ascending=False))

print('\n-------EJERCICIO11-------')
dep_conta = df.groupby('Nombre departamento').count()
top_10_dep = dep_conta['ID'].sort_values(ascending=False).head(10)
print(top_10_dep)

print('\n-------EJERCICIO12-------')
dep_falle = df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').count()
print(dep_falle['ID'].sort_values(ascending=False).head(10))

print('\n-------EJERCICIO13-------')
dep_recu = df[df['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').count()
print(dep_recu['ID'].sort_values(ascending=False).head(10))

print('\n-------EJERCICIO14-------')
mun_conta = df.groupby('Nombre municipio').count()
top_10_mun = mun_conta['ID'].sort_values(ascending=False).head(10)
print(top_10_mun)

print('\n-------EJERCICIO15-------')
mun_falle = df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').count()
print(mun_falle['ID'].sort_values(ascending=False).head(10))

print('\n-------EJERCICIO16-------')
mun_recu = df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').count()
print(mun_recu['ID'].sort_values(ascending=False).head(10))

print('\n-------EJERCICIO17-------')
print(df.groupby('Nombre departamento').count())

print('\n-------EJERCICIO18-------')
contageado_sexo = df.groupby('Sexo')
print(contageado_sexo.count()['ID'])

print('\n-------EJERCICIO19-------')
list_by = ['Sexo', 'Nombre municipio', 'Nombre departamento']
print(df.groupby(list_by)['Edad'].mean())

print('\n-------EJERCICIO20-------')
pais_procedencia = df.groupby('Nombre del país').count()
print(pais_procedencia['ID'].sort_values(ascending=False))

print('\n-------EJERCICI21-------')
print(df.sort_values(ascending=False, by='Fecha de diagnóstico'))

print('\n-------EJERCICIO22-------')
tasa_mortalidad = (len(df[df['Ubicación del caso'] == 'Fallecido']) / len(df)) * 100
tasa_recuperacion = (len(df[df['Recuperado'] == 'Recuperado']) / len(df)) * 100
print('tasa de mortalidad: ' + "{:.6f}".format(tasa_mortalidad))
print('tasa de recuperación: ' + "{:.6f}".format(tasa_recuperacion))