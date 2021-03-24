rules = """
                     _   _ ________  ___
                    | \ | |_   _|  \/  |
                    |  \| | | | | .  . |
                    | . ` | | | | |\/| |
                    | |\  |_| |_| |  | |
                    \_| \_/\___/\_|  |_/
                    
                Nim is a game about taking tokens.
        The last person to take all the tokens is the loser."""


def computer(user_input):
    print("Computer's turn.")

    if user_input == 0:
        amount_taken = 3
    else:
        amount_taken = 4 - user_input

    print("Computer took {} tokens.".format(amount_taken))

    return amount_taken


def user(tokens):
    print("Player turn.")

    while True:
        try:
            amount_to_take = int(input("How many tokens do you want to take? (1 - 3) >"))

            if amount_to_take > 3 or amount_to_take < 1 or (tokens - amount_to_take) < 0:
                print("You took a wrong amount of tokens. Try again.")

                continue
            break

        except ValueError:
            print("Enter a number.")

    print("You took {} tokens.".format(amount_to_take))

    return amount_to_take


def game():
    player = 0
    usr_input = 0
    tokens = 12

    print(rules)
    print()
    input("Start? (Press enter) >")

    while tokens != 0:
        print(tokens)

        if player == 1:
            usr_input = user(tokens)
            player -= 1
            tokens -= usr_input
        elif player == 0:
            player += 1
            tokens -= computer(usr_input)
        continue

    return player


def winner(winning_player):
    players = {0: "Computer", 1: "Player"}

    print("{} wins!".format(players.get(winning_player)))


if __name__ == '__main__':
    winner(game())
