def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    if not binary:
        binary = "0"
    return binary

def binary_to_decimal(binary):
    decimal = 0
    length = len(binary)
    for i in range(length):
        bit = int(binary[length - 1 - i])  # Get bit from right
        decimal += bit * (2 ** i)
    return decimal

def decimal_to_hexadecimal(decimal):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal //= 16
    if not hexadecimal:
        hexadecimal = "0"
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    hex_digits = "0123456789ABCDEF"
    decimal = 0
    length = len(hexadecimal)
    for i in range(length):
        char = hexadecimal[length - 1 - i]  # Get character from right
        value = hex_digits.index(char)
        decimal += value * (16 ** i)
    return decimal

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)  # Convert to decimal
    binary = decimal_to_binary(decimal)  # Convert decimal to binary
    return binary

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)  # Convert to decimal
    hexadecimal = decimal_to_hexadecimal(decimal)  # Convert decimal to hexadecimal
    return hexadecimal

def main():
    print("\nDecimal to Binary (10):")
    print(decimal_to_binary(10))
    
    print("\nBinary to Decimal (1010):")
    print(binary_to_decimal("1010"))
    
    print("\nDecimal to Hexadecimal (255):")
    print(decimal_to_hexadecimal(255))
    
    print("\nHexadecimal to Decimal (FF):")
    print(hexadecimal_to_decimal("FF"))
    
    print("\nHexadecimal to Binary (FF):")
    print(hexadecimal_to_binary("FF"))
    
    print("\nBinary to Hexadecimal (11111111):")
    print(binary_to_hexadecimal("11111111"))

main()