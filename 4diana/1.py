def merger(a, b):
    new_list = []
    d = a + b
    while d:
        delete_num = min(d)
        while delete_num in d:
            new_list.append(delete_num)
            d.remove(delete_num)
    return new_list


list_a = [3, 45, 50]
list_b = [44, 43, 44]
list_c = merger(list_a, list_b)
print(list_c)