import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
explode = [0.0 for n in range(len(policzone.index))]
explode[np.random.randint(0, len(policzone.index) + 1)] = 0.2
policzone.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, explode=explode, shadow=True)
plt.title("Procentowy udział kwot zamówień sprzedawców")
plt.show()