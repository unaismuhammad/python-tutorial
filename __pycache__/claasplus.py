

def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary if binary != "" else "0"


decimal_number = 7
print("Decimal number:", decimal_number)
print("Binary of", decimal_number, "is", decimal_to_binary(decimal_number))
