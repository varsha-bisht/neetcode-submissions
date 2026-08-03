from typing import List

def contains_duplicate(words: List[str]) -> bool:
    total_length_list = len(words)
    set_str = set(words)
    total_length_set = len(set_str)
    return total_length_list != total_length_set

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
