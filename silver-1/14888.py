from sys import stdin

N = int(stdin.readline())
nums = [int(i) for i in stdin.readline().split()]
maxmin = [-float('inf'), float('inf')]

def backtrack(lst, ops):
    
    if len(lst) == 1:
        if lst[0] > maxmin[0]:
            maxmin[0] = lst[0]
        if lst[0] < maxmin[1]:
            maxmin[1] = lst[0]
        return
    for op in ops.keys():
        if ops[op] > 0:
            ops[op] -= 1
            first_val = eval(str(lst[0]) + op + str(lst[1]))
            new_lst = [int(first_val)]
            new_lst.extend(lst[2:])
            backtrack(new_lst, ops)
            ops[op] += 1

t = [int(i) for i in stdin.readline().split()]
ops = {}
ops['+'] = t[0]
ops['-'] = t[1]
ops['*'] = t[2]
ops['/'] = t[3]
backtrack(nums, ops)
print(maxmin[0])
print(maxmin[1])