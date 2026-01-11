# frecuencia.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class TablaFrecuencia:
    def __init__(self, df, columna):
        self.df = df
        self.columna = columna
        self.clases = []
        self.num_clases = 0
        self.tabla = pd.DataFrame()

    def calcular_clases(self):
        datos = self.df[self.columna].values
        n = len(datos)
        pot = 1
        while 2**pot < n:
            pot += 1
        self.num_clases = pot

        min_val = datos.min()
        max_val = datos.max()
        ancho = (max_val - min_val) / self.num_clases

        self.clases = []
        for i in range(self.num_clases):
            inf = min_val + i*ancho
            sup = inf + ancho
            self.clases.append((inf, sup))

    def crear_tabla_frecuencia(self):
        datos = self.df[self.columna].values
        frec_abs = []
        frec_rel = []

        for i, (inf, sup) in enumerate(self.clases):
            if i == self.num_clases - 1:
                conteo = np.sum((datos >= inf) & (datos <= sup))
            else:
                conteo = np.sum((datos >= inf) & (datos < sup))
            frec_abs.append(conteo)
            frec_rel.append(conteo / len(datos))

        frec_acum = np.cumsum(frec_abs)

        # CORRECCIÓN 1: Renombrar la columna para que se vea claramente
        self.tabla = pd.DataFrame({
            'Clase inferior': [c[0] for c in self.clases],
            'Clase superior': [c[1] for c in self.clases],
            'Frecuencia absoluta': frec_abs,  # <- CAMBIADO de 'Frecuencia'
            'Frecuencia relativa': frec_rel,
            'Frecuencia acumulada': frec_acum
        })
        return self.tabla

    def calcular_estadisticos(self):
        datos = self.df[self.columna].values
        media = np.mean(datos)
        mediana = np.median(datos)
        mod = stats.mode(datos, keepdims=True)
        moda = mod.mode[0] if len(mod.mode) > 0 else None
        varianza = np.var(datos, ddof=1)
        desviacion = np.std(datos, ddof=1)
        return {
            'media': media,
            'mediana': mediana,
            'moda': moda,
            'varianza': varianza,
            'desviacion': desviacion
        }

    def mostrar_tabla_grafica(self, title='Tabla de Frecuencias'):
        """Muestra la tabla de frecuencias en una ventana gráfica"""
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.axis('tight')
        ax.axis('off')

        # Formatear los datos para la tabla
        tabla_formato = self.tabla.copy()
        tabla_formato['Clase inferior'] = tabla_formato['Clase inferior'].map('{:.2f}'.format)
        tabla_formato['Clase superior'] = tabla_formato['Clase superior'].map('{:.2f}'.format)
        tabla_formato['Frecuencia relativa'] = tabla_formato['Frecuencia relativa'].map('{:.4f}'.format)

        tabla_visual = ax.table(cellText=tabla_formato.values,
                                colLabels=tabla_formato.columns,
                                cellLoc='center',
                                loc='center',
                                bbox=[0, 0, 1, 1])

        tabla_visual.auto_set_font_size(False)
        tabla_visual.set_fontsize(9)
        tabla_visual.scale(1, 2)

        # Colorear el encabezado
        for i in range(len(tabla_formato.columns)):
            tabla_visual[(0, i)].set_facecolor('#4CAF50')
            tabla_visual[(0, i)].set_text_props(weight='bold', color='white')

        plt.title(title, fontsize=14, weight='bold', pad=20)
        plt.tight_layout()
        plt.show()

    def graficar_histograma(self, title='Histograma'):
        datos = self.df[self.columna].values
        # Crear figura con espacio extra abajo para las estadísticas
        fig, ax = plt.subplots(figsize=(12, 8))

        bins = [c[0] for c in self.clases] + [self.clases[-1][1]]
        ax.hist(datos, bins=bins, edgecolor='black', alpha=0.7)
        ax.set_title(title)
        ax.set_xlabel(self.columna)
        ax.set_ylabel('Frecuencia')

        stats_dict = self.calcular_estadisticos()

        # Formatear las estadísticas en una línea horizontal
        stats_text = (
            f"Media: {stats_dict['media']:.2f}  |  "
            f"Mediana: {stats_dict['mediana']:.2f}  |  "
            f"Moda: {stats_dict['moda']:.2f}  |  "
            f"Varianza: {stats_dict['varianza']:.2f}  |  "
            f"Desviación estándar: {stats_dict['desviacion']:.2f}"
        )

        # Colocar el texto debajo del gráfico usando coordenadas de la figura
        fig.text(0.5, 0.02, stats_text,
                 ha='center',
                 fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))

        # Ajustar para dar espacio al texto inferior
        plt.subplots_adjust(bottom=0.12)
        plt.show()