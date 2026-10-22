import matplotlib.pyplot as plt

import data_loader

# Країни для аналізу динаміки показника
COUNTRY1 = "Ukraine"
COUNTRY2 = "Poland"


# Функція виводить короткий аналіз зміни показника в часі для країни
def analyze(country, years, values):
    change = values[-1] - values[0]

    if change > 0:
        trend = "зростання"
    elif change < 0:
        trend = "спадання"
    else:
        trend = "без змін"

    print(
        f"{country}: {years[0]} р. - {values[0]:.2f}%, "
        f"{years[-1]} р. - {values[-1]:.2f}%, "
        f"зміна: {change:+.2f} в.п. ({trend})"
    )


# Функція будує лінійний графік динаміки показника для двох країн
def plot_line(years1, values1, years2, values2):
    plt.figure(figsize=(8, 5))

    plt.plot(years1, values1, marker="o", label=COUNTRY1)
    plt.plot(years2, values2, marker="o", label=COUNTRY2)

    plt.title(
        f"{data_loader.INDICATOR_NAME}\nfor {COUNTRY1} and {COUNTRY2}",
        fontsize=14
    )
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Exports (% of GDP)", fontsize=12)

    # На осі X відображаємо тільки цілі роки
    plt.xticks(years1)

    plt.legend()
    plt.grid(True)
    plt.show()


# Функція виконує всі дії завдання 1 по черзі
def run_task1(data):
    countries, years, values = data

    country1 = data_loader.find_country(countries, COUNTRY1)
    country2 = data_loader.find_country(countries, COUNTRY2)

    # Перевірка наявності країн у завантажених даних
    if country1 is None or country2 is None:
        print("У файлі немає даних для країн:", COUNTRY1, "або", COUNTRY2)
        return

    years1, values1 = data_loader.get_series(countries, years, values, country1)
    years2, values2 = data_loader.get_series(countries, years, values, country2)

    print("\nАналіз зміни показника в часі:")
    analyze(COUNTRY1, years1, values1)
    analyze(COUNTRY2, years2, values2)

    plot_line(years1, values1, years2, values2)


if __name__ == "__main__":
    loaded_data = data_loader.load_data()

    if loaded_data is not None:
        run_task1(loaded_data)
