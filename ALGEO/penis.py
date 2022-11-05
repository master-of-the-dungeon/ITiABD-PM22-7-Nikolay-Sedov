a11 = 1
ann = 1.04
a1n = 1.22
n = 36000

q = (ann/a11)**(1/n-1)
d = (a1n-a11)/(n-1)

S1 = [a11 * q**i for i in range(n)]

S2 = [S1[i]**-1 for i in range(n)]

S3 = [a11 + d*i for i in range(n)]

S4 = S3[:1] + [S[i]**(-1)/S1[i] for i in range(1,n)]

SS = S2 + S4[1:]
round(min(SS), 3), round(sum(SS),3)