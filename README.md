# Proyecto - Manejando y Transformando Excel con Python

Este proyecto implementa la lectura, transformación y exportación de archivos de Excel utilizando **Python** y **Pandas**.

## Requerimientos y Transformaciones realizadas

1. **Transformación de Id:** Compuesto por la primera letra y la última letra del nombre (en mayúscula) concatenadas con su valor numérico original (ej. `JZ1`).
2. **Formato de Nombre:** Nombre y apellido formateados en formato título (`Juan Perez`).
3. **Formato de Profesión:** Convertido a mayúsculas (`INGENIERO`).
4. **Cálculo de Columna Total:** Ubicada después del sueldo, calculada como `Sueldo - (20% de impuesto)`.
5. **Columna Indice:** Generada de forma numérica secuencial al inicio y con formato visual centrado.

## Estructura del Proyecto

* `app.py`: Script principal de procesamiento y transformación.
* `datos.xlsx`: Archivo Excel de entrada original.
* `excel_procesado.xlsx`: Archivo Excel generado con las transformaciones.
* `crear_datos.py`: Script auxiliar para regenerar los datos base.
* `requirements.txt`: Dependencias del proyecto (`pandas`, `openpyxl`).

## Instalación y Ejecución

```bash
# 1. Crear y activar entorno virtual
python -m venv .venv
source .venv/Scripts/activate  # En Windows: .venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el proyecto
python app.py
```

