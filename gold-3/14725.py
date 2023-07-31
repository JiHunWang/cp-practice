from sys import stdin


class TrieNode:
    def __init__(self, key, isEnd=False):
        self.key = key
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TrieNode(None)
    
    def insert(self, info):
        cur = self.head
        for partial in info:
            if partial not in cur.children:
                cur.children[partial] = TrieNode(partial)
            cur = cur.children[partial]

N = int(input())
trie = Trie()
for _ in range(N):
    info = stdin.readline().split()[1:]
    trie.insert(info)

def dfs(root, indent):
    if not root:
        return
    if root.key:
        print('-' * (indent * 2) + root.key)
    for child in sorted(root.children.keys()):
        dfs(root.children[child], indent + 1)

dfs(trie.head, -1)