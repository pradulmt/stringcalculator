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

    negative_numbers = []
    sum_of_numbers = 0
    for num in lst:
        if num < 0:
            negative_numbers.append(str(num))
        sum_of_numbers += num

    if negative_numbers:
         raise ValueError("negative numbers not allowed {}".format(",".join(negative_numbers)))

    return sum_of_numbers
