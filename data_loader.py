import csv

import numpy as np

CSV_FILE = "exports_gdp.csv"
VALUE_COLUMN = "Exports of goods and services (% of GDP)"
INDICATOR_NAME = "Exports of goods and services (% of GDP)"


# Функція завантажує дані з CSV-файлу і повертає три списки: країни, роки, значення
def load_data(filename=CSV_FILE):
    countries = []
    years = []
    values = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                countries.append(row["Country Name"].strip())
                years.append(int(row["Year"]))
                values.append(float(row[VALUE_COLUMN]))

    except FileNotFoundError:
        print("Файл", filename, "не знайдено! Спочатку виконайте практичну роботу 5-6.")
        return None

    except (KeyError, ValueError):
        print("Помилка: файл", filename, "має неправильну структуру або некоректні дані!")
        return None

    except (OSError, csv.Error):
        print("Помилка відкриття або читання файлу:", filename)
        return None

    if len(countries) == 0:
        print("Файл не містить даних!")
        return None

    # Рахуємо, скільки різних країн є у файлі
    unique_countries = []

    for country in countries:
        if country not in unique_countries:
            unique_countries.append(country)

    print("Дані успішно завантажено з файлу:", filename)
    print("Кількість країн у файлі:", len(unique_countries))
    return countries, years, values


# Функція шукає країну в списку без урахування регістру
# і повертає назву країни так, як вона записана у файлі
def find_country(countries, name):
    for country in countries:
        if country.lower() == name.strip().lower():
            return country

    return None


# Функція формує масиви років і значень показника для вибраної країни
def get_series(countries, years, values, country):
    # Збираємо роки, для яких є дані по цій країні, і сортуємо їх
    country_years = []

    for i in range(len(countries)):
        if countries[i] == country:
            country_years.append(years[i])

    country_years.sort()

    # Для кожного року знаходимо значення показника
    country_values = []

    for year in country_years:
        for i in range(len(countries)):
            if countries[i] == country and years[i] == year:
                country_values.append(values[i])

    return np.array(country_years), np.array(country_values)
