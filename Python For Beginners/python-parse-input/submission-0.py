from typing import List

def read_integers() -> List[int]:
    user_text = input().split(",")
    return [int(x) for x in user_text]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
