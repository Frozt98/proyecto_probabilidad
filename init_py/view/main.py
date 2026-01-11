
from init_py.view.menu import Menu

# Importar listas de meses de cada año
from init_py.A2018 import meses_2018
from init_py.A2019 import meses_2019
from init_py.A2020 import meses_2020
from init_py.A2021 import meses_2021
from init_py.A2022 import meses_2022
from init_py.A2023 import meses_2023
from init_py.A2024 import meses_2024
from init_py.A2025 import meses_2025
from init_py.A2026 import meses_2026

lista_anios = [
    ("2018", meses_2018),
    ("2019", meses_2019),
    ("2020", meses_2020),
    ("2021", meses_2021),
    ("2022", meses_2022),
    ("2023", meses_2023),
    ("2024", meses_2024),
    ("2025", meses_2025),
    ("2026", meses_2026)
]

menu = Menu(lista_anios)
menu.mostrar_menu()
