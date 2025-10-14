import sys

input = sys.stdin.readline


word = "WelcomeToSMUPC"

print(word[int(input()) % 14 - 1])