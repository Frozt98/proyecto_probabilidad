from init_py.domain.datos import DatosAnio


meses = ['Enero']*8
dias = list(range(1, 9))
produccion = [454847.86,
              463181.29,
              463340.84,
              468551.74,
              469523.05,
              469959.33,
              472017.61,
              472169.73,

              ]
gastos = [58.32,
57.32,
57.76,
55.99,
57.13,
57.32,
57.42,
57.32,
]

enero2026 = DatosAnio(2026, meses, dias, produccion, gastos)