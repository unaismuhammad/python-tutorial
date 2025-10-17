x=10 #global function
def outer_function():
    x = 5 #enclosing scope
    def inner_function(): #inner function
        x=6
        print(x) #output 6
    inner_function()
outer_function()
print(x) #output 10

def sum_number(*a)
    total=0
    for number in a:
      total +=number
    return(result)
result sum_number(1,2,4,5,6,7,8,84,4,34)
print(result)