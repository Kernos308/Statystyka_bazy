import numpy as np
from scipy.stats import bernoulli
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm
from numpy import random
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')

# zad1

wartosci = [1, 2, 3, 4, 5, 6]
prawdopodobienstwa = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

print("Wartosc oczekiwana")
oczekiwana = 0
for i in wartosci:
    oczekiwana += i * prawdopodobienstwa[i-1]
print(oczekiwana, "\n")

print("Wariancja")
wariancja = 0
for i in wartosci:
    wariancja += prawdopodobienstwa[i-1] * ((i-oczekiwana) ** 2)
print(wariancja, "\n")

print("Odchylenie standardowe")

odchylenie = wariancja ** (1/2)
print(odchylenie, "\n")

# zad2

# rozklad Bernoulliego
def pmf(x,p):
    f = p**x*(1-p)**(1-x)
    return f

p = 0.3
n = 100
rvs = []
for i in range(n):
    if np.random.rand() <= p:
        rvs.append(1)
    else:
        rvs.append(0)

bernoulli_dist = []
for i in rvs:
    bernoulli_dist.append(pmf(i, p))

# rozklad dwumianowy

r_values = list(range(n+1))
binom_dist = [binom.pmf(r, n, p) for r in r_values]

# rozklad Poissona

poisson_dist = poisson.pmf(r_values, mu=10, loc=40)


# zad3

print("Srednia, wariancja, skosnosc, kurtoza dla rozkladu Bernoulliego: \n")

bernoulli_mean, bernoulli_var, bernoulli_skew, bernoulli_kurt = bernoulli.stats(p, moments='mvsk')
print(bernoulli_mean, bernoulli_var, bernoulli_skew, bernoulli_kurt)
print("\n")

print("Srednia, wariancja, skosnosc, kurtoza dla rozkladu Dwumianowego: \n")

binom_mean, binom_var, binom_skew, binom_kurt = binom.stats(n, p, moments='mvsk')
print(binom_mean, binom_var, binom_skew, binom_kurt)
print("\n")

print("Srednia, wariancja, skosnosc, kurtoza dla rozkladu Poissona: \n")

poisson_mean, poisson_var, poisson_skew, poisson_kurt = poisson.stats(p, moments='mvsk')
print(poisson_mean, poisson_var, poisson_skew, poisson_kurt)
print("\n")

# zad4
x = np.arange(0, 100, 1)

fig, axs = plt.subplots(3)

axs[0].plot(x, bernoulli_dist)
axs[0].set_title("Rozklad Bernoulliego")

axs[1].plot(r_values, binom_dist)
axs[1].set_title("Rozklad Dwumianowy")

axs[2].plot(r_values, poisson_dist)
axs[2].set_title("Rozklad Poissona")
fig.subplots_adjust(hspace=0.8)
plt.show()


# zad 5

n = 20
k = list(range(n+1))
p = 0.4
binom_dist1 = binom.pmf(k, n, p)

print(sum(binom_dist1))

# zad6

mean = 0
std_dev = 2
normal_dist = random.normal(loc=mean, scale = std_dev, size=100)
print(normal_dist)

normal_mean, normal_var, normal_skew, normal_kurt = norm.stats(loc=mean, scale=std_dev, moments='mvsk')

print("Srednia, wariancja, skosnosc, kurtoza dla rozkladu normalnego: \n")


print(normal_mean, normal_var, normal_skew, normal_kurt)
print("\n")

# zad7

x = np.arange(0, 100, 1)
normal_dist = random.normal(1, 2, 100)
standard_dist = random.normal(1, 2, 100)
density_dist = random.normal(-1, 0.5, 100)
fig, axs = plt.subplots(3)

axs[0].hist(normal_dist, 100)
axs[0].set_title("Rozklad Normalny")

axs[1].hist(standard_dist, 100)
axs[1].set_title("Rozklad Standardowy")

axs[2].hist(density_dist, 100)
axs[2].set_title("Rozklad Gestosci")
fig.subplots_adjust(hspace=0.8)

plt.show()