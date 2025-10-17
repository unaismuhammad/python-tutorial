# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n* factorial(n - 1)
# print(factorial(6)) 


# def factorial(n):
#     a=1
#     for factorial in range(1,n + 1):
#         a=a*factorial
#     return a
# print(factorial(4))

def tail_factorial(n,accumulator=1):
    if n == 0 or n == 1:
        return accumulator
    else:
        return tail_factorial(n -1,accumulator*n)
print(tail_factorial(5))
            
            
             