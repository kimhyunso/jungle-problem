import sys
sys.stdin = open("input.txt", "r") 

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
log_numbers = []
log_numbers.append(numbers[0])




print(len(log_numbers))
    
    


