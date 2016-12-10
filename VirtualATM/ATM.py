
import sys
import csv
import os.path
import time
from random import randint

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'bank')
pin = 0

# This CodeBlock Checks if the value of the card number / pin is valid
def checkCard(cardNumber):
    with open(filename, 'r') as f:
        next(f)
        reader = csv.reader(f)
        userRow = 0
        for row in reader:
            row = list(map(float, row))
            userRow = userRow + 1
            if cardNumber == int(row[0]):
                k = 1
                pin = int(input("Please enter your four digit pin: "))
                while k < 5:
                    if pin == int(row[1]):
                        return (userRow, pin)
                    else:
                        pin = int(input("Incorrect, please try again: "))
                        k = k + 1
                print("Access Denied!")
                sys.exit()
    print("This card does not exist, please try again.")
    createAccount(cardNumber, )

# This function creates a new account
def createAccount(cardNumber, pin):
    text = (str(cardNumber) + "," + str(pin) + ",0\n")
    with open(filename, 'a') as appendFile:
        appendFile.write(text)

# This function overwites the Balance
def replaceBalance(userRow, cardNumber, pin, balance):
    lines = open(filename, 'r').readlines()
    text = (str(cardNumber) + "," + str(pin) + "," + str(balance)+ "\n")
    lines[userRow] = text
    out = open(filename, 'w')
    out.writelines(lines)
    out.close()

# This function checks customer's Balance
def checkBalance(cardNumber, userRow):
    with open(filename, 'r') as f:
        next(f)
        reader = csv.reader(f)
        k = 0
        for row in reader:
            k = k + 1
            if k == userRow:
                balance = row[2]
                return balance
        print("Oops: BALANCE READ ERROR")
        sys.exit()

# This function allows the customer to deposit
def deposit(cardNumber, userRow, balance):
    depositValue = float(input("How much do you want to deposit? "))
    balance = float(balance) + depositValue
    print("Your new balance is $%s" % str(balance))
    replaceBalance(userRow, cardNumber, pin, balance)
    return balance


# This function allows customer to withdraw
def withdrawal(cardNumber, userRow, balance):
    withdrawalValue = float(input("How much money do you want to withdraw? "))
    if float(balance) - withdrawalValue >= 0:
        balance = float(balance) - float(withdrawalValue)
        print("Awesome")
        print("Your withdrawal was successful.")
        print("By the way, your new balance is: $%s" %balance)
        replaceBalance(userRow, cardNumber, pin, balance)
        return balance
    else:
        print("Oopsie Daisy: Sadly you do not have enough money to withdraw.")
        return float(balance)

# Clear console when needed
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Program Begins (main menu and GUI)
cls()
print ("------------------WELCOME TO-------------------")
print ("-----KING MALCOLM VIRTUAL ATM OF GREATNESS -------")
print ("---WHERE ALL ASPIRATIONS ARE MADE REALITY---")
userRow = 0
while userRow == 0:
    cardNumber = input("Please enter your card number, '1' to exit, or '0' to create a new account: \n")
    if cardNumber == 1:
        sys.exit()
    elif cardNumber == 0:
        cardNumber = input("Create an account right now, just enter a FIVE DIGIT card number: ")
        pin = randint(1001,9999)
        print("Your new pin is: %s" % pin)
        createAccount(cardNumber, pin)
        userRow, pin = (checkCard(cardNumber))
    else:
        userRow, pin = (checkCard(cardNumber))
balance = checkBalance(cardNumber,userRow)

selection = 0
while selection < 4:
    selection = input("\nWhat would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n\n")
    if selection is 1:
        print("Your balance is: $%s" % balance)
    elif selection is 2:
        balance = deposit(cardNumber, userRow, balance)
    elif selection is 3:
        balance = withdrawal(cardNumber, userRow, balance)
    elif selection is 4:
        print("Thank you for using King Malcolm's Virtual ATM of greatness, do have a nice day and come back soon!")
sys.exit()