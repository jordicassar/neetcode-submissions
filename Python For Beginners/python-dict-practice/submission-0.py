from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    # Dict initialization
    dict = {}
    # Enter the loop
    for char in word:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
