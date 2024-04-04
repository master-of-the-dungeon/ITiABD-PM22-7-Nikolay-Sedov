class Arr(object):
    def __init__(self, num=0, array=None):
        if array is None:
            array = []
        self.__num = num
        self.__array = array
    
    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self, n):
        self.__num = n
    
    @property
    def array(self):
        return self.__array
    
    @array.setter
    def array(self, s):
        if isinstance(s, list):
            self.__array = s
            self.__num = len(s)
    
    def find_min(self):
        return min(self.__array)
    
    def find_max(self):
        return max(self.__array)
    
    def sort(self):
        self.__array = sorted(self.__array)
    
    def summa(self):
        return sum(self.__array)
    
    def add(self, a):
        self.__array.append(a)
        self.__num += 1
    
    def mul(self, b):
        self.__array = [x * b for x in self.__array]
    
   
    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.add(other)
        return self
    
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.mul(other)
        return self


arr = Arr(3, [1, 2, 3])
print(arr.array)  

arr + 4  
print(arr.array)  

arr * 2  
print(arr.array)  
