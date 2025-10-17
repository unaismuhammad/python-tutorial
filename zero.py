# try:
#     num =int(input("enter a number"))
#     result = 10/num
# except ZeroDivisionError:
#     print("division by zero is not allowed!")
# else:
#     print(f"the result is{result}")
# finally:
#     print("this will always be printed")



# x = -5
# if x < 0:
#     raise ValueError("negative number are not allowed!")


class NegativeNumberError(Exception):
    pass
def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative number are not allowed!")
    else:
        print(f"result is {num}")        
try:
    check_number(20)
except NegativeNumberError as e:
        print(e)

