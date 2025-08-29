def solution(a, b):
    word1 = int(str(a)+str(b))
    word2 = int(str(b)+str(a))
    return max(word1,word2)