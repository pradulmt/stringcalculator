# step 1

def add(numbers_str):
    lst = numbers_str.split(',')
    if not lst:
        return 0
    if len(lst) == 1 and lst[0] == "":
        return 0
    lst[:] = [int(x) for x in lst]
    return sum(lst)



print(add(""))

print(add("1"))


print(add("1,5"))
