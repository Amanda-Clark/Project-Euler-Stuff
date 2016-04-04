#Problem 6
ans1 = 0
for i in range(1, 101):
   ans1 = i*i + ans1
ans2 = sum(range(1, 101))
ans2 = ans2* ans2
ans3 = ans2 - ans1
print(ans3)
