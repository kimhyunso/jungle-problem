counter = 0
prime_numbers = []
divide_count = 0

for num in range(2, 1001):
    for i in range(2, num):
        divide_count += 1
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)

print('소수: ', prime_numbers)
print('나눗셈을 실행한 횟수: ', divide_count)


prime_numbers = [None] * 168
prime_numbers[0] = 2
find_prime_number_count = 1
divide_count = 0
count = 0

for num in range(3, 1001, 2):
    for i in range(1, find_prime_number_count):
        divide_count += 1
        if num % prime_numbers[i] == 0:
            break
    else:
        count += 1
        prime_numbers[find_prime_number_count] = num
        find_prime_number_count += 1

print(prime_numbers)
print('나눗셈을 실행한 횟수: ', divide_count)

find_prime_number_count = 2
prime_numbers = [None] * 168
prime_numbers[0] = 2
prime_numbers[1] = 3
divide_count = 0

for n in range(5, 1001, 2):
    i = 1
    while prime_numbers[i] * prime_numbers[i] <= n:
        divide_count += 2
        if n % prime_numbers[i] == 0:
            break
        i += 1
    else:
        prime_numbers[find_prime_number_count] = n
        find_prime_number_count += 1
        divide_count += 1


print(prime_numbers)
print('곱셈과 나눗셈을 실행한 횟수: ', divide_count)
