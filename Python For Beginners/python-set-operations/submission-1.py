from typing import List

def count_unique_words(words: List[str]) -> int:
    # create a set
    unique_words = set()
    # iterate through words
    for word in words:
        # add word into set
        unique_words.add(word)
    # return length of set 
    return len(unique_words)
    
# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))