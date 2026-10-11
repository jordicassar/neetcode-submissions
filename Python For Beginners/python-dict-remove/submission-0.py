from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for key in keys:
        if key in my_dict:
            my_dict.pop(key)
    return my_dict
    

# do not modify below this line
# Should remove keys a and c and return key b
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
# Throws a KeyError Exception
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"])) 
