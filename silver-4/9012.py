from sys import stdin

def check(s):
    stack = []
    for ch in s.strip():
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            else:
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
    return len(stack) == 0

T = int(stdin.readline())
for _ in range(T):
    s = stdin.readline()
    if check(s):
        print('YES')
    else:
        print('NO')