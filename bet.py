MAX_BET = 100
MIN_BET = 1

def get_bet(balance, lines):
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                if bet * lines > balance:
                    print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
                else:
                    break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

if __name__ == "__main__":
    # Any test code here
    pass
