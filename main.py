from random import *
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {
    nine: "9",
    ten: "10",
    jack: "J",
    queen: "Q",
    king: "K",
    ace: "A",
}

player_score = 0
computer_score = 0


def start():
    print("Let's play a game of Akilli X Poker Dice.")
    while game():
        pass
    scores()


def game():
    print("The Computer will help you throw your 5 Dice.")
    throws()
    return play_again()


def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print("Dice", i + 1, ":", names[dice[i]])

    result = hand(dice)
    print("You currently have ", result)

    while True:
        rerolls = int(input("How many dice do you want to throw again? "))
        try:
            if rerolls in (1, 2, 3, 4, 5):
                break
        except ValueError:
            pass
        print("Ooops!!! I didn't understand that. Please enter 1, 2, 3, 4, or 5.")

    if rerolls == 0:
        print("You finished with ", result)
    else:
        roll_number = rerolls
        dice_rerolls = roll(roll_number)
        dice_changes = [i for i in range(rerolls)]
        print("Enter the number of a dice to roll: ")
        iterations = 0
        while iterations < rerolls:
            iterations += 1
            while True:
                selection = int(input(""))
                try:
                    if selection in (1, 2, 3, 4, 5):
                        break
                except ValueError:
                    pass
                print("Ooops!!! I didn't understand that. Please enter 1, 2, 3, 4, or 5.")
            dice_changes[iterations-1] = selection - 1
            print("You have change dice ", selection)
        iterations = 0
        while iterations < rerolls:
            iterations += 1
            replacement = dice_rerolls[iterations-1]
            dice[dice_changes[iterations - 1]] = replacement
        dice.sort()
        for i in range(len(dice)):
            print("Dice", i + 1, ":", names[dice[i]])
        result = hand(dice)
        print("You finish with ", result)


def roll(roll_number):
    numbers = [i for i in range(1, 7)]
    dice = [i for i in range(roll_number)]
    iterations = 0
    while iterations < roll_number:
        iterations = iterations + 1
        dice[iterations-1] = choice(numbers)
    return dice


def hand(dice):
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1, 2, 3, 4, 5]
    straight2 = [2, 3, 4, 5, 6]

    if dice == straight1 or dice == straight2:
        return "A straight!"
    elif dice_hand[0] == 5:
        return "Five of a Kind!"
    elif dice_hand[0] == 4:
        return "Four of a Kind!"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "A Full house!"
        else:
            return "Three of a Kind!"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "Two pair."
        else:
            return "One pair."
    else:
        return "A high Card"


def play_again():
    answer = input("Would you like to play again? y/n : ").lower()
    if answer in ("y", "yes", "of course", "of course!"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next!!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


if __name__ == "__main__":
    start()