def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
            return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

def sum_f(n):
    if n==0:
        return 0
    else:
        return fibonacci(n)+ sum_f(n-1)    
print(sum_f(6))

# 0 1 1 2 3 5 8=20
