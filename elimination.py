from position import Position
import copy


def gauss(A):
    U = copy.deepcopy(list(A))
    m = len(U)  # rows
    n = len(U[0])  # columns
    E = []
    for pivot_index in range(min(m, n) - 1):
        pivot_offset = 1 + pivot_index
        pivot = U[pivot_index][pivot_index]
        for row in range(m - pivot_offset):
            row += pivot_offset  # Increment rows since we're ignoring the first one
            multiplier = U[row][pivot_index] / pivot
            E.append(generateE(n, Position(row, pivot_index), multiplier))
            U[row] = [U[row][column] - multiplier * U[pivot_index][column] for column in range(n)]
    return U, E


def generateE(size, location, value):
    E = generateI(size)
    E[location.row][location.column] = -value
    return E


def generateI(rank):
    I = []
    for index in range(rank):
        I.append([])
        for innerIndex in range(rank):
            value = 1 if index == innerIndex else 0
            I[index].append(value)
    return I


def gauss_jordan(A):
    U = copy.deepcopy(list(A))
    m = len(U)  # rows
    n = len(U[0])  # columns
    max_rank = min(m, n)
    I = generateI(max_rank)
    for pivot_index in range(max_rank):
        pivot = U[pivot_index][pivot_index]
        if pivot != 1:
            U[pivot_index] = [U[pivot_index][column] / pivot for column in range(n)]
            I[pivot_index] = [I[pivot_index][column] / pivot for column in range(n)]
        for row in range(m):
            if row != pivot_index:
                multiplier = U[row][pivot_index] / U[pivot_index][pivot_index]
                U[row] = [U[row][column] - multiplier * U[pivot_index][column] for column in range(n)]
                I[row] = [I[row][column] - multiplier * I[pivot_index][column] for column in range(n)]

    return I


def factorize_D(input_U):
    U = copy.deepcopy(list(input_U))
    m = len(U)  # rows
    n = len(U[0])  # columns
    max_rank = min(m, n)
    I = generateI(max_rank)
    for i in range(max_rank):
        I[i][i] = U[i][i]
    U = [[row[column] / row[i] for column in range(len(row))] for i, row in enumerate(U)]
    return I, U




