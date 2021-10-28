import random

player_scores = []

def start_game():
    print("Hello and welcome to the game where you guess a number #1-10:")
    picked_number = 0

    while picked_number == 0:
        try:
            picked_number = int(input("Pick a number #1-10: "))
        except ValueError:
            print("Please enter a numerical value:   ")

    solution = random.randrange(1, 10)

    number_count = 0
    while picked_number != solution:
        number_count += 1
        if picked_number < 1:
            try:
                picked_number = int(input("You attempted to enter a number lower than 10, this is wrong, keep trying!:"))
            except ValueError:
                print("Wrong value. Try again.")
            continue
        elif picked_number > 10:
            try:
                picked_number = int(input("You attempted to enter a number higher than 10, this is wrong, keep trying!:"))
            except ValueError:
                print("Wrong value. Try again.")
            continue
        elif picked_number < solution:
            try:
                picked_number = int(input("It's Higher:   "))
            except ValueError:
                print("Wrong. Try again.")
        elif picked_number > solution:
            try:
                picked_number = int(input("It's Lower:    "))
            except ValueError:
                print("Wrong. Try again.")

    if picked_number == solution:
        number_count += 1
        player_scores.append(number_count)
        print("Congratulations, #{} is correct! It took you {} tries, but you have finished the game.".format(picked_number, number_count))
        go_again = input("Do you want to play the game again? (Y/N) ")
        go_again = go_again.lower()
        if go_again == 'y':
            start_game()
        else:
            print("Goodbye!")






start_game()
