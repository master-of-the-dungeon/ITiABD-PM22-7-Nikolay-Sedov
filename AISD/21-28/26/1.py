import re
is_number = lambda x: bool(re.match(r'^[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$', x))
print(is_number('test123test'))
print(is_number('1235'))
print(is_number('-1.23'))
print(is_number('3.14e-2'))
print(is_number('abc123'))