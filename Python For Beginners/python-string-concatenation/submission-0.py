def concatenate(s1: str, s2: str) -> str:
    if len(s1 + s2) > 10:
        return "Too long!"
    else:
        return s1+s2



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
