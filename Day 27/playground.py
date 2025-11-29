def add(*args):
    total_sum = 0
    for item in args:
        total_sum += item
    return total_sum

print(add(1,2,3,4,5,6,7,8,9))