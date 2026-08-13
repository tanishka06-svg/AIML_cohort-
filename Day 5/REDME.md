# Bank Account Program

## Overview

In the session of Day 5, we learned about classes, objects, and methods in Python. To understand these concepts better, this program was created using a simple Bank Account example.

The program demonstrates how we can keep data and the operations together inside a class.

The class allows us to:

- Create a bank account
- Store the account owner's name
- Store and update the account balance
- Deposit money into the account
- Withdraw money from the account
- Check the current balance
- Handle cases where there is not enough balance

## Class Components

### Attributes

The `BankAccount` class has two main attributes:

- `self.owner` — Stores the name of the account owner.
- `self.balance` — Stores the current balance in the account.

### Methods

The class contains the following methods:

- `__init__()` — Sets the owner's name and the initial balance when the account is created.
- `deposit()` — Adds the given amount to the account balance.
- `withdraw()` — Checks the balance and withdraws the amount if sufficient money is available.
- `show_balance()` — Displays the current balance of the account.

## Execution Flow

### 1. Create the Account

account = BankAccount("Tanishka", 1000)

Here, we create an object called account from the BankAccount class.

The constructor receives two values:

owner = "Tanishka"
balance = 1000

These values are stored in the object using:

self.owner = owner
self.balance = balance

So, the starting balance of the account is:

1000
### 2. Deposit Money

account.deposit(1500)

Here, we call the deposit() method and add 1500 to the account.

The calculation will be:

1000 + 1500 = 2500

After the deposit, the balance becomes:

2500
### 3. Withdraw Money
account.withdraw(2000)

Now, we try to withdraw 2000 from the account.

Before withdrawing, the program checks whether the account has sufficient  balance:

if amount <= self.balance:

Since the current balance is 2500 and the withdrawal amount is 2000, the condition is true.

The amount is withdrawn successfully:

2500 - 2000 = 500

The new balance is:

500

If we tried to withdraw more money than the available balance, the program would display:

Insufficient balance

### 4. Display the Balance
account.show_balance()

At the end, the show_balance() method is called and displayed the remaining amount in the account.

## Output
Balance:500

## What I Learned

 I Learned how a class can be used to represent something from real life.

I also got a better understanding of:

Creating classes and objects
Using the __init__() method
Working with self
Creating and calling class methods
Updating attributes
Performing operations on objects

## Summary
This is a example of Object-Oriented Programming (OOP) in Python. Instead of writing separate code for every operation, we created a BankAccount class that contains both the account information and the operations that can be performed on it.
