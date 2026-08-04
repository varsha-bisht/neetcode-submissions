def add_two_numbers() -> int:
    usr_input = input()
    usr_list = usr_input.split(",")
    total = 0

    for i in usr_list:
        total += int(i)

    return total


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
