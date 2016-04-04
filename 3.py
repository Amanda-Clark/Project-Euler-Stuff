# #Problem 3

import math

num = 600851475143


root = math.sqrt(num)
for i in range(3, int(root)):
    while num % i == 0:
        print(i)
        num = num/i


