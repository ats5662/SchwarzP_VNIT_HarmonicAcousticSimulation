import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from calcAbsorptionCoefficient import cac
import os
path = os.getcwd()
file1 = np.array([a for a in os.listdir(path) if a.endswith('mic1.hist')])
file2 = np.array([b for b in os.listdir(path) if b.endswith('mic2.hist')])
mic1 = file1[0]
mic2 = file2[0]
dfSim = cac(mic1, mic2, 150)
dfSim.to_csv("alphaVsFrequency_FINAL.csv", index=False)
plt.rcParams["figure.figsize"] = (20,8)
fig = plt.figure()
ax = plt.axes()
plt.xlim([377, 3400])
plt.ylim([0, 1])
plt.ylabel("Absorption Coefficient")
plt.xlabel("Frequrency (Hz)")
ax.plot(dfSim["f"], dfSim["alpha"]);
plt.savefig('SimResults.png')
