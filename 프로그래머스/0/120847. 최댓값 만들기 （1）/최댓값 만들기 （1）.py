def solution(numbers):
    numbers.sort()
    return max([numbers[i] * numbers[i + 1] for i in range(0,len(numbers) - 1)])