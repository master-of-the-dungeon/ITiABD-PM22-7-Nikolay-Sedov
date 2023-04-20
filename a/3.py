class MyObject:
    def __init__(self, int_val, str_val, float_val):
        self.int_val = int_val
        self.str_val = str_val
        self.float_val = float_val

    def __int__(self):
        return self.int_val

    def __str__(self):
        return self.str_val

    def __float__(self):
        return self.float_val

my_obj = MyObject(10, "Hello, World!", 3.14)

int_val = int(my_obj)
print(int_val)  # выведет: 10

str_val = str(my_obj)
print(str_val)  # выведет: Hello, World!

float_val = float(my_obj)
print(float_val)  # выведет: 3.14
