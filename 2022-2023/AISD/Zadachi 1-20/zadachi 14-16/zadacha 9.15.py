def invert_str(s, n, k):
    if k > len(s):
        return ""
    return s[n:n+k][::-1]
s = input()
n = int(input())
k = int(input())
print(invert_str(s,n,k))