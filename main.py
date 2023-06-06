import csv
import numpy as np
import matplotlib.pyplot as plt
import time

import LaGrange
import Spline

SAMPLES = 480  # limitation of samples taken from the file (default they have 512 samples)
DENSITIES = [16, 32, 48, 80]  # list of possible densities
DIVISION_DENSITY = DENSITIES[0]  # this variable means that for every x where 32*x there is an interpolated point
HOW_MANY_POINTS = round(SAMPLES / DIVISION_DENSITY) + 1  # counter of interpolated points
STEP = 8  # how much space is needed between each point when calculating interpolated values
FILE_NAME = "GlebiaChallengera"

################################
# reading file and setting variables to further work

path = "dane/" + FILE_NAME + ".csv"
f = open(path, "r")  # handle to the file
data = list(csv.reader(f, delimiter=","))  # open csv file
f.close()  # close file stream
dataArray = np.array(data)  # create array from the file data
xData = np.array(dataArray[:SAMPLES+1, 0]).astype(np.float64)  # an array containing x values from csv file
yData = np.array(dataArray[:SAMPLES+1, 1]).astype(np.float64)  # an array containing y values from csv file
TOTAL_DISTANCE = xData[SAMPLES - 1]  # distance from the start point to the end point

################################

################################
# plotting a chart for a given file

fig, ax = plt.subplots()
ax.plot(xData, yData)
ax.set_title("Aproksymacja profilu wysokościowego")
ax.set_xlabel("Odległość [m]")
ax.set_ylabel("Wysokość [m]")
plt.show()

################################

################################
# Lagrange interpolation
start = time.time()  # measuring time for computing interpolation

yLagrange = []  # making an empty list for y values
xLagrange = []  # making an empty list for x values
height_interpolated = np.array(yData[::DIVISION_DENSITY])  # making an array containing interpolated points for height (x)
distance_interpolated = np.array(xData[::DIVISION_DENSITY])  # making an array containing interpolated points for distance (y)

i = 0
while i <= TOTAL_DISTANCE:
    yLagrange.append(LaGrange.lagrange(i, distance_interpolated, height_interpolated))  # calculating y(x)
    xLagrange.append(i)  # appending current step
    i += STEP  # increasing i by a step

end = time.time()
diff = end - start
print("Czas trwania interpolacji Lagrange'a: {:10.4f} sekund".format(diff))
fig, ax = plt.subplots()
ax.plot(xData, yData, color='b', label="Oryginalne dane")
ax.plot(xLagrange, yLagrange, color='orange', label="Wartości interpolowane")
ax.scatter(distance_interpolated, height_interpolated, label='Interpolowane punkty', color='red')
ax.legend()
ax.set_title(f"Interpolacja Lagrange'a {FILE_NAME} dla {HOW_MANY_POINTS} punktów")
ax.set_xlabel("Odległość [m]")
ax.set_ylabel("Wysokość [m]")
plt.show()

################################

################################
# Spline interpolation

start = time.time()

spline_points = []  # making an empty list
how_many_steps = round(TOTAL_DISTANCE / STEP)
for i in range(how_many_steps):
    spline_points.append(Spline.spline(xData, yData, i * STEP, DIVISION_DENSITY))  # y(x)

end = time.time()
diff = end - start
print("Czas trwania interpolacji funkcjami sklejanymi: {:10.4f} sekund".format(diff))

x = np.arange(0, how_many_steps * STEP, STEP)
y = np.array(spline_points).astype(np.float64)
fig, ax = plt.subplots()
ax.plot(xData, yData, color='b', label="Oryginalne dane")
ax.plot(x, y, color='orange', label="Wartości interpolowane")
ax.scatter(distance_interpolated, height_interpolated, label='Interpolowane punkty', color='red')
ax.legend()
ax.set_title(f"Interpolacja funkcjami sklejanymi {FILE_NAME} dla {HOW_MANY_POINTS} punktów")
ax.set_xlabel("Odległość [m]")
ax.set_ylabel("Wysokość [m]")
plt.show()

################################
