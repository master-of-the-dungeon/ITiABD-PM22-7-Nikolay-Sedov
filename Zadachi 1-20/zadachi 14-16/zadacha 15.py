def invert_str(s, n, k):
    if k > len(s):
        return ""
    return s[n:n+k][::-1]