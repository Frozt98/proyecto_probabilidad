from init_py.domain.frecuencia import TablaFrecuencia
import pandas as pd

class Menu:
    def __init__(self, lista_anios):
        self.lista_anios = lista_anios

    def mostrar_menu(self):
        while True:
            print("\n==== Menú de Análisis de Producción y Costo de Petroleo ====")
            print("1. Filtrar por Año y Mes")
            print("2. Análisis Anual")
            print("0. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '0':
                print("Saliendo...")
                break
            elif opcion == '1':
                self.seleccionar_anio_mes()
            elif opcion == '2':
                self.seleccionar_anio_anual()
            else:
                print("Opción inválida")

    def seleccionar_anio_mes(self):
        print("\nSelecciona un año:")
        for i, (anio_str, _) in enumerate(self.lista_anios, 1):
            print(f"{i}. {anio_str}")
        seleccion = int(input("Selecciona el año: ")) - 1
        anio_obj = self.lista_anios[seleccion][1]

        print("\nSelecciona un mes:")
        for i, mes_obj in enumerate(anio_obj, 1):
            print(f"{i}. {mes_obj.df['Mes'].iloc[0]}")
        seleccion_mes = int(input("Selecciona el mes: ")) - 1
        mes_obj = anio_obj[seleccion_mes]

        df_filtrado = mes_obj.df

        # DEBUG: Verificar nombres de columnas
        print(f"\nColumnas disponibles: {df_filtrado.columns.tolist()}")

        # Producción
        print("\n--- Producción ---")
        tf_prod = TablaFrecuencia(df_filtrado, 'Producción')
        tf_prod.calcular_clases()
        tf_prod.crear_tabla_frecuencia()

        # Mostrar tabla gráfica
        tf_prod.mostrar_tabla_grafica(title=f'Tabla de Frecuencias - Producción ({df_filtrado["Mes"].iloc[0]} {mes_obj.anio})')

        # Mostrar histograma
        tf_prod.graficar_histograma(title=f'Producción - {df_filtrado["Mes"].iloc[0]} {mes_obj.anio}')

        # Costo de petroleo
        print("\n--- Costo del petroleo ---")

        # Intentar encontrar la columna correcta
        columna_costo = None
        posibles_nombres = ['Costo de petroleo', 'Precio del petroleo', 'Gastos', 'Costo', 'Precio']

        for nombre in posibles_nombres:
            if nombre in df_filtrado.columns:
                columna_costo = nombre
                print(f"Usando columna: {columna_costo}")
                break

        if columna_costo is None:
            print(f"ERROR: No se encontró columna de costos. Columnas disponibles: {df_filtrado.columns.tolist()}")
            return

        tf_costo = TablaFrecuencia(df_filtrado, columna_costo)
        tf_costo.calcular_clases()
        tf_costo.crear_tabla_frecuencia()

        # Mostrar tabla gráfica
        tf_costo.mostrar_tabla_grafica(title=f'Tabla de Frecuencias - Precio del petroleo ({df_filtrado["Mes"].iloc[0]} {mes_obj.anio})')

        # Mostrar histograma
        tf_costo.graficar_histograma(title=f'Precio del petroleo - {df_filtrado["Mes"].iloc[0]} {mes_obj.anio}')

    def seleccionar_anio_anual(self):
        print("\nSelecciona un año para análisis anual:")
        for i, (anio_str, _) in enumerate(self.lista_anios, 1):
            print(f"{i}. {anio_str}")
        seleccion = int(input("Selecciona el año: ")) - 1
        anio_str, meses = self.lista_anios[seleccion]

        # Combinar todos los meses del año
        df_anual = pd.concat([mes.df for mes in meses], ignore_index=True)

        # DEBUG: Verificar nombres de columnas
        print(f"\nColumnas disponibles: {df_anual.columns.tolist()}")

        # Producción
        print(f"\n--- Producción - Año completo {anio_str} ---")
        tf_prod = TablaFrecuencia(df_anual, 'Producción')
        tf_prod.calcular_clases()
        tf_prod.crear_tabla_frecuencia()

        # Mostrar tabla gráfica
        tf_prod.mostrar_tabla_grafica(title=f'Tabla de Frecuencias - Producción (Año {anio_str})')

        # Mostrar histograma
        tf_prod.graficar_histograma(title=f'Producción - Año completo {anio_str}')

        # Costo de petroleo - intentar con diferentes nombres posibles
        print(f"\n--- Precio del petroleo - Año completo {anio_str} ---")

        # Intentar encontrar la columna correcta
        columna_costo = None
        posibles_nombres = ['Precio de petroleo', 'Costo del petroleo', 'Gastos', 'Costo']

        for nombre in posibles_nombres:
            if nombre in df_anual.columns:
                columna_costo = nombre
                print(f"Usando columna: {columna_costo}")
                break

        if columna_costo is None:
            print(f"ERROR: No se encontró columna de costos. Columnas disponibles: {df_anual.columns.tolist()}")
            return

        tf_costo = TablaFrecuencia(df_anual, columna_costo)
        tf_costo.calcular_clases()
        tf_costo.crear_tabla_frecuencia()

        # Mostrar tabla gráfica
        tf_costo.mostrar_tabla_grafica(title=f'Tabla de Frecuencias - Precio del petroleo (Año {anio_str})')

        # Mostrar histograma
        tf_costo.graficar_histograma(title=f'Precio del petroleo - Año completo {anio_str}')