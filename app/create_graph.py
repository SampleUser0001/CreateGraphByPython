import pandas as pd
from matplotlib import pyplot as plt

# print('Hello Python!!')
df = pd.read_csv('./input/free-mem.csv', names=['time','value'])
plt.plot(df['time'],df['value'],marker=",")
# plt.show()
plt.savefig('graph.png')
