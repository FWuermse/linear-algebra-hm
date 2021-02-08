from elimination import gauss
from elimination import gauss_jordan
from matrix_operations import multiply


def main():
    A = build_matrix()
    U, Es = gauss(A)
    E = multiply(multiply(Es[2], Es[1]), Es[0])
    L = gauss_jordan(E)
    assert multiply(E, A) == U
    assert multiply(E, A) != multiply(A, E)
    assert multiply(L, U) == A


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
