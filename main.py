import csv
import numpy as np
import matplotlib.pyplot as plt

import LaGrange
import Spline

SAMPLES = 480

path = "dane/MountEverest.csv"
f = open(path, "r")  # uchwyt do pliku
data = list(csv.reader(f, delimiter=","))
f.close()
dataArray = np.array(data)
xData = np.array(dataArray[:SAMPLES+1, 0]).astype(np.float64)
yData = np.array(dataArray[:SAMPLES+1, 1]).astype(np.float64)

fig, ax = plt.subplots()
ax.plot(xData, yData)
ax.set_title("Aproksymacja profilu wysokościowego")
ax.set_xlabel("Odległość")
ax.set_ylabel("Wysokość")
plt.show()

yLaGrange = []
xLaGrange = []

ile = 32

wysokosc = np.array(yData[::ile])
dlugosc = np.array(xData[::ile])

odleglosc = xData[SAMPLES-1]
i = 0
while i <= odleglosc:
    yLaGrange.append(LaGrange.lagrange(i, dlugosc, wysokosc))
    xLaGrange.append(i)
    i += 8

fig, ax = plt.subplots()
ax.plot(xData, yData)
ax.plot(xLaGrange, yLaGrange)
ax.set_title("Interpolacja LaGrange'a")
ax.set_xlabel("Odległość")
ax.set_ylabel("Wysokość")
plt.show()

sklejanePunkty = []
krok = 8
indeks = 0
ileKrokow = round(odleglosc/krok)
for i in range(ileKrokow):
    sklejanePunkty.append(Spline.spline(xData, yData, i * krok, 32))

x = np.arange(0, ileKrokow * krok, krok)
y = np.array(sklejanePunkty).astype(np.float64)
fig, ax = plt.subplots()
ax.plot(xData, yData)
ax.plot(x, y)
ax.set_title("Interpolacja funkcjami sklejanymi")
ax.set_xlabel("Dystans")
ax.set_ylabel("Wysokość")
plt.show()


