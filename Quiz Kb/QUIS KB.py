A = [[2, 0, -3], [1, 4, 5]]
B = [[3, 1], [-1, 0], [4, 2]]
C = [[4, 7], [2, 1], [-1, -1]]


def multiply_matrices(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def add_matrices(X, Y):
    result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    return result


AB = multiply_matrices(A, B)
AC = multiply_matrices(A, C)


result = add_matrices(AB, AC)

print("AB:")
for row in AB:
    print(row)

print("AC:")
for row in AC:
    print(row)

print("AB + AC:")
for row in result:
    print(row)