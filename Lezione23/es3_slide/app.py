
import numpy as np

def main():
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print(matrix)

    transposed_matrix = matrix.T

    print(transposed_matrix)

    if __name__=="__main__":
        main()