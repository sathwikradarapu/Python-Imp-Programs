def get_numbers_from_string(value):
    for char in value:
        if char.isdigit():
            print(char, end='')
value = input()
get_numbers_from_string(value)