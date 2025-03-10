#%%
import sys 
import math
import random
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0,20,100)
plt.plot(p,np.sin(p))
plt.show()

#%%
import matplotlib.pyplot as plt

#%%
cat = ["bored", "happy", "bored"]
dog = ["happy", "bored", "happy"]
activity = ["combing", "drinking", "feeding"]

fig, ax = plt.subplots()
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.show()

#%%
