import re

def add(numbers_str):
    delimiter = ',|\n'
    if numbers_str.startswith("//"):
        delimiter_part, numbers_str = numbers_str.split("\n")
        delimiter = delimiter_part[2:3]

    lst = re.split(delimiter, numbers_str)
    if not lst:
        return 0
    if len(lst) == 1 and lst[0] == "":
        return 0
    lst[:] = [int(x) for x in lst]
    return sum(lst)



print(add(""))

print(add("1"))


print(add("1,5"))

print(add("1\n2,3"))

print(add("//;\n1;2"))
