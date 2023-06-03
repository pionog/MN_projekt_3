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
