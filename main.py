from elimination import gauss, gauss_jordan, factorize_D
from matrix_operations import multiply, transpose


def main():
    A = build_matrix()
    U, Es = gauss(A)
    E = multiply(multiply(Es[2], Es[1]), Es[0])
    L = gauss_jordan(E)
    T = transpose(A)
    D, new_U = factorize_D(U)
    assert multiply(E, A) == U
    assert multiply(E, A) != multiply(A, E)
    assert multiply(L, U) == A
    assert multiply(multiply(L, D), new_U) == A
    assert transpose(T) == A


def build_matrix():
    return [
        [1, 3, 1],
        [4, 4, 6],
        [5, 3, 2]]


def print_matrix(matrix, name):
    print(f'Matrix {name}:')
    for row in matrix:
        print(row)


if __name__ == '__main__':
    main()
