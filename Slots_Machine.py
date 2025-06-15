# spicy modules
import time
import random

# Chad 1 of the program - handles the automated spinning in a beautiful way!
def spinrow(symbols):
    luck1 = random.choice(symbols)
    luck2 = random.choice(symbols)
    luck3 = random.choice(symbols)

    print("-=-=-=-=-=-=-=-=-=-=-\nAnd the boxie spins.....")
    print("-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(0)
    print(f"|{luck1}|❓|❓|")
    time.sleep(0)
    print(f"|{luck1}|{luck2}|❓|")
    time.sleep(0)
    print(f"|{luck1}|{luck2}|{luck3}|")
    print("-=-=-=-=-=-=-=-=-=-=-")

    return luck1,luck2,luck3

# Chad 2 of the program - handles the result and gives out the profit (if exists) as well... (this stole the job of payout function)

def resultdecider(watashi, nbet):
    orng = 0
    pookie = 0
    wmelon = 0
    nbetlocal = nbet
    if watashi == ('🍊', '🍊', '🍊'):
        print(f"Bingo! You won ${2 * nbet}!")
        orng += 2 * nbetlocal

    elif watashi == ('🎀', '🎀', '🎀'):
        print(f"WOOHOO! You won ${7 * nbet}!!")
        pookie += 7 * nbetlocal

    elif watashi == ('🍉', '🍉', '🍉'):
        print(f"Yay! You won ${4 * nbet}!")
        wmelon += 4 * nbetlocal
    else:
        nbetlocal = 0
        print("Bonkers! Nothing to gain >.<")
    return orng or pookie or wmelon or nbetlocal

def bethandling(raw_input: str, balance: int):
    raw = raw_input.lower()

    if raw == "q":
        return "quit", balance
    
    if not raw.isdigit():
        print("Please enter a valid input!")
        return None, balance

    bet = int(raw)

    if bet < 10:
        print("Minimum allowed is $10 cuh..")
        return None, balance
    if bet > 1000:
        print("Maximum allowed is $1000 cuh...")
        return None, balance
    if bet > balance:
        print(f"Insufficient balance! [Current balance: {balance}]")
        return None, balance
    
    return bet, balance - bet

# Global Variables 👑

symbols = ('🎀' , '🍉' , '🍊')

def main():
    global balance, winning, symbols, carry_on, watashi, nbet

    balance = 0
    winning = 0
    carry_on = True
    nbet = 0

# Welcome Script

    print("----------------------------------")
    print("WELCOME TO GAMBLING!!!!!!!!!!!111")
    print("Symbols: 🎀 🍉 🍊")
    print("----------------------------------\n")

# User wish for starting or quitting - this is not in a loop because we dont want it to be repeated throughout bet sessions. (it is in a loop now lmao)
    while carry_on:
        wish = input("What would you like to do?: \n1. BETTING \n2. Quit \n> ")

        if wish == "1":
    # try block for swiftly passing code even if error occurs (which is likely to occur)
            try:
                ini_balance = int(input("----------------------------------\nWhat balance do you possess currently?: \n> $")) # the show begins, will ask user for their initial bal - in case of no winning throughout the game, theres no way to increase this *yet*
                if ini_balance <= 10:
                    print("----------------------------------\nSorry you do not have sufficient amount to participate!\n----------------------------------")
                    exit()
            except ValueError:
                print("  ~  Please enter a valid input!  ~  \n")
            else:
                balance += ini_balance
                break
        if wish == "2":
            print("Do come back again! 😘") # show quits too early :(
        
        else:
            print("\n...What? 😭\n----------------------------------")


# Main body for gamble paradise 😭

    while carry_on:
            str_betamt = (input("----------------------------------\nWhat amount would you like to bet? (min: $10, max: $1000) ['q' to quit]: \n> $"))
            
            bet_result, balance = bethandling(str_betamt, balance)

            if bet_result == "quit":
                print("Do come back again! 😘")
                exit()
            if bet_result == None:
                continue

            nbet = bet_result

            
            watashi = spinrow(symbols) # this will call the function spinrow() and let us capture the value of it in "watashi" variable for later use in resultdecider()
            wuw = resultdecider(watashi, nbet) # this will call the function resultdecider() and let us capture its value in "wuw" variable for later use in payout, possibly (didnt use).

            # if the user does NOT win
            if wuw == 0:
                    nbet *= 0 
            # if the user WINS1
            else:
                nbet *= 0
                winning += wuw
                winchoice = input("----------------------------------\nDo you wish to obtain a payout of your winning(s)? (y/n) \n> ") # prompts user if they want cashout or not
                if winchoice == "y":
                    balance += winning
                    time.sleep(3)
                    print(f"Successfully added ${winning} to your balance! [Balance = ${balance}]")
                    winning *= 0
                else:
                    print("Happy day ahead! 😊")
                
if __name__ == "__main__":
    main()

# the lines below are to be ignored

                # Ask user if they want to enter the payout
                #winwin = input("Do you want the payout of your winning(s)?: (y/n) \n> ")
                #if winwin == "y":
                #    meow = payout()
                #    print(meow)
                #    balance += winning
                #    print(f"Balance now: ${balance}")

# todo: 1. [DONE] create def payout logic : add the (if) winning to a seperate winning variable or just nbet\bet whatever ;;; thatll be the core of it.
# 2. decorations [pending]
# 3. rename variables probably and clean up the code [pending]
# 4. set up more validations, example: set up loops for wrong inputs. [almost done]
# 5. fix the wish -> set up loop [DONE]
# 6. add comments [DONE]
# 7, ADD TRY EXCEPT to allow exiting without triggering error in line 90 (whew)