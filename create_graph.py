import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('input/free-mem.csv', names=['time','value'])
plt.plot(df['time'],df['value'],marker=",")
plt.show()
