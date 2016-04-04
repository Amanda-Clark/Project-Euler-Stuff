# #Problem 2
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

