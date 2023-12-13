from numpy import random
import pandas as pd
from scipy import stats
from scipy.stats import shapiro

# zad1

normal_dist = random.normal(2, 30, 200)
print(normal_dist.mean())
mean = 2.5

s, p_value = stats.ttest_1samp(normal_dist, mean)

print(p_value)
alfa = 0.05
if p_value < alfa:
    print("Odrzucamy hipotezę")
else:
    print("Nie ma podstaw do odrzucenia hipotezy")

# zad2

df = pd.read_csv("napoje.csv", delimiter=";")

df_grouped = df.groupby('rok')
print("### PLIK napoje.csv ###\n")
print("Srednia lecha")
mean_for_year = []
for rok, value in df_grouped['lech']:
    mean_for_year.append(stats.gmean(value))

print(sum(mean_for_year)/len(mean_for_year))
print("\n")

print("Srednia coli")
mean_for_year = []
for rok, value in df_grouped['cola']:
    mean_for_year.append(stats.gmean(value))

print(sum(mean_for_year)/len(mean_for_year))

print("\n")

print("Srednia regionalnego")
mean_for_year = []
for rok, value in df_grouped['regionalne']:
    mean_for_year.append(stats.gmean(value))

print(sum(mean_for_year)/len(mean_for_year))

#zad3

for column in df.columns:
    data = df[column]
    stat_shapiro, p_shapiro = shapiro(data)
    if p_shapiro < alfa:
        print(f'Kolumna {column} nie wykazuje normalnosci')
    else:
        print(f'Kolumna {column} wykazuje normalnosc')


drinks = [('okocim', 'lech'), ('fanta', 'regionalne'), ('cola', 'pepsi')]


for drink in drinks:
    drink1, drink2 = drink
    data1 = df[drink1]
    data2 = df[drink2]

    stat_test, p_value = stats.ttest_rel(data1, data2)

    print(f'Test t-Studenta dla par {drink1} - {drink2}:')
    print(f'Statystyka testowa: {stat_test}')
    print(f'Wartość p: {p_value}')

    if p_value < alfa:
        print('Srednie nie sa rowne')
    else:
        print('Rownosc srednich')
