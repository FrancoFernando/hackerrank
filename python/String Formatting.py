# with fstrings
def print_formatted(number):
    width = len(f"{number:b}")
    for num in range(1,number+1):
        binary = f"{num:b}".rjust(width,' ')
        octal = f"{num:o}".rjust(width,' ')
        hexadecimal = f"{num:X}".rjust(width,' ')
        decimal = str(num).rjust(width,' ')
        print(decimal,octal,hexadecimal,binary)
'''
def print_formatted(number):
    width = len(f"{number:b}")
    for num in range(1,number+1):
        binary = bin(num)[2:].rjust(width,' ')
        octal = oct(num)[2:].rjust(width,' ')
        hexadecimal = hex(num)[2:].upper().rjust(width,' ')
        decimal = str(num).rjust(width,' ')
        print(decimal,octal,hexadecimal,binary)
 '''       
        
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
