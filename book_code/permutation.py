def permutation(numbers, r):
    numbers.sort()
    used = [0 for _ in range(len(numbers))]

    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return
        
        for i in range(len(numbers)):
            if not used[i]:
                chosen.append(numbers[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    
numbers = [3, 5, 2, 1, 2, 3]
# [1, 2, 3]
# [3, 5, 2]

permutation(numbers, 3)

