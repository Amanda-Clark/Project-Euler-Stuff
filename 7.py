import math

def isprime(n):
    for m in range(2, int(n**0.5)+1):
        if not n%m:
            return False
    return True

target = 10001
start = 2
i = 0
while i < target:
    if isprime(start):
        i +=1
        if i == target:
            print("The 10,001th prime number is " + str(start))
    start += 1

