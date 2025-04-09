from game_logic import deposit, get_number_of_lines, get_bet, spin_slot_machine, print_slot_machine, Symbol_count, checkWinnings
ROWS = 3
COLS = 3

def main():
    balance = deposit()
    print(f"You have deposited ${balance}.")
    lines = get_number_of_lines()
    bet = get_bet(balance, lines)
    final_bet =  bet * lines
    balance -= final_bet
    print(f"You have bet ${bet} on {lines} lines. Total Bet: {final_bet}, Remaining Balance: ${balance}.")

    slots = spin_slot_machine(ROWS, COLS, Symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = checkWinnings(slots, lines, bet, Symbol_count)
    print(f"You won ${winnings} on lines {winning_lines}.")
    print(f"Your balance is now ${balance + winnings}.")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()  
