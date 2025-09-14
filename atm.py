import numpy as np
import time
from datetime import datetime#for adding timestamps to transactions
print("Welcome to Mania Bank!!")#the name of the bank
language = str(input("Select Your Language Urdu/English :"))#let the user to choose the language
#display welcome message based on choosed language
if language == "Urdu":
    print("Khush Amdeed")#welcome message in urdu
elif language == "English":
    print(f"Welcome User!")
#initialize an empty list to store transaction history
transaction_history = []
    
pins = np.array([1234,2345,3456,4567,5678,6789,7891,3451,2022,2025,3456,6732,4651,1236,2654])#the array of pins

balance = np.array([12000,15000,25000,35000,45000,2000,19000,20000,35000,43000,25000,8900,25000,1250000,23450])#the array of balance

attempts = 3#it define that how many attempts are available for the user
#loop to validate pin
while attempts>0: #Continue while attempts remain
  pin = int(input("Enter your pin:"))#ask user to enter pin
  
  if pin in pins:#if the entered pin is in pins array then it shows us our balance
    index = np.where(pins==pin)[0][0]#get index of matching pin
    print(f"Your balance is:{balance[index]}")
    
    break#exit loop after successful login
  else:
    attempts-=1#Reduce attempts if pin is wrong
    print(f"Invalid pin! Attempts left: {attempts}")#show remaining attempts
  if attempts==0:#if no attempts left
    print(f"Too many attempts! your card blocked")
    exit()#exit the prg
#show atm menu
print("Atm Menu:")
User_choice = int(input("1.Balance\n2.Deposit\n3.Withdraw\n4.New User\nPlease select an option:"))#it will show the user the menu and ask for the choice
#option 1 : Check Balance
if User_choice == 1:
    print(f"Your Balance is RS.{balance[index]}")#show current balance
    transaction_history.append(f"{datetime.now()}-Balance: {balance[index]}")#balance check with timestamp
    show_history=int(input("Do you want to see your transaction history? 1.Yes 2.No:"))#Ask if user wants to see their transaction history
    if show_history==1:
      for i in transaction_history:#print each transaction
       print(i)
    elif show_history==2:
      print("No transaction history")#if the user declines
#option 2:deposit money
elif User_choice == 2:
    deposit_user = int(input("Please enter the amount that you want to deposit :"))#ask deposit amount
    balance[index]+= deposit_user#add deposit to balance
    transaction_history.append(f"{datetime.now()}-Deposited amount:{deposit_user}")#deposit with timestamp
    print(f"You have deposited Rs.{deposit_user}")#confirm deposit
    print(f"Your total balance is Rs.{balance[index]}")#show updated balance
    show_history=int(input("Do you want to see your transaction history? 1.Yes 2.No:"))
    if show_history==1:
      for i in transaction_history:#print each transaction
       print(i)
    elif show_history==2:
      print("No transaction history")#if the user don't want to see the history then it
#option 3:Withdraw money
elif User_choice == 3:
    withdraw_user = int(input("Please enter the amount:"))#ask withdrawal amount
    balance[index]-=withdraw_user#deduct withdrawal from balance
    transaction_history.append(f"{datetime.now()}-Withdraw amount:{withdraw_user}")#withdraw with timestamp
    print(f"You with draw Rs.{withdraw_user}")
    print(f"your total balance is Rs.{balance[index]}")#show updated balance
    show_history=int(input("Do you want to see your transaction history? 1.Yes 2.No:"))#it will ask the user to see
    if show_history==1:
      for i in transaction_history:#print each transaction history
       print(i)
    elif show_history==2:
      print("No transaction history")#if the user don't want to see the history then it
#option 4:register new user
elif User_choice==4:
  while True:#loop to allow multiple new users
    choice = input(" Do You want to add new user? Yes/No: ")#asks if user want to register
    if choice == "Yes":
      new_pin = int(input("Enter your pin:"))#ask for new pin
      new_balance = int(input("Enter your balance:"))#ask for new balance
      if new_pin in pins:#check if pin is already exist
       print("This pin already exist.Please choose different one!")#warn user
      else:
       pins = np.append(pins , new_pin)#add new pin to array
       balance=np.append(balance,new_balance)#add new balance to array
       print("Successfully registered")#confirm registered
    elif choice == "No":
     print("No more user will be added")#exit registration loop
     break
    else:
     print("Invalid choice")#handle invalid choice
     #show updated pins and balances
    print(f"updated pins array:",pins)#Display all pins
    print(f"updated balance array:",balance)#display all balances
