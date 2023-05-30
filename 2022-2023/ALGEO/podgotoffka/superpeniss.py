from sympy import*
from numpy import*
from scipy.linalg import*
from PIL import ImageGrab
from IPython.display import display, Image
def nmmma():
    A = Matrix(
        [[3, 7, -6, -1, 8, -3, -2], [1, -5, 8, -3, -5, 4, -5], [1, 3, -4, 6, -2, 0, 8], [-1, 11, -12, 9, 3, -3, 9],
         [-3, 11, -12, 5, 8, -4, 6], [-3, 2, 1, -4, 4, 1, -7], [1, -5, 6, -2, -4, 3, -2]])
    print(A)
    print(factor(A.charpoly().as_expr()))

def vmlml():
    A = Matrix([[7, -12, 6], [10, -19, 10], [12, -24, 13]])
    C, A1 = A.diagonalize()
    print(C, A1)
    l = Symbol('l')
    D = Matrix([[7 - l, 12, 6], [10, -19 - l, 10], [12, -24, 13 - l]])
    print(D)
    print(solveset(D.det()))
    print('корень 1')
    C1 = Matrix([[6, -12, 6, 0], [10, -20, 10, 0], [12, -24, 12, 0]])
    print(C1)
    print('для корня из-241')
    C2 = Matrix([[7 + root(241, 2), 12, 6, 0], [10, root(241, 2) - 19, 10, 0], [12, -24, 13 + root(241, 2), 0]])
    print(C2)
    print('для корня мз 241')
    C3 = Matrix([[7 - root(241, 2), 12, 6, 0], [10, -root(241, 2) - 19, 10, 0], [12, -24, 13 - root(241, 2), 0]])
    print(C3)

def plovp():
    A = Matrix([[1, -18, 15], [-1, -22, 20], [1, -25, 22]])
    print(A)
    C = Matrix([[1, 3, 2], [-2, -1, 1], [1, 2, 2]])  # матрица перехода от е' к е''
    print(C)
    print(C.inv() * A * C)

def lpzvv():
    x, y = symbols('x y')
    L = Matrix([[x, y, x + y, x - y, 2 * x]]).T
    print(L)
    L1 = Matrix([1, 0, 1, 1, 2]) * x
    print(L1, L1 / x)
    L2=Matrix([1,0,1,1,2])*y
    print(L2,L2/y)
    M = Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, -1, 0, 1, 0], [2, 0, 0, 0, 1]])
    print(M)

def pl1il2():
    L1 = Matrix([[1, 0], [1, 1], [1, 1], [1, 1]])
    print(L1)
    L2 = Matrix([[1, 2, 4, -3], [3, 5, 6, -4]])
    print(L2)
    print(L2.nullspace(), 'решение ФСР однородной системы')
    print('объединяем эти матрицы в одну')
    L = Matrix([[1, 0, 8, -7], [1, 1, -6, 5], [1, 1, 1, 0], [1, 1, 0, 1]])
    print(L, L.rref(), L.rank())
    print(' из базисных миноров располагается на векторах а1,a2,b1, b2.Следовательно,эти вектора могут составить базис суммы пространств L1 и L2. базис L1 и L2:')
    print(L.columnspace(),  'сумма')
    L = Matrix([[3, 0], [4, 1], [-4, -1], [-1, 2]])
    x = Matrix([2, 1, 1, 1])
    L_x = Matrix(hstack([L, x]))
    print(L_x, L_x.rref())
    X = Matrix([[1, 1, 1, 1], [0, 1, 1, 1], [8, -6, 1, 0], [-7, 5, 0, 1], [1, 2, 3, 4]]).T
    print(X.rref())
    print(X.rref()[0][:,4])
    a1 = Matrix([1, 1, 1, 1])
    a2 = Matrix([0, 1, 1, 1])
    b1 = Matrix([8, -6, 1, 0])
    b2 = Matrix([-7, 5, 0, 1])
    print(5 * a1 - 5 * a2 + 3 * b1 + 4 * b2)
    y = 5 * a1 - 5 * a2
    print(y)
    z = 3 * b1 + 4 * b2
    print(z)

