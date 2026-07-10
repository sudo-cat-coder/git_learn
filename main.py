# guess number game
from rich import print
from random import randint

def computer_number():
    return randint(1,50)

computer_num = computer_number()
running = True
while running:
    try :
        user = int(input(" enter you'r number : "))
        if user > computer_num:
            print("[magenta]you'r number bigger than me[magenta]\n")
        elif user < computer_num:
            print("[magenta]my number bigger than you[magenta]n")
        else:
            print("[green]you win![green]")
            print(f'my number was {computer_num}')
            isRunning = input('do you want to continue?[Y/n]').lower()
            if isRunning == 'N' or isRunning == 'n':
                running = False
    except :
        print("[red] you didn't enter a number [red]\n")
        
    
