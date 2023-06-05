import numpy as np

def spline(xData, yData, distance, indicies_intervals):  # distance - indicies_intervals - steps between two indicies
    how_many = round(xData.shape[0] / indicies_intervals) + 1  # how_many - number of interpolated points
    n = 4 * (how_many - 1)  # n - number of equations
    matrix = np.zeros((n, n))
    result_matrix = np.zeros((n, 1))

    x_interpolated = np.array(xData[::indicies_intervals])
    y_interpolated = np.array(yData[::indicies_intervals])

    # S0(x0) = f(x0)
    matrix[0][0] = 1
    result_matrix[0][0] = y_interpolated[0]

    # S0(x1) = f(x1)
    h = x_interpolated[1] - x_interpolated[0]
    matrix[1][0] = 1
    matrix[1][1] = h
    matrix[1][2] = pow(h, 2)
    matrix[1][3] = pow(h, 3)
    result_matrix[1][0] = y_interpolated[1]

    # S''0(x0) = 0  -->  [c0 * 1] = 0
    matrix[2][2] = 1
    result_matrix[2][0] = 0

    # S''n-1(xn) = 0  -->  [cn-1 * 2] + [dn-1 * 6 * h] = 0
    h = x_interpolated[how_many - 1] - x_interpolated[how_many - 2]
    matrix[3][4 * (how_many - 2) + 2] = 2
    matrix[3][4 * (how_many - 2) + 3] = 6 * h
    result_matrix[3] = 0

    for i in range(1, how_many-1):
        h = x_interpolated[i] - x_interpolated[i - 1]
        # Si(xi) = f(xi)  -->  [ai * 1] = f(xi)
        matrix[4 * i][4 * i] = 1
        result_matrix[4 * i][0] = y_interpolated[i]

        # Si(xi+1) = f(xi+1)
        matrix[4 * i + 1][4 * i] = 1
        matrix[4 * i + 1][4 * i + 1] = h
        matrix[4 * i + 1][4 * i + 2] = pow(h, 2)
        matrix[4 * i + 1][4 * i + 3] = pow(h, 3)
        result_matrix[4 * i + 1][0] = y_interpolated[i + 1]

        # S'i-1(xi) = [bi-1 * 1] + [ci-1 * 2 * h] + [di-1 * 3 * h^2] + [bi * (-1)] = 0
        matrix[4 * i + 2][4 * (i - 1) + 1] = 1
        matrix[4 * i + 2][4 * (i - 1) + 2] = 2 * h
        matrix[4 * i + 2][4 * (i - 1) + 3] = 3 * pow(h, 2)
        matrix[4 * i + 2][4 * i + 1] = -1
        result_matrix[4 * i + 2][0] = 0

        # S''i-1(xi) = [ci-1 * 2] + [di-1 * 6 * h] + [ci * (-2)] = 0
        matrix[4 * i + 3][4 * (i - 1) + 2] = 2
        matrix[4 * i + 3][4 * (i - 1) + 3] = 6 * h
        matrix[4 * i + 3][4 * i + 2] = -2
        result_matrix[4 * i + 3][0] = 0

    inverted_matrix = np.linalg.inv(matrix)

    wanted_matrix = np.matmul(inverted_matrix, result_matrix)


    for i in range(how_many-1):
        elevation = 0.0
        if distance >= x_interpolated[i] and distance <= x_interpolated[i+1]:
            for j in range(4):
                h = distance - x_interpolated[i]
                elevation += wanted_matrix[4 * i + j] * pow(h, j)
            break

    return elevation
