import os
import random
import time
from colorama import Fore, Style, init
from pyfiglet import figlet_format


init(autoreset=True)


os.system("title 0x75s BlackJack b0.3")

def print_0x75():
    art = figlet_format("0x75s", font="slant")
    print(Fore.YELLOW + Style.BRIGHT + art)

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for rank, _ in hand:
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def print_hand(name, hand, reveal_all=True):
    print(f"{Fore.CYAN + Style.BRIGHT}{name}'s hand:")
    if name == "Dealer" and not reveal_all:
        first_card = f"{hand[0][0]}{hand[0][1]}"
        print(f"{first_card}  Hidden card")
        print("  → Total: ?")
    else:
        for card in hand:
            print(f"{card[0]}{card[1]}", end='  ')
        print(f"  → Total: {calculate_hand_value(hand)}")
    print()


def dealer_turn(deck, dealer_hand, player_value):
    print(Fore.MAGENTA + Style.BRIGHT + "\nDealer's turn:")
    while True:
        value = calculate_hand_value(dealer_hand)
        print_hand("Dealer", dealer_hand, reveal_all=True)  

        if value > 21:
            print(Fore.RED + Style.BRIGHT + "Dealer busts!")
            break
        elif value >= 17:
            print(Fore.MAGENTA + Style.BRIGHT + f"Dealer stands on {value}")
            break
        else:
            print(Fore.MAGENTA + Style.BRIGHT + f"Dealer hits on {value}")
            time.sleep(1)
            card = deck.pop()
            dealer_hand.append(card)
            print(f"Dealer draws {card[0]}{card[1]}\n")
            time.sleep(1)


def main():
    print_0x75()
    print(Fore.MAGENTA + Style.BRIGHT + figlet_format("BlackJack", font="slant"))

    while True:
        deck = create_deck()
        random.shuffle(deck)

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print_hand("Dealer", dealer_hand, reveal_all=False)
        print_hand("Player", player_hand, reveal_all=True)

       
        while True:
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print(Fore.RED + Style.BRIGHT + "You bust! Dealer wins.")
                break
            choice = input(Fore.GREEN + "Hit or Stand? (h/s): ").lower()
            if choice == 'h':
                card = deck.pop()
                player_hand.append(card)
                print(f"You drew {card[0]}{card[1]}")
                print_hand("Player", player_hand, reveal_all=True)
            elif choice == 's':
                print(f"You stand on {player_value}")
                break
            else:
                print("Invalid input. Please type 'h' or 's'.")

        player_value = calculate_hand_value(player_hand)
        if player_value <= 21:
            dealer_turn(deck, dealer_hand, player_value)

            dealer_value = calculate_hand_value(dealer_hand)
            print_hand("Dealer", dealer_hand, reveal_all=True)
            print_hand("Player", player_hand, reveal_all=True)

            if dealer_value > 21 or player_value > dealer_value:
                print(Fore.GREEN + Style.BRIGHT + "You win!")
            elif player_value < dealer_value:
                print(Fore.RED + Style.BRIGHT + "Dealer wins!")
            else:
                print(Fore.YELLOW + Style.BRIGHT + "It's a tie!")

        again = input(Fore.BLUE + "Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Bye!")
            break
        print("\n" + "-"*40 + "\n")
        time.sleep(1)

if __name__ == "__main__":
    main()

