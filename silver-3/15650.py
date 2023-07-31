from sys import stdin

N, M = [int(i) for i in stdin.readline().split()]
def printList(lst):
    print(' '.join([str(s) for s in lst]))

def backtrack(idx, cur):
    if len(cur) == M:
        printList(cur)
        return
    for i in range(idx, N + 1):
        cur.append(i)
        backtrack(i + 1, cur)
        cur.pop()

backtrack(1, [])