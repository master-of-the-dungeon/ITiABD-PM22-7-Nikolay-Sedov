import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__} execution time: {execution_time:.6f} seconds")
        return result
    return wrapper


def insertion_sort(words, ascending=True):
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        if ascending:
            while j >= 0 and words[j] > key:
                words[j+1] = words[j]
                j -= 1
        else:
            while j >= 0 and words[j] < key:
                words[j+1] = words[j]
                j -= 1
        words[j+1] = key
    return words


def selection_sort(words, ascending=True):
    for i in range(len(words)):
        if ascending:
            min_index = i
            for j in range(i+1, len(words)):
                if words[j] < words[min_index]:
                    min_index = j
            words[i], words[min_index] = words[min_index], words[i]
        else:
            max_index = i
            for j in range(i+1, len(words)):
                if words[j] > words[max_index]:
                    max_index = j
            words[i], words[max_index] = words[max_index], words[i]
    return words


def quicksort(words, ascending=True):
    if len(words) <= 1:
        return words
    pivot = words[0]
    left = []
    right = []
    for word in words[1:]:
        if (ascending and word < pivot) or (not ascending and word > pivot):
            left.append(word)
        else:
            right.append(word)
    return quicksort(left, ascending) + [pivot] + quicksort(right, ascending)


@measure_time
def sort_words(filename, ascending=True, algorithm='insertion'):
    with open(filename) as file:
        words = file.read().split()

    if algorithm == 'insertion':
        words = insertion_sort(words, ascending)
    elif algorithm == 'selection':
        words = selection_sort(words, ascending)
    elif algorithm == 'quicksort':
        words = quicksort(words, ascending)
    else:
        raise ValueError(f"Invalid sorting algorithm: {algorithm}")

    print("\nSorted words:")
    for word in words:
        print(word)


sort_words('example.txt', ascending=False, algorithm='quicksort')
