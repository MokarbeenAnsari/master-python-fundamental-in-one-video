# Nested if-else
num = 100

if num % 2 == 0:
    print("Number is even.")
    if num < 100:
        print("Given number is also less than 100.")
else:
    print("Number is odd.")
