def remove_fourth_character(word: str) -> str:
    before_fourth = word[:3]

    after_fourth = word[4:]

    new_message = before_fourth + after_fourth

    return new_message

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
