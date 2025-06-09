
# functions 

def balancef(balance):
    print(f"Your current balance is ${balance :.2f}.\n")
    print("======================================")


def deposit():
    print("======================================")
    dep_amt = float(input("Enter the amount you'd like to deposit: \n> $"))
    if dep_amt < 0:
        print("\nPlease enter a valid amount!")
        return 0
    else:
        print(f"\nSucessfully deposited ${dep_amt :.2f} in your balance.")
        print("======================================")
    return dep_amt

        
def withdraw(balance):
    print("======================================")
    withd_amt = float(input("Enter the amount to withdraw: \n> $"))

    if withd_amt <= balance:
        print(f"\nSucessfully withdrew ${withd_amt :.2f}.")
        return withd_amt
    elif withd_amt > balance:
        print(f"\nYou do not have sufficient balance to withdraw this amount! [Current Balance: ${balance}]")
        print("======================================")
    return 0

# global vars & core

def main():
    balance = 0
    is_working = True

# Logic
    while is_working:
        print("======================================")
        user_wish = input("Good Evening. What do you want to do? \n1. Check Balance \n2. Make a Deposit \n3. Withdraw an amount \n4. Exit \n> ")

        if user_wish == "1":  
            balancef(balance)
        elif user_wish == "2":
            balance += deposit()
        elif user_wish == "3":
            balance -= withdraw(balance)
        elif user_wish == "4":
            is_working = False
            print("Have a wonderful day ahead! 😊")
        else:
            print("Fym? 😭")

if __name__ == '__main__':
    main()