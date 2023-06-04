# return from Function
def minimum(first, second):
    if first < second:
        return first
    else:
        return second

min = minimum(23, 56)
print(min) # 23

min = minimum(102, 56)
print(min) # 56

min = minimum(45, 56)
print(min) # 45