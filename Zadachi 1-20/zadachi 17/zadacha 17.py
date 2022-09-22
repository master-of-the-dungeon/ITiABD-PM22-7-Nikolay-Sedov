def del_number():
    file = open('sample 1.txt', 'r')
    nums= '1234567890'
    notnumlines = []
    for line in file:
        if nums in line:
            notnumlines.append(line)
    print(notnumlines)
del_number()
