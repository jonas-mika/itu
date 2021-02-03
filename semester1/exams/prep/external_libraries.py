import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random

# load dataset
# data = pd.read_csv("test.csv")

# print(data)
# print("\n" + "-"*5 + "DATATYPES" + "-"*5 + "\n")
# print(data.dtypes)

def fivenumsum(data):
	return np.percentile(data, [0, 25, 50, 75, 100], interpolation="midpoint")

example = [0,0,1,2,63,61,27,13]
# print(fivenumsum(example)) # [0 , 0.5 , 7.5 , 44 , 63]

#plt.boxplot(example)
#plt.show()

# genders = [random.choice([0,1]) for _ in range(20)]
# uniques, counts = np.unique(genders, return_counts=True)

# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,9))

# axes[0].bar(uniques, counts)
# axes[1].pie(counts)

# axes[0].set_xticks(uniques)
# axes[0].set_xticklabels(["Male", "Female"])
# axes[0].set_xlabel("Categories")
# axes[0].set_ylabel("Counts")

# for ax in axes:
#     ax.set_xlabel("Categories")
#     ax.set_ylabel("Counts")
#     ax.set_title("Gender Distribution")
# plt.savefig("plot_categorical_data.png")


numerical_data = [random.random()*5 for _ in range(50)]
print(numerical_data)