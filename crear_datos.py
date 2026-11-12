import pandas as pd

datos = {
    'Id': [1, 2, 3, 4, 5],
    'Nombre': ['juan perez', 'ana lopez', 'dario ojeda', 'rosa fuentes', 'domingo masias'],
    'Profesion': ['ingeniero', 'contador', 'medico', 'psicologa', 'programador'],
    'Sueldo': [200, 180, 350, 190, 250]
}

df = pd.DataFrame(datos)
df.to_excel('datos.xlsx', index=False)
print("datos.xlsx creado exitosamente")

