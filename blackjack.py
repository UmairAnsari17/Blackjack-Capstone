import random
from art11 import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_cards = random.choice(cards)
    return random_cards

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
        if u_score == c_score:
            return "Draw 😊"
        elif c_score == 0:
            return "Lose, the Opponent has BlackJack!😱"
        elif u_score == 0:
            return "Win, With a BlackJack!😎"
        elif u_score > 21:
            return "You Went Over. You Lose😭"
        elif c_score > 21:
            return "Opponent Went Over. You Win😁"
        elif u_score > c_score:
            return "You Win😃"
        else:
            return "You Lose 😤"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score  = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Your score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over =True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, and final score is: {user_score}")
    print(f"Computer's final hand is: {computer_cards}, and it's final score is: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 50)
    play_game()