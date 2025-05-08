import itertools
def solution(number):
    count = 0
    combi = list(itertools.combinations(number,3))
    for character in combi:
        if sum(character) == 0:
            count += 1
    return count
