from sys import stdin
import collections

M, N = [int(i) for i in stdin.readline().split()]
nums = [int(i) for i in stdin.readline().split()]
prefix = collections.deque([0])

for num in nums:
    prefix.append(num + prefix[-1])

for _ in range(N):
    i, j = [int(k) for k in stdin.readline().split()]
    print(prefix[j] - prefix[i-1])