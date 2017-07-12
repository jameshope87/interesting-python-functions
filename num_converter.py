#hex converter

def dec_to_hex(number):
    return hex(number)

def dec_to_bin(number):
    return bin(number)

def hex_to_dec(number):
    return int(number, 16)

def bin_to_dec(number):
    return int(number, 2)

    
if __name__ == "__main__":
    while True:
        print("Welcome to number converter, please enter your choice from the list below:")
        print('''1. Decimal to Binary\n
2. Decimal to Hexidecimal\n
3. Binary to Decimal\n
4. Hexidecimal to Decimal''')
        choice = input('>>')
        while choice not in ['1', '2', '3', '4']:
            print("please select a number from 1 to 4")
            choice = input('>>')
        print("Right, now please enter your number")
        number = input('>>')
        if choice == '1':
            print(bin(int(number)))  
        elif choice == '2':
            print(hex(int(number)))
        elif choice == '3':
            print(int(number, 2))
        elif choice == '4':
            print(int(number, 16))

        print("Would you like another operation?")
        cont = str(input('>>'))
        if cont.lower().startswith("n"):
            quit()
