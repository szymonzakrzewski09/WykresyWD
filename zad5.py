import numpy as np
import matplotlib.pyplot as plt
plt.subplot(1, 3, 1)
grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
grouped.plot.bar(color=['r', 'g'])
plt.xlabel('Płeć')
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.ylabel('Liczba narodzonych dzieci')
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
y = df.groupby('Rok').agg({'Liczba':['sum']}).values.flatten() plt.bar(x, y)
plt.show()