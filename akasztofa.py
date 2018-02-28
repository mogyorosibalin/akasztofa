from variables import *
import time
import subprocess


class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BOLD = "\033[1m"
    END = "\033[0m"


def reset_terminal():
    subprocess.call(["printf", "\033c"])


def check_given_letter(used_letters, letter):
    if type(letter) is str:
        if len(letter) == 1:
            if letter.upper() not in used_letters:
                used_letters.append(letter.upper())
                return used_letters
            raise ValueError("The letter is already in use!")
        else:
            raise ValueError("The letter must contain only one character!")
    else:
        raise ValueError("Please enter a valid string!")


def get_wrong_letters(given_word, used_letters):
    return sum([1 for letter in used_letters if letter not in given_word])


def show_playground(given_word, used_letters):
    colors = Colors()
    reset_terminal()
    print(figure[get_wrong_letters(given_word, used_letters)])
    print("\n")
    for letter in given_word:
        print(" {}{}{:^3}{} ".format(colors.GREEN, colors.BOLD, letter.upper() if letter in used_letters else " ", colors.END), end="")
    print()
    for i in given_word:
        print(" {:^3} ".format("---"), end="")
    print("\n")
    print("Letters used:\n")
    for letter in used_letters:
        if letter not in given_word:
            print(" {}{}{}{} ".format(colors.RED, colors.BOLD, letter, colors.END), end="")
    print("\n\n" + "-" * 60)


def is_lose(given_world, used_letters):
    return get_wrong_letters(given_word, used_letters) == len(figure) - 1


def is_win(given_world, used_letters):
    # return any([True for letter in given_word if letter not in used_letters])
    for letter in given_word:
        if letter not in used_letters:
            return False
    return True


used_letters = []
given_word = "kecske".upper()

while True:
    show_playground(given_word, used_letters)
    letter = input("Next letter: ")
    try:
        used_letters = check_given_letter(used_letters, letter)
    except ValueError:
        print("Invalid input")
    if is_lose(given_word, used_letters):
        show_playground(given_word, used_letters)
        print("You lost!")
        break
    if is_win(given_word, used_letters):
        show_playground(given_word, used_letters)
        print("You won!")
        break
    time.sleep(.5)