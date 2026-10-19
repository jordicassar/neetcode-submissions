def print_first_char(word: str) -> None:
    print(word[0])

def print_second_char(word: str) -> None:
    print(word[1])

def print_last_char(word: str) -> None:
    for char in word:
        last_char = len(word) -1
    print(word[last_char])


# do not modify below this line
print_first_char("hello")
print_second_char("hello")
print_last_char("hello")

print_first_char("yay")
print_second_char("yay")
print_last_char("yay")
