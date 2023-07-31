from sys import stdin

N = int(stdin.readline())
stack = []
for _ in range(N):
    
    prompt = stdin.readline().split()
    if len(prompt) > 1:
        stack.append(int(prompt[1]))
    else:
        if prompt[0] == 'top':
            if not stack:
                print(-1)
            else:
                print(stack[-1])
        elif prompt[0] == 'size':
            print(len(stack))
        elif prompt[0] == 'empty':
            print(int(len(stack) == 0))
        else:
            if not stack:
                print(-1)
            else:
                print(stack.pop())
