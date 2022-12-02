import csv, pickle
def load_table(doctype='csv', path='', name=''):
    try:
        if doctype == 'csv':
            result = []
            with open(f'{path}/{name}.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter = ';')
                for row in reader:
                    result.append(row)
            return result
        elif doctype == 'pickle':
            result = []
            with open(f'{path}/{name}.pickle', 'rb') as picklefile:
                while True:
                    try:
                        result.append(pickle.load(picklefile))
                    except EOFError:
                        return result
                        break
        elif doctype == 'txt':
            with open(f'{path}/{name}.txt', 'r') as txtfile:
                result = txtfile.readlines()
            return result
        else:
            print("Вам нужно ввести один из типов документов [csv, txt, pickle]")
    except FileNotFoundError:
        print("Такого файла не существует!\nПроверь свой путь или имя файла!")

def create_table(doctype='csv', path='', name='default', csvdata=[], txtdata='', pickledata = {}):
    if doctype == 'csv':
        with open(f'{path}/{name}.csv', 'w', newline='') as csvfile:
            print(f">>> файл {name}.{doctype} в директории {path} создан")
            writer = csv.writer(csvfile, delimiter=';')
            print(f">>> запись в файл начата")
            nd = []
            for row in csvdata:
                if type(row) is list:
                    writer.writerow(row)
                else:
                    nd.append(row)
                    print(nd)
                    writer.writerow(nd)
                    nd = []
            print(f">>> запись в файл закончена")
    elif doctype == 'txt':
        with open(f'{path}/{name}.txt', 'w') as txtfile:
            print(f">>> файл {name}.{doctype} в директории {path} создан")
            print(f">>> запись в файл начата")
            for row in txtdata:
                txtfile.write(row)
            print(f">>> запись в файл закончена")
    elif doctype == 'pickle':
        with open(f'{path}/{name}.pickle', 'wb') as picklefile:
            print(f">>> файл {name}.{doctype} в директории {path} создан")
            print(f">>> запись в файл начата")
            pickle.dump(pickledata, picklefile, protocol=pickle.HIGHEST_PROTOCOL)
            print(f">>> запись в файл закончена")

def print_table(table):
    for i in table:
        print(i)

def get_rows_by_number(path='', name='',start=0, stop=0, copy_table=False):
    result= load_table('csv', path, name)
    ts = []
    for i,r in enumerate(result):
        if i >= start and i <= stop:
            ts.append(r)
    if copy_table:
        create_table('csv', path, f"{name}_copy", csvdata=ts)
    else:
        return(ts)

def get_rows_by_index(path='',name='',val=[], copy_table=False):
    result= load_table('csv', path, name)
    ts = []
    for row in result:
        for each in val:
            if each in row:
                ts.append(row)
                break
    if copy_table:
        create_table('csv', path, f"{name}_copy", csvdata=ts)
    else:
        return(ts)

def get_column_types(path='', name='', by_number=True):
    result= load_table('csv', path, name)
    ts = {}
    value = []
    k = 0
    for row in result:
        if k == 0:
            for each in row:
                ts.setdefault(each, '')
                value.append(each)
        elif k == 1:
            for ind,each in enumerate(row):
                ts[value[ind]] = str(type(each))
            break
        k+=1
    return(ts)

def get_values(path='', name='', column=0):
    result= load_table('csv', path, name)
    ts = []
    if type(column) is int:
        for row in result:
            try:
                ts.append(row[column])
            except IndexError:
                ts.append(None)
        return ts
    else:
        ind = 0
        if column in result[0]:
            for r,i in enumerate(result[0]):
                if i == column:
                    ind = r
        for row in result:
            try:
                ts.append(row[ind])
            except IndexError:
                ts.append(None)
        return ts

def get_value(path='', name='', column=0):
    try:
        if type(column) is int:
            return load_table('csv', path, name)[0][column]
        else:
            ind = 0
            if column in load_table('csv', path, name)[0]:
                for r,i in enumerate(load_table('csv', path, name)[0]):
                    if i == column:
                        ind = r
            return load_table('csv', path, name)[0][ind]

    except IndexError:
        return None

def set_values(path='', name='', values = [], column=0):
    result= load_table('csv', path, name)
    ts = []
    for ind, row in enumerate(result):
        if ind == 0:
            ts.append(row)
        elif ind > len(values):
            break
        else:
            ts.append(row)
            ts[ind][column] = values[ind-3]
    return ts

def set_value(path='', name='', value='', column=0):
    result= load_table('csv', path, name)
    ts = []
    for ind, row in enumerate(result):
        if ind == 0:
            ts.append(row)
        elif ind > len(value):
            break
        else:
            ts.append(row)
            ts[ind][column] = value
    return ts

create_table(doctype='pickle',path='/Users/nikolaysedoff/PycharmProjects/ITiABD-PM22-7-Nikolay-Sedov/Praktikum/File Manager',name='test',pickledata={})
load_table(doctype='txt',path='/Users/nikolaysedoff/PycharmProjects/ITiABD-PM22-7-Nikolay-Sedov/Praktikum/File Manager',name='test')