import numpy as np
from scipy import stats

n = int(input())
x = list(map(int, input().split()))
mean = np.mean(x)
median = np.median(x)
mode = int(stats.mode(x)[0])
print(mean)
print(median)
print(mode)
