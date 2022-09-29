from math import*

x = float(input('значение x ='))

if x >=2:
	y=2*(x**3)-2*x-1
	print(f'y = {y:.2f}')
elif x<=2:
	y=3*(x**2)-2*x+1
	print(f'y = {y:.2f}')