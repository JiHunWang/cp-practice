from sys import stdin

def solve():
    N = int(stdin.readline())
    seq = [0 for _ in range(N)]
    for i in range(N):
        seq[i] = int(stdin.readline())
    
    next = 1
    idx = 0
    stack = []
    answer = ""
    while next <= N:
        if not stack:
            stack.append(next)
            answer += '+'
            next += 1
        elif seq[idx] > stack[-1]:
            stack.append(next)
            answer += '+'
            next += 1
        elif seq[idx] == stack[-1]:
            stack.pop()
            answer += '-'
            idx += 1
        else:
            return "NO"
        # elif seq[idx] 
    
    while stack:
        if stack[-1] == seq[idx]:
            stack.pop()
            answer += '-'
            idx += 1
        else:
            return "NO"
    return answer


if __name__ == '__main__':
    answer = solve()
    if answer == 'NO':
        print('NO')
    else:
        for ch in answer:
            print(ch)