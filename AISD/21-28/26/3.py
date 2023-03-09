def remove_common_elements(list1, list2):
    for element in list2:
        if element in list1:
            list1.remove(element)
    return list1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,123,1232353245,123,35734953]
list2 = [2, 4, 6, 8,10,123]
result = remove_common_elements(list1, list2)
print(result)
