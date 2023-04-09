find_a_in_middle = lambda words: list(filter(lambda word: len(word) % 2 == 1 and 'a' in word[len(word)//2], words))
words = ["banana", "apple", "avocado", "grape", "pear","cac","treaert"]
result = find_a_in_middle(words)
print('Результат работы первой функции: ',result)
find_power_of_two = lambda numbers: list(filter(lambda number: number > 0 and (number & (number - 1)) == 0, numbers))
numbers = [2, 4, 6, 8, 10, 16, 32, 64, 128, 1030, 100500]
result = find_power_of_two(numbers)
print('Результат работы второй функции: ',result)