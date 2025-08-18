import string
word = input()
answer = []
lower = [i for i in string.ascii_lowercase]

for i in lower:
    if i in word:
        answer.append(word.index(i))
    else:
        answer.append(-1)

print(*answer)