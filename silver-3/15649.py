from sys import stdin

N, M = [int(i) for i in stdin.readline().split()]
def printList(lst):
    print(' '.join([str(s) for s in lst]))

def backtrack(lst, cur):
    if len(cur) == M:
        printList(cur)
        return
    for i in range(len(lst)):
        cur.append(lst[i])
        backtrack(lst[:i] + lst[i+1:], cur)
        cur.pop()

backtrack([i for i in range(1, N+1)], [])