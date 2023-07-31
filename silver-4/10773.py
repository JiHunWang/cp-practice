from sys import stdin

def solve():
    K = int(stdin.readline())
    stack = []
    for _ in range(K):
        num = int(stdin.readline())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    print(sum(stack))

if __name__ == '__main__':
    solve()