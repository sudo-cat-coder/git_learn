# guess number game

from random import randint

def computer_number():
    return randint(1,50)

computer_num = computer_number()
running = True
while running:
    user = int(input("enter you'r number : "))
    if user > computer_num:
        print("you'r number bigger than me\n")
    elif user < computer_num:
        print("my number bigger than you\n")
    else:
        print('you win')
        print(f'my number was {computer_num}')
        isRunning = input('do you want to continue?[Y/n]').lower()
        if isRunning == 'N' or isRunning == 'n':
            running = False
    
