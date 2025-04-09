from game_logic import deposit, get_number_of_lines, get_bet

def main():
    balance = deposit()
    print(f"You have deposited ${balance}.")
    lines = get_number_of_lines()
    bet = get_bet(balance, lines)
    print(f"You have bet ${bet} on {lines} lines.")

if __name__ == "__main__":
    main()  
