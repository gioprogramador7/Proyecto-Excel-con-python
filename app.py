# 1. La columna Id tiene que ser 
#    transformada = La primera letra
#    del nombre y la ultima
#    concatenado con su valor numerico
#    ejemplo:  JZ1

# 2. La columna nombre tiene tener
#    El nombre y el apellido comenzando
#    con mayuscula
#    ejemplo:  Juan Perez

# 3. La columna profesion debera estar
#    en mayuscula

# 4. Crear una nueva columna 'Total' despues
#    sueldo, que sera igual al 
#    sueldo - impuesto (20% del sueldo)
#    ejemplo:  200 - 40 = 160

# 5. Crear una nueva columna que se llame
#    Indice, sera una columna autogenerada
#    numerica y secuencial.
#    Se debe ubicar como la primera columna
#    1 - Juan Perez, 5 - Domingo Masias

import pandas as pd

data_personas=pd.read_excel('datos.xlsx')

print("--- Datos iniciales ---")
print(data_personas.head())

# Requisito 1: Id con primera y última letra del nombre en mayúscula + valor numérico
data_personas['Id']=data_personas['Nombre'].astype(str).str.upper().str[0] +\
                    data_personas['Nombre'].astype(str).str.upper().str[-1] +\
                    data_personas['Id'].astype(str)

# Requisito 2: Nombre en formato Título (primera letra de cada palabra en mayúscula)
data_personas['Nombre']=data_personas['Nombre'].astype(str).str.title()

# Requisito 3: Profesión en mayúsculas
data_personas['Profesion']=data_personas['Profesion'].astype(str).str.upper()

# Requisito 4: Columna Total = Sueldo - 20%
data_personas['Total']=data_personas['Sueldo'] - data_personas['Sueldo']*0.2

# Requisito 5: Columna Indice numérica secuencial (1 al n)
data_personas['Indice']=range(1, len(data_personas)+1)

# Reordenar las columnas para ubicar 'Indice' al inicio
data_personas=data_personas[['Indice', 'Id','Nombre','Profesion','Sueldo','Total']]

# Formateo visual centrado para el índice
data_personas['Indice']=data_personas['Indice'].astype(str).str.center(20)

print("\n--- Datos procesados ---")
print(data_personas)

# Exportar a Excel
data_personas.to_excel('excel_procesado.xlsx', index=False)
print("\n¡Archivo 'excel_procesado.xlsx' generado con éxito!")
