def add_two_numbers() -> int:
    num_str = input()
    new_str = num_str.split(",")
    int_list = []
    total = 0

    for val in new_str:
        int_list.append(int(val))

    for val in int_list:
        total+=val

    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
