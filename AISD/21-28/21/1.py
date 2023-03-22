import matplotlib.pyplot
import math
from prettytable import PrettyTable
import numpy as np
x = np.arange(-10, 10.01, 0.01)
# n = int(input('Введите N: '))
a = int(input('Введите a: '))
b = int(input('Введите b: '))
iksi = []
igreki = []
mytable = PrettyTable()
for x in range(a,b+1):
    y = math.fabs((x)/((x**2)-1))
    iksi.append(x)
    igreki.append(y)
mytable.add_column("Значение X",iksi)
mytable.add_column("Значение Y",igreki)
print(mytable)
matplotlib.pyplot.plot(iksi,igreki)
matplotlib.pyplot.show()