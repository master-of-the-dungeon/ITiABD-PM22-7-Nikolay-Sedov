import random
def proverka(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return 1
    else:
        return 0

def razlozhenie(n):
    i = 2
    r = []
    while n > 1:
        while n % i == 0:
            r.append(i)
            n //= i
        i += 1
    return r


a = [i+1 for i in range (20)]
b = []
for i in range(len(a)):
    if proverka(a[i]) == 1:
        b.append(a[i])
    else:
        t = razlozhenie(a[i])
        for j in range(len(t)):
            b.append(t[j])
print(a)
print(b)