# The break statement
nums = [12, 56, 6, 7, 8, 19, 17]
n = 13
found = False

for n1 in nums:
    for n2 in nums:
        if n1 + n2 == n:
            found = True
            break

    if found:
        print(n1, n2)
        break