from typing import List

def read_integers() -> List[int]:
    user_input = input()
    user_list = user_input.split(",")

    final_list = []
    for num in user_list:
        final_list.append(int(num))
    return final_list

    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
