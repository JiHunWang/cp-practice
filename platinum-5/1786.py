from sys import stdin

T = input()
P = input()

def getFailure(s):
    pi = [0 for _ in range(len(s))]
    begin, matched = 1, 0
    while begin + matched < len(s):
        if s[begin + matched] == s[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

# T = haystack, P = needle
def KMP(T, P):
    t, p = len(T), len(P)
    pi = getFailure(P)
    answer = []
    begin, matched = 0, 0
    while begin + p <= t:
        if matched < p and T[begin + matched] == P[matched]:
            matched += 1
            if matched == p:
                answer.append(begin + 1)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return answer

answer = KMP(T, P)
print(len(answer))
if len(answer) > 0:
    print(' '.join([str(i) for i in answer]))