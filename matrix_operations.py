def multiply(A, B):
    return [[sum(row * column for row, column in zip(row_A, column_B))
                                for column_B in zip(*B)]
                                    for row_A in A]
