import numpy as np
import matplotlib.pyplot as plt
x = ['Java','Udav','Php','JS','C#','CPP']
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
print(x)
print(y)
fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(17)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure

plt.show()