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
        'двести':200,
        'триста':300,
        'четыреста':400,
        'пятьсот':500,
        'шестьсот':600,
        'семьсот':700,
        'восемьмот':800,
        'девятьсот':900,
        'тысяча':1000,
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
        if not hasattr(self, '_result'):
            self._result = eval(self._data_build)
        return self._result

    def result_text(self):
        if not hasattr(self, '_result'):
            self._result = self.result()
        data_parsing_dict_revers = dict((v, k) for k, v in self.data_parsing_dict.items())
        result_test = ''
        for i, d in enumerate(self._result.__str__(), -len(self._result.__str__())):
            if abs(i) == 3:
                d_text = data_parsing_dict_revers[int(d) * 100].capitalize()
                result_test += d_text + ' '
            elif abs(i) == 2:
                d_text = data_parsing_dict_revers[int(d) * 10]
                result_test += (d_text if result_test else d_text.capitalize()) + ' '
            else:
                d_text = data_parsing_dict_revers[int(d)]
                result_test += (d_text if result_test else d_text.capitalize())
        return result_test


data = input('Введите выражение: ')
try:
    calc = StrCalc(data)
    result = calc.result()
    result_text = calc.result_text()
    print(result, '(%s)' % result_text)
except Exception as e:
    print(e)
