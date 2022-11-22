# Adding in colourful text
class Colour:
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    White = "\u001b[37m"
    Cyan = "\u001b[36m"
    Reset = "\u001b[0m"
    bracketsymbol = Blue
    normaltext = Cyan
    plussymbol = Red
    lines = White
    text = Yellow

# Function to get input with formated and coloured chacters
def getinput(option,range):
    while True:
        try:
            choice = int(input(f"({Colour.text}{option}{Colour.Reset}) > "))
            if range == 0:
                return 1
            elif 0 < choice <= range:
                return choice
            else:
                display("Invalid Option")
        except Exception:
            display("Invalid Option")
    return choice

# This function allows the user to display a formatted menu to the cli and get input based on the options provided
def menu(options):
    print(f"{Colour.bracketsymbol}[{Colour.plussymbol}+{Colour.bracketsymbol}]{Colour.Yellow} {options[0]}   ",end="")
    for index, option in enumerate(options[1:],1):
        print(f"{Colour.Yellow}[{index}] {option}   ",end="")
    print(f"{Colour.Reset}\n")
    return getinput(options[0], len(options)-1)

# Displays text in a nice colourful format
def display(text):
    print(f"{Colour.bracketsymbol}[{Colour.plussymbol}+{Colour.bracketsymbol}] {Colour.Reset}{text}\n")
