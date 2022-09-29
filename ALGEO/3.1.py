import sympy as sp
M_1 = sp.Matrix(4,3,[
    3,0,2,
    0,1,3,
    2,2,0,
    0,1,0
])
M_2 = sp.Matrix(3,4,[
    1,2,-1,2,
    -2,-2,1,2,
    2,1,1,2
])
Res1 = M_1*M_2
M_3 = sp.Matrix(4,4,[
    0,-4,6,1,
    2,2,-5,-2,
    2,-2,6,4,
    1,3,0,1
])
Res2 = Res1+M_3
print(M_2)
print(Res2)