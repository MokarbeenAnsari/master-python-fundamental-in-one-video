# lambdas in Python
def twice(num):
    return 2 * num

twice_lambda = lambda num : 2 * num

print(twice(30))
print(twice_lambda(30))

addition = lambda a, b: a + b
print(addition(40, 50))

high = lambda num : "High" if num > 50 else "Low"
print(high(60))
print(high(30))