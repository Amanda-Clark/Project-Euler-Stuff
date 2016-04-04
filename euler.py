# #
# # #Problem 1
# answer = 0
# for num in range(1, 1000):
#     if num % 5 == 0 or num % 3 == 0:
#         answer = num + answer
#
# print(answer)
#
# # #Problem 2
# fibs = []
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(0, n):
#         temp = a
#         a = b
#         b = temp + b
#     return a
# fibs =[]
# for c in range(0, 100):
#     if fibonacci(c) < 4000000:
#         fibs.append(fibonacci(c))
# nums = []
# for num in fibs:
#     if num % 2 ==0:
#         nums.append(num)
#
#
# print(sum(nums))
#
#
# # #Problem 3
#
# import math
#
# num = 600851475143
#
#
# root = math.sqrt(num)
# for i in range(3, int(root)):
#     while num % i == 0:
#         print(i)
# #         num = num/i
#
#
# #Problem 4
# ans = 0
# for i in range(100, 999):
#     for j in range(100, 999):
#         prod = i * j
#         if str(prod)== str(prod)[::-1]:
#             if prod > ans:
#                 ans = prod
#                 print(ans)
#
# #Problem 5
#
# from functools import reduce
#
# def gcd(a, b):
#     """Return greatest common divisor using Euclid's Algorithm."""
#     while b:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     """Return lowest common multiple."""
#     return a * b // gcd(a, b)
#
# def lcmm(*args):
#     """Return lcm of args."""
#     return reduce(lcm, args)
#
# ans = lcmm(*range(1,21))
# print(ans)
#
# #Problem 6
# ans1 = 0
# for i in range(1, 101):
#    ans1 = i*i + ans1
# ans2 = sum(range(1, 101))
# ans2 = ans2* ans2
# ans3 = ans2 - ans1
# print(ans3)

#Problem 7

import math

# def isprime(n):
#     for m in range(2, int(n**0.5)+1):
#         if not n%m:
#             return False
#     return True
#
# target = 10001
# start = 2
# i = 0
# while i < target:
#     if isprime(start):
#         i +=1
#         if i == target:
#             print("The 10,001th prime number is "+ str(start))
#     start += 1

