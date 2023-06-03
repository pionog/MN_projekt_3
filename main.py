import csv
import numpy as np
import matplotlib.pyplot as plt

import LaGrange

path = "dane/MountEverest.csv"
f = open(path, "r")  # uchwyt do pliku
data = list(csv.reader(f, delimiter=","))
f.close()
dataArray = np.array(data)
xData = np.array(dataArray[:, 0]).astype(np.float64)
yData = np.array(dataArray[:, 1]).astype(np.float64)

fig, ax = plt.subplots()
ax.plot(xData, yData)
ax.set_title("Aproksymacja profilu wysokościowego")
ax.set_xlabel("Odległość")
ax.set_ylabel("Wysokość")
plt.show()

yLaGrange = []
xLaGrange = []

wysokosc = np.array(yData[::64])
dlugosc = np.array(xData[::64])
i = 0
while i < 512:
    yLaGrange.append(LaGrange.lagrange(xData[i], dlugosc, wysokosc))
    xLaGrange.append(xData[i])
    i += 64


fig, ax = plt.subplots()
ax.plot(xLaGrange, yLaGrange)
ax.set_title("Aproksymacja profilu wysokościowego")
ax.set_xlabel("Odległość")
ax.set_ylabel("Wysokość")
plt.show()
