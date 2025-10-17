def highorder(a,b,subs):
    return subs(a,b)

def plus(a,b):
    return a+b

def multiply(a,b):
    return a*b

def substraction(a,b):
    return a-b

def division(a,b):
    return a/b

print(highorder(4,5,plus))
print(highorder(6,4,multiply))
print(highorder(150,10,division))
print(highorder(14,5,substraction))
