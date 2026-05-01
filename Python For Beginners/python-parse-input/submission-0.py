from typing import List

def read_integers() -> List[int]:
    val = input()
    val_list = val.split(",")
    new_list=[]
    for val in val_list:
        new_list.append(int(val))
    return new_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
