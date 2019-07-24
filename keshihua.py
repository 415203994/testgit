import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("shuttle.csv")

data["field7"].hist(bins=10)
print data.describe()
plt.show()