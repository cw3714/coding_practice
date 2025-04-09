import numpy as np
def solution(arr1, arr2):
    matrix1 = np.array(arr1)
    matrix2 = np.array(arr2)
    return (matrix1 + matrix2).tolist()