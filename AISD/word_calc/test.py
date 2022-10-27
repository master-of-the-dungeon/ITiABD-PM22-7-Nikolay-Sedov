class StrCalc:
    data_parsing_dict = {
        'ноль': 0,
        'один': 1,
        'два': 2,
        'три': 3,
        'четыре': 4,
        'пять': 5,
        'шесть': 6,
        'семь': 7,
        'восемь': 8,
        "девять": 9,
        "десять": 10,
        'одиннадцать': 11,
        'двенадцать': 12,
        'тринадцать': 13,
        'четырнадцать': 14,
        'пятнадцать': 15,
        'шестнадцать': 16,
        'семнадцать': 17,
        'восемнадцать': 18,
        'девятнадцать': 19,
        'двадцать': 20,
        'тридцать': 30,
        'сорок': 40,
        'пятьдесят': 50,
        'шестьдесят': 60,
        'семьдесят': 70,
        'восемьдесят': 80,
        'девяносто': 90,
        'сто': 100,
        'пилюс':'+',
        'плюс': '+',
        'минус': '-',
        'умножить': '*',
        'делить': '/'}

    def __init__(self, data):
        self._data = data
        self._data_format = self.data_format()
        self._data_parsing_list = self.data_parsing_list()
        self._data_operation = self.get_data_operations()
        self._data_digits = self.data_digits()
        self._data_build = self.data_build()

    @property
    def data(self):
        return self._data.__str__().lower()

    def data_format(self):
        data = self.data.replace(' на ', ' ')
        data = data.split()
        return data

    def data_parsing_list(self):
        data_parsing_list = [self.data_parsing_dict.get(i) for i in self._data_format]
        if None in data_parsing_list:
            raise ValueError('Error, data parsing error')
        return data_parsing_list

    def data_digits(self):
        data_parsing = ','.join(map(str, self._data_parsing_list))
        data_digit = data_parsing.split('{}'.format(self._data_operation))
        data_digit_list = [sum(map(int, [d for d in i.split(',') if d])) for i in [i for i in data_digit if i]]
        data_digit_len = len(data_digit_list)
        if data_digit_len < 2:
            raise ValueError('Error, there are not enough digits to perform the operation')
        if data_digit_len > 2:
            raise ValueError('Error, too many digits to perform the operation')
        return data_digit_list[0], data_digit_list[1]

    def get_data_operations(self):
        operations = [i for i in self._data_parsing_list if isinstance(i, str)]
        if len(operations) > 1:
            raise ValueError('Error, more than one operation')
        if not operations:
            raise ValueError('Error, missing operation')
        return operations[0]

    def data_build(self):
        data_digit_a, data_digit_b = self._data_digits
        return '{} {} {}'.format(data_digit_a, self._data_operation, data_digit_b)

    def result(self):
        return eval(self._data_build)


data = input('Введите выражение: ')
calc = StrCalc(data)
result = calc.result()
print(result)