Number = input(f"Please enter a valid no \n")

def OddEven():
    try:
        User_Input = int(Number)
        if User_Input % 2 == 0:
            print(f"The number is even")
        else:
            print(f"The number is odd")
    except ValueError :
        print(f"This is not a valid number. Please enter an integer number")

while True:
    OddEven()
    Number = input(f"Please enter a valid no \n")