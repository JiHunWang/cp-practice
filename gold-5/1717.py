from sys import stdin

class UnionFind:
    def __init__(self, n):
        self.uf = [-1 for _ in range(n+1)]
    
    def find(self, i):
        if self.uf[i] < 0:
            return i
        self.uf[i] = self.find(self.uf[i])
        return self.uf[i]

    def get_parent(self, i):
        return self.find(i)
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i != parent_j:
            # -2 < -1, etc.
            if self.uf[parent_i] < self.uf[parent_j]:
                self.uf[parent_i] += self.uf[parent_j]
                self.uf[parent_j] = parent_i
            else:
                self.uf[parent_j] += self.uf[parent_i]
                self.uf[parent_i] = parent_j


n, m = [int(i) for i in stdin.readline().split()]
uf = UnionFind(n)
for _ in range(m):
    op, i, j = [int(i) for i in stdin.readline().split()]
    if op == 0:
        uf.union(i, j)
    else:
        if uf.get_parent(i) != uf.get_parent(j):
            print("NO")
        else:
            print("YES")
