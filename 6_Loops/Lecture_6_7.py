# The continue statement
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if num == 4 or num == 7:
        continue
    print(num, end=' ')
print()