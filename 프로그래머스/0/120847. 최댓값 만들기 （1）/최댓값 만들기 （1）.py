import numpy as np
def solution(numbers):
    return int(np.prod(sorted(numbers)[-1:-3:-1]))