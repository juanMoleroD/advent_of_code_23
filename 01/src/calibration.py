numbers = ['one', 'two', 'three', 'four','five','six',
           'seven', 'eight', 'nine']

def return_input(input: str) -> str:
    return input

def get_first_number(input: str) -> str:
    value: int = -1
    lowest_index_number_found = -1
    for index, number in enumerate(numbers):
        search_result: int = input.find(number)
        if  search_result != -1:
            if lowest_index_number_found == -1:
                lowest_index_number_found = search_result
                value = index +1
            if search_result < lowest_index_number_found:
                lowest_index_number_found = search_result
                value = index + 1
    if value == -1: return "-1"
    return str(value)

def get_first_digit(input: str) -> str:
    for index, letter in enumerate(input):
        if letter.isnumeric():
            return letter

def get_last_digit(input: str) -> str:
    for letter in input[::-1]:
        if letter.isnumeric():
            return letter
    return "-1"

def get_last_number(input: str) -> str:
    highest_index_number_found = -1
    value: int = -1
    for index,number in enumerate(numbers):
        search_result = input.rfind(number)
        # print(f'number: {number} - result {search_result} - current Highest {highest_index_number_found}')
        if search_result != -1:
            if highest_index_number_found == -1:
                highest_index_number_found = search_result
                value = index + 1
            if search_result > highest_index_number_found:
                highest_index_number_found = search_result
                value = index + 1
    if value == -1 : return '-1'
    return str(value)    

def get_first(input: str) -> str:
    digit = get_first_digit(input)
    number: int = get_first_number(input)
    digit_position = input.find(digit)
    number_position = input.find(numbers[int(number) -1])
    if digit == "-1" : return number
    if number == "-1" : return digit
    if digit_position < number_position : return digit
    return number

def get_last(input: str) -> str:
    digit = get_last_digit(input)
    number: int = get_last_number(input)
    digit_position = input.rfind(digit)
    number_position = input.rfind(numbers[int(number) -1])
    # print(f'digit {digit} on pos {digit_position}')
    # print(f'number {number} on pos {number_position}')

    if digit == "-1" : return number
    if number == "-1" : return digit
    if digit_position > number_position : return digit
    return number

def get_first_and_last(input):
    first: str = get_first(input)
    last: str = get_last(input)
    return f'{first}{last}'

def read_first_line(file_input) -> str:
    return file_input.readline().strip('\n')

def get_sum(file_input):
    sum: int = 0
    for line in file_input:
        # (print(get_first_and_last(line)))
        sum += int(get_first_and_last(line))
    return sum