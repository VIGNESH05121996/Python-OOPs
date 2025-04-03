def harmonicNumber(n):
     return sum(1 / k for k in range(1, n + 1))

n = 15
print(harmonicNumber(n)) 