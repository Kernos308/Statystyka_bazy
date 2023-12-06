from numpy import random
import pandas as pd
from scipy import stats


# zad1

normal_dist = random.normal(2, 30, 200)
print(normal_dist.mean())

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