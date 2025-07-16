'''
1. primtive expressions
2. means of combination (덧셈, 곰셈...)
3. mean of abstraction (추상화): 네이밍 -> 함수 
How를 숨기고 what을 사용, 복잡한 형태를 하나의 단어로 사용
[data abstraction]
'''

'''
f(a) = (a + 1)^2 + (2a)^2
'''

def f(a):
    return sum_of_square(a + 1, a *2)

def sum_of_square(x, y):
    return square(x) + square(y)

def square(x):
    return x * x

# # application order evaluation, nornal order evaluation

# def p():
#     while True:
#         pass

# def test(x, y):
#     return 0 if x == 0 else y

# test(0, p())




def nsum(n):
    # return (n * n + n) // 2
    return sum(i for i in range(1, n + 1))

a = nsum(10)

def recur_sum(n):
    if n <= 1:
        return 1
    return n + recur_sum(n - 1)

test = recur_sum(10)


# Tail Recursion

def sum_iter(n, total):
    if n == 0:
        return total
    return sum_iter(n - 1, total + n)

def sum(n):
    return sum_iter(n, 0)



def exp(b, n):
    if n < 0:
        return 1
    return n * exp(b, n-1)


def exp_iter(b, counter, product):
    if counter == 0:
        return product
    return exp_iter(b, counter - 1, b * product)

def exp_i(b, n):
    product = 1
    for i in range(n, 1):
        product *= n
    return product

def test(b, n):
    if n < 0:
        return 1
    
    if n % 2 == 0:
        return square(test(b, n // 2))
    else:
        return b * test(b, n - 1)
    


def count_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    
    return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)


coins = [1, 2, 3]
result = count_change(4, coins)

print(result)
