import matplotlib.pyplot as plt

import data_loader


# Функція запитує назву країни та перевіряє її наявність у даних
def input_country(countries):
    while True:
        name = input("Введіть назву країни англійською (наприклад: Poland): ").strip()

        if name == "":
            print("Помилка: назва країни не може бути порожньою!")
            continue

        # Назва країни не може містити цифр
        has_digit = False

        for symbol in name:
            if symbol.isdigit():
                has_digit = True
                break

        if has_digit:
            print("Помилка: назва країни не може містити цифри!")
            continue

        country = data_loader.find_country(countries, name)

        if country is None:
            print("Країну", name, "не знайдено в завантажених даних. Спробуйте ще раз.")
            continue

        return country


# Функція будує стовпчасту діаграму зміни показника за роками для країни
def plot_bar(country, years, values):
    plt.figure(figsize=(8, 5))

    year_labels = []

    for year in years:
        year_labels.append(str(year))

    plt.bar(year_labels, values, color="steelblue")

    # Підписуємо значення над стовпцями
    for i in range(len(values)):
        plt.text(i, values[i], f"{values[i]:.2f}", ha="center", va="bottom", fontsize=10)

    plt.title(f"{data_loader.INDICATOR_NAME}\nin {country}", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Exports (% of GDP)", fontsize=12)
    plt.grid(True, axis="y")
    plt.show()


# Функція виконує всі дії завдання 2 по черзі
def run_task2(data):
    countries, years, values = data

    country = input_country(countries)
    country_years, country_values = data_loader.get_series(countries, years, values, country)

    print("\nЗначення показника для країни", country + ":")

    for i in range(len(country_years)):
        print(f"{country_years[i]}: {country_values[i]:.2f}%")

    plot_bar(country, country_years, country_values)


if __name__ == "__main__":
    loaded_data = data_loader.load_data()

    if loaded_data is not None:
        run_task2(loaded_data)
