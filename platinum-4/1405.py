N = input()
s = input()

def getFailure(s):
    pi = [0 for _ in range(len(s))]
    begin, matched = 1, 0
    while begin + matched < len(s):
        if matched < len(s) and s[begin + matched] == s[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

failure = getFailure(s)
print(len(s) - failure[-1])