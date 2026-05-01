def add_two_numbers() -> int:
    user_input = input()
    str_val_list = user_input.split(",")
    total=0

    for val in str_val_list:
        total+=int(val)

    return total


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
