n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

numerator = 0
for i in range(n):
    numerator += (x[i]*w[i])

wmean = numerator/sum(w)
wmean = round(wmean)
print(wmean)
