import numpy as np


# def lagrange(data, x, index):
#     wynik = 1
#     i = 0
#     while i < 512:
#         wynik *= iloczyn(x, index, i)
#         i += 64
#     # wynik - fi_index(x)
#     return wynik*data[index]


def lagrange(x, xData, yData):
    n = len(xData)
    result = 0.0

    for i in range(n):
        term = yData[i]
        for j in range(n):
            if j != i:
                term *= (x - xData[j]) / (xData[i] - xData[j])
        result += term

    return result

# y - rozpatrywany y, index - index x, number - numer iteracji
# def iloczyn(x, index, number):
#     if index == number:
#         return 1
#     else:
#         licznik = x - number
#         mianownik = index - number
#         return licznik/mianownik