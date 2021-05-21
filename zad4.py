import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('iris.data', sep=',', decimal='.', header=None)
print(df)
colors = np.random.randint(0, 50, len(df.index))
scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) for x in range(len(df.index))]
scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) * 5 for x in range(len(df.index))]
plt.scatter(df[0], df[1], c=colors, s=scale)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()