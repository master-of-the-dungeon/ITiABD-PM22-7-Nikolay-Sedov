def SIMM(str):
    if len(str) % 2:
        return False
    if str[0] != str[-1]:
        return False
    if len(str) == 2:
        return True
    str = str[1:-1]
    return SIMM(str)


strings = ['1234554321', 'asdfghgfdsa', 'asdfghhgfdsa', 'qwertyasdfghj', '123asddsa321']
for s in strings:
    if SIMM(s):
        print(f'Строка "{s}" симметричная')
    else:
        print(f'Строка "{s}" НЕ симметричная')