
#Problem 1
answer = 0
for num in range(1, 1000):
    if num % 5 == 0 or num % 3 == 0:
        answer = num + answer

print(answer)

#Problem 2
fibs = []
def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a
fibs =[]
for c in range(0, 100):
    if fibonacci(c) < 4000000:
        fibs.append(fibonacci(c))
nums = []
for num in fibs:
    if num % 2 ==0:
        nums.append(num)


print(sum(nums))


#Problem 3

import math

num = 600851475143


root = math.sqrt(num)
for i in range(3, int(root)):
    while num % i == 0:
        print(i)
        num = num/i








