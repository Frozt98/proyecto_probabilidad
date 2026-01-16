import json
import os

# Importar todas las listas de meses
from init_py.A2018 import meses_2018
from init_py.A2019 import meses_2019
from init_py.A2020 import meses_2020
from init_py.A2021 import meses_2021
from init_py.A2022 import meses_2022
from init_py.A2023 import meses_2023
from init_py.A2024 import meses_2024
from init_py.A2025 import meses_2025
from init_py.A2026 import meses_2026

def convertir_datos_a_json():
    """
    Convierte todos los datos de los años a formato JSON
    para ser utilizados por la aplicación web
    """

    # Diccionario con todos los años
    todos_los_anios = {
        '2018': meses_2018,
        '2019': meses_2019,
        '2020': meses_2020,
        '2021': meses_2021,
        '2022': meses_2022,
        '2023': meses_2023,
        '2024': meses_2024,
        '2025': meses_2025,
        '2026': meses_2026
    }

    # Estructura para almacenar todos los datos
    datos_json = {}

    # Procesar cada año
    for anio, meses in todos_los_anios.items():
        datos_json[anio] = []

        # Procesar cada mes
        for mes_obj in meses:
            # Obtener el nombre del mes (primera fila de la columna 'Mes')
            nombre_mes = mes_obj.df['Mes'].iloc[0]

            # Crear estructura del mes
            mes_data = {
                'mes': nombre_mes,
                'dias': mes_obj.df['Día'].tolist(),
                'produccion': mes_obj.df['Producción'].tolist(),
                'gastos': mes_obj.df['Gastos'].tolist()
            }

            datos_json[anio].append(mes_data)

    # Crear directorio web si no existe
    if not os.path.exists('web'):
        os.makedirs('web')
        print("✅ Carpeta 'web' creada")

    # Guardar en archivo JSON
    ruta_json = os.path.join('web', 'datos.json')
    with open(ruta_json, 'w', encoding='utf-8') as f:
        json.dump(datos_json, f, indent=2, ensure_ascii=False)

    print(f"✅ Datos convertidos exitosamente a: {ruta_json}")

    # Mostrar resumen
    print("\n📊 Resumen de datos generados:")
    for anio, meses in datos_json.items():
        print(f"  Año {anio}: {len(meses)} meses")
        for mes in meses:
            print(f"    - {mes['mes']}: {len(mes['dias'])} días")

    return datos_json

if __name__ == "__main__":
    print("🔄 Iniciando conversión de datos Python a JSON...\n")
    try:
        convertir_datos_a_json()
        print("\n✨ ¡Proceso completado! Ahora puedes abrir web/index.html en tu navegador.")
    except Exception as e:
        print(f"\n❌ Error durante la conversión: {e}")
        print("\nAsegúrate de que:")
        print("  1. Estás ejecutando el script desde la carpeta raíz del proyecto")
        print("  2. Todas las carpetas A2018, A2019, etc. tienen archivos __init__.py")
        print("  3. Cada archivo de mes tiene la variable correcta exportada")