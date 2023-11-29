import matplotlib
import pandas as pd
import numpy as np
from statistics import median
from scipy import stats
import matplotlib.pyplot as plt
from pandas import plotting

matplotlib.use('TKAgg')

# zad1
df = pd.read_csv("MDR_RR_TB_burden_estimates_2023-11-29.csv", delimiter=",")
print("### PLIK MDR_RR_TB_burden_estimates_2023-11-29.csv ###\n")
print("Wartosc min: ", min(df["e_inc_rr_num"]))
print("Wartosc max: ", max(df["e_inc_rr_num"]))
print("Wartosc srednia: ", df["e_inc_rr_num"].mean())
print("Odchylenie standardowe: ", df["e_inc_rr_num"].std())
print("Mediana: ", df["e_inc_rr_num"].median(), "\n")

# zad2
data = np.loadtxt("Wzrost.csv", delimiter=',', skiprows=0, unpack=True)
print("### PLIK Wzrost.csv ###\n")
print("Wartosc min: ", data.min())
print("Wartosc max: ", data.max())
print("Wartosc srednia: ", data.mean())
print("Odchylenie standardowe: ", data.std())
print("Mediana: ", median(data), "\n")

# zad3
df = pd.read_csv("napoje.csv", delimiter=";")
df_grouped = df.groupby('rok')
print("### PLIK napoje.csv ###\n")
print("Srednia")
for rok, value in df_grouped['lech']:
    print((rok, stats.gmean(value)))
print("\n")

print("Minimalna")
for rok, value in df_grouped['okocim']:
    print((rok, stats.tmin(value)))
print("\n")

print("Maksymalna")
for rok, value in df_grouped['fanta ']:
    print((rok, stats.tmax(value)))
print("\n")

print("Odchylenie standardowe")
for rok, value in df_grouped['pepsi']:
    print((rok, stats.tstd(value)))
print("\n")

print("Wariancja")
for rok, value in df_grouped['regionalne']:
    print((rok, stats.variation(value)))
print("\n")

print("Entropia")
for rok, value in df_grouped['żywiec']:
    print((rok, stats.entropy(value)))
print("\n")

print("Bayes")
for rok, value in df_grouped['cola']:
    print((rok, stats.bayes_mvs(value)))
print("\n")

# zad4
df = pd.read_csv("brain_size.csv", delimiter=";")
df_women = df.loc[df['Gender'] == "Female"]
print("### PLIK brain_size.csv ###\n")
print("Srednia: ", df["VIQ"].mean())
print("Kobiety: ", len(df.loc[df['Gender'] == "Female"]))
print("Mezczyzni: ", len(df.loc[df['Gender'] == "Male"]))


df_women['Height'] = pd.to_numeric(df_women["Height"])
df_women['Weight'] = pd.to_numeric(df_women["Weight"])
# plotting.scatter_matrix(df[["VIQ", "PIQ", "FSIQ"]])
plotting.scatter_matrix(df_women[["Weight", "Height", "MRI_Count"]])
plt.show()

