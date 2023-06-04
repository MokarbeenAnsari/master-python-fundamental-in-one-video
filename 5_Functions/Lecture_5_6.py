# Function scope & Lifetime
def fun():
    name ='Mokarbeen'
    print(name)
    return name

name_ = fun()
print(name_)