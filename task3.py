import matplotlib.pyplot as plt
import numpy as np

import data_loader
from task1 import COUNTRY1, COUNTRY2


# Функція запитує рік, для якого є дані в обох країн
def input_year(available_years):
    years_text = ""

    for year in available_years:
        years_text = years_text + str(year) + ", "

    years_text = years_text[:-2]  # Прибираємо останню кому

    while True:
        text = input(f"Введіть рік для порівняння ({years_text}): ").strip()

        try:
            year = int(text)
        except ValueError:
            print("Помилка: рік має бути цілим числом!")
            continue

        if year not in available_years:
            print("Для цього року немає даних. Доступні роки:", years_text)
            continue

        return year


# Функція формує підпис сектора: відсоток і абсолютне значення
def make_label(pct, all_values):
    absolute = np.round(pct / 100 * np.sum(all_values), 2)
    return f"{pct:.1f}%\n({absolute})"


# Функція будує кругову діаграму порівняння двох країн за обраний рік
def plot_pie(labels, values, year):
    plt.figure(figsize=(6, 6))

    wedges, texts, autotexts = plt.pie(
        values,
        labels=labels,
        autopct=lambda pct: make_label(pct, values)
    )

    plt.title(
        f"{data_loader.INDICATOR_NAME}\n{COUNTRY1} vs {COUNTRY2} ({year})",
        fontsize=13
    )
    plt.setp(autotexts, size=10, weight="bold")
    plt.show()


# Функція виконує всі дії завдання 3 по черзі
def run_task3(data):
    countries, years, values = data

    country1 = data_loader.find_country(countries, COUNTRY1)
    country2 = data_loader.find_country(countries, COUNTRY2)

    # Перевірка наявності країн у завантажених даних
    if country1 is None or country2 is None:
        print("У файлі немає даних для країн:", COUNTRY1, "або", COUNTRY2)
        return

    years1, values1 = data_loader.get_series(countries, years, values, country1)
    years2, values2 = data_loader.get_series(countries, years, values, country2)

    # Беремо тільки ті роки, які є в обох країн
    common_years = []

    for year in years1:
        if year in years2:
            common_years.append(int(year))

    if len(common_years) == 0:
        print("Немає спільних років для порівняння!")
        return

    year = input_year(common_years)

    # Знаходимо значення показника для обраного року
    index1 = list(years1).index(year)
    index2 = list(years2).index(year)

    pie_values = np.array([values1[index1], values2[index2]])
    labels = np.array([country1, country2])

    plot_pie(labels, pie_values, year)


if __name__ == "__main__":
    loaded_data = data_loader.load_data()

    if loaded_data is not None:
        run_task3(loaded_data)
