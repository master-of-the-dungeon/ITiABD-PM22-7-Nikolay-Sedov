import time
from termcolor import colored
zxc = 1000
print(colored("Я гуль",'magenta'))
time.sleep(1)
while zxc>=0:
    g = str(zxc)
    zxc-=7
    f = g+'-7'+'='+str(zxc)
    print(colored(f,'magenta'))
    time.sleep(0.05)
