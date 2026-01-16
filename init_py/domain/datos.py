# datos.py
import pandas as pd

class DatosAnio:
    def __init__(self, anio, meses, dias, produccion, gastos):
        self.anio = anio
        self.df = pd.DataFrame({
            'Mes': meses,
            'Día': dias,
            'Producción': produccion,
            'Gastos': gastos
        })
        self.mes = meses[0]

    def filtrar_mes(self, mes):
        return self.df[self.df['Mes'] == mes]
