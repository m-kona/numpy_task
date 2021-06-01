import numpy as np
import matplotlib as plt
nums = [0.5,0.7,1,1.2,1.3,2.1]
bins = [0,1,2,3]

x_pos = [i for i, _ in enumerate(nums)]
plt.bar(x_pos, nums, color='yellow')
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.title("Numpy Task 2")
plt.xticks(x_pos, nums)
plt.show()