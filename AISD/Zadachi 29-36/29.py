def remove_negative_elements(stack):
    output = []
    for element in reversed(stack):
        if element >= 0:
            output.append(element)
    return list(reversed(output))


def test_remove_negative_elements():

    input_stack = [1, -2, 3, -4, 5]
    expected_output = [1, 3, 5]
    assert remove_negative_elements(input_stack) == expected_output
    print(expected_output)
    input_stack = [10, -20, 30, -40, 50, -60, 70, -80]
    expected_output = [10, 30, 50, 70]
    assert remove_negative_elements(input_stack) == expected_output
    print(expected_output)
    input_stack = [-1, -2, -3, -4]
    expected_output = []
    assert remove_negative_elements(input_stack) == expected_output
    print(expected_output)
    input_stack = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert remove_negative_elements(input_stack) == expected_output
    print(expected_output)
    input_stack = []
    expected_output = []
    assert remove_negative_elements(input_stack) == expected_output
    print(expected_output)
test_remove_negative_elements()