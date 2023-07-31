from sys import stdin

N = int(stdin.readline())
count = [0]

def NQueens(row, cols):

    def check(cols):
        for col in cols[:-1]:
            if col == cols[-1]:
                return False
        idx = len(cols) - 1
        for i, col in enumerate(cols[:-1]):
            if abs(i - idx) == abs(col - cols[-1]):
                return False
        return True

    if row == N:
        count[0] += 1
        return
    for col in range(N):
        cols.append(col)
        if check(cols):
            NQueens(row + 1, cols)
        cols.pop()
    
    
NQueens(0, [])
print(count[0])