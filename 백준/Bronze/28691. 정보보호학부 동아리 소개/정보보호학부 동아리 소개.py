import sys

input = sys.stdin.readline

word_list = {'M' : 'MatKor', 
             'W' : 'WiCys',
             'C' : 'CyKor',
             'A' : 'AlKor', 
             '$' : '$clear'}

print(word_list[input().strip()])