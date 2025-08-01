import sys
sys.stdin = open("input.txt", "r")

words = input()
parts = words.split('-')
total = sum(map(int, parts[0].split('+')))

for part in parts[1:]:
    total -= sum(map(int, part.split('+')))

print(total)