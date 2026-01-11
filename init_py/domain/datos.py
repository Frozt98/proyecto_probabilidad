# datos.py
import pandas as pd

class DatosAnio:
    def __init__(self, anio, meses, dias, produccion, gastos):
        """
        Guarda todos los datos diarios de un año
        """
        self.anio = anio
        self.df = pd.DataFrame({
            'Mes': meses,
            'Día': dias,
            'Producción': produccion,
            'Gastos': gastos
        })
        self.mes = meses[0]  # Asume que todos los datos son del mismo mes

    def filtrar_mes(self, mes):
        return self.df[self.df['Mes'] == mes]
