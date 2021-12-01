
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

print('\n-------EJERCICIO23-------')
print('tasa de mortalidad:')
print(df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').count()['ID'] / len(df) * 100)
print('\ntasa de recuperación:')
print(df[df['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').count()['ID'] / len(df) * 100)

print('\n-------EJERCICIO24-------')
print('tasa de mortalidad:')
print(df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').count()['ID'] / len(df) * 100)
print('\ntasa de recuperación:')
print(df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').count()['ID'] / len(df) * 100)

print('\n-------EJERCICIO25-------')
print(df.groupby(['Nombre municipio', 'Ubicación del caso'])['ID'].count())

print('\n-------EJERCICI26-------')
print(df.groupby(['Nombre municipio'])['Edad'].mean())

print('\n-------EJERCICIO27-------')
aten = df.groupby('Fecha de diagnóstico')['ID'].count()
df.groupby('Fecha de diagnóstico')['ID'].count().cumsum().plot()
ate_fe = df.groupby(['Recuperado', 'Fecha de diagnóstico'])['ID'].count()
falle_recu = df.groupby(['Recuperado', 'Fecha de diagnóstico'])['ID'].count().unstack(0).fillna(0)
falle_recu.cumsum().plot(y=['Fallecido', 'Recuperado'], title='27)')
plt.show()

print('\n-------EJERCICIO28-------')
array_dep = list(df.groupby('Nombre departamento').count()['ID'].sort_values(ascending=False).head(10).keys())
only_10_dep = df[df['Nombre departamento'].isin(array_dep)]
groupby = ['Nombre departamento', 'Fecha de diagnóstico']
con_10_dep = only_10_dep.groupby(groupby)['ID'].count()
# contagiados
df_co_dep = con_10_dep.unstack(0).fillna(0)
df_co_dep.cumsum().plot(subplots=True, figsize=(14, 7), title='28)Contagiado')
# recuperados
groupby2 = ['Recuperado', 'Nombre departamento', 'Fecha de diagnóstico']
con_10_dep2 = only_10_dep.groupby(groupby2)['ID'].count()
df_co_depR = con_10_dep2['Recuperado'].unstack(0).fillna(0)
df_co_depR.cumsum().plot(subplots=True, figsize=(14, 7), title='28)Recuperado')
# fallecidos
df_co_depF = con_10_dep2['Fallecido'].unstack(0).fillna(0)
df_co_depF.cumsum().plot(subplots=True, figsize=(14, 7), title='28)Fallecido')
plt.show()

print('\n-------EJERCICIO29-------')
array_mun = list(df.groupby('Nombre municipio').count()['ID'].sort_values(ascending=False).head(10).keys())
only_10_mun = df[df['Nombre municipio'].isin(array_mun)]
groupby = ['Nombre municipio', 'Fecha de diagnóstico']
con_10_mun = only_10_mun.groupby(groupby)['ID'].count()
# contagiados
df_co_mun = con_10_mun.unstack(0).fillna(0)
df_co_mun.cumsum().plot(subplots=True, figsize=(14, 7), title='29)Contagiado')
# recuperados
groupby2 = ['Recuperado', 'Nombre municipio', 'Fecha de diagnóstico']
con_10_mun2 = only_10_mun.groupby(groupby2)['ID'].count()
df_co_munR = con_10_mun2['Recuperado'].unstack(0).fillna(0)
df_co_munR.cumsum().plot(subplots=True, figsize=(14, 7), title='29)Recuperado')
# fallecidos
df_co_munF = con_10_mun2['Fallecido'].unstack(0).fillna(0)
df_co_munF.cumsum().plot(subplots=True, figsize=(14, 7), title='29)Fallecido')
plt.show()

print('\n-------EJERCICIO30-------')
print(df.groupby('Edad')['ID'].count().sort_values(ascending=False))

print('\n-------EJERCICIO31-------')
por_atencion = df.groupby('Ubicación del caso')['ID'].count()
print(por_atencion.sort_values(ascending=False) / len(df) * 100)

print('\n-------EJERCICIO32-------')
df.groupby('Ubicación del caso')['ID'].count().plot(subplots=True, kind='bar', title='32)')
plt.show()

print('\n-------EJERCICIO33-------')
por_sexo = df.groupby('Sexo')['ID'].count()
por_sexo.plot(subplots=True, kind='bar', title='33)')
plt.show()

