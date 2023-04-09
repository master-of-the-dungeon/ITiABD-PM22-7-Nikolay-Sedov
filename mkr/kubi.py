def even_result(func):
    def wrapper(*args):
        result = func(*args)
        if result % 2 == 0:
            print("Результат четный")
        return result
    return wrapper


@even_result
def sum_of_squares(lst):
    return sum(map(lambda x: x**2, lst))


@even_result
def sum_of_cubes(lst):
    return sum(map(lambda x: x**3, lst))


# вызываем функции
print(sum_of_squares([1, 2, 3, 4, 5])) # выводится "Результат четный" и 55
print(sum_of_cubes([1, 2, 3, 4, 5])) # выводится 225
