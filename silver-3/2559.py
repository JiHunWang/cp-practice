from sys import stdin
from collections import deque

N, K = [int(i) for i in stdin.readline().split()]
nums = [int(i) for i in stdin.readline().split()]

prefix = deque([0])
for num in nums:
    prefix.append(prefix[-1] + num)

best = -float('inf')
for i in range(K, len(prefix)):
    best = max(best, prefix[i] - prefix[i-K])

print(best)