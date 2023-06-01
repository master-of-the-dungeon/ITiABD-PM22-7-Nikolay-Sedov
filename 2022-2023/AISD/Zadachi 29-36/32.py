# from typing import List
# def add_two_numbers(l1: List[int], l2: List[int]) -> List[int]:
#     # заполняем списки нулями слева, чтобы обеспечить равную длину
#     while len(l1) < len(l2):
#         l1.insert(0, 0)
#     while len(l2) < len(l1):
#         l2.insert(0, 0)
#
#     # складываем списки справа налево
#     carry = 0
#     result = []
#     for i in range(len(l1) - 1, -1, -1):
#         digit_sum = l1[i] + l2[i] + carry
#         carry, digit = divmod(digit_sum, 10)
#         result.insert(0, digit)
#
#     # если был остаток при сложении последних разрядов, добавляем его в начало
#     if carry > 0:
#         result.insert(0, carry)
#
#     return result
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# result = add_two_numbers(l1, l2)
# print(result)
# l1 = [9, 9, 9, 9]
# l2 = [1]
# result = add_two_numbers(l1, l2)
# print(result)
