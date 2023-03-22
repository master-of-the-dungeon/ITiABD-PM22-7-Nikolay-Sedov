def is_divisible_by_digits(n):
    digits = [int(d) for d in str(n) if d != '0']
    return all(n % d == 0 for d in digits)

def find_numbers(start, end):
    return [n for n in range(start, end+1) if is_divisible_by_digits(n)]

numbers = find_numbers(1, 47)
print(numbers)
