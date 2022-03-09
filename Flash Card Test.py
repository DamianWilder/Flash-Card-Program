# Program to simulate flash cards for studying for test material for NOS110, Operating Systems Concepts

import random
from flashCardTerms import FLASH_CARDS

# look at importing OS to get_terminal_size for outputting strings to proper width


MENU_CHOICES = ("MODE", "HELP", "DONE", "START", "CHAPTERS")
CHAPTERS_LIST = [x for x in FLASH_CARDS]


def main():
    show_welcome()
    show_menu()
    program_running = True
    mode = "remembered"
    chapters = []
    while program_running:
        selection = get_user_choice()
        if selection == "MODE":
            mode = select_mode(mode)
        elif selection == "CHAPTERS":
            chapters = get_chapters()
        elif selection == "HELP":
            show_menu()
        elif selection == "START":
            print()
            if not chapters:
                print("You must select at least one chapter before beginning")
            else:
                begin_studying(mode, chapters)
        elif selection == "DONE":
            print()
            program_running = False


def begin_studying(mode, chapters):
    print()
    answer_key = [key for i in chapters for key in FLASH_CARDS[i]]
    if mode == "standard":
        random.shuffle(answer_key)
        correct_counter = 0
        for key in answer_key:
            correct_answer = key
            for i in FLASH_CARDS:
                if FLASH_CARDS[i].get(key):
                    print(FLASH_CARDS[i][key])
                    print()
                else:
                    continue
            answer = input("Answer:\t \t \t")
            if answer.upper() == correct_answer.upper():
                print("Correct!")
                correct_counter += 1
                print()
            elif answer == "done":
                quit_early = input("Would you like to exit early (y/n)? ")
                if quit_early == "y":
                    print()
                    break
            else:
                print(f"Correct answer: \t{key}")
                print()
        if correct_answer / len(answer_key) > 60:
            answer_message = f" That's {correct_counter / len(answer_key)}%!"
        else:
            answer_message = ""
        print(
            f"You got {correct_counter} answers correct out of {len(answer_key)}.{answer_message}"
        )

    elif mode == "remembered":
        testing = True
        random.shuffle(answer_key)
        already_correct = []
        while testing:
            correct_counter = 0
            for key in answer_key:
                correct_answer = key
                for i in FLASH_CARDS:
                    if FLASH_CARDS[i].get(key):
                        print(FLASH_CARDS[i][key])
                        print()
                    else:
                        continue
                answer = input("Answer:\t \t \t")
                if answer.upper() == correct_answer.upper():
                    print("Correct!")
                    correct_counter += 1
                    already_correct.append(correct_answer)
                    print()
                elif answer == "done":
                    quit_early = input("Would you like to exit early (y/n)? ")
                    if quit_early == "y":
                        print()
                        break
                else:
                    print(f"Correct answer: \t{key}")
                    print()
            if correct_answer / len(answer_key) > 60:
                answer_message = f" That's {correct_counter / len(answer_key)}%!"
            else:
                answer_message = ""
            print(
                f"You got {correct_counter} answers correct out of {len(answer_key)}.{answer_message}"
            )
            print()
            play_again = input("Play again (y/n)? ")
            print()
            if play_again == "y":
                for i in answer_key[::]:
                    if i in already_correct:
                        answer_key.remove(i)
                if not answer_key:
                    print("You already got everything right! Exiting to main menu")
                    print()
                    testing = False
                    break
            else:
                print("Exiting to main menu")
                print()
                testing = False
                break


def show_welcome():
    print(
        """
    Welcome to the NOS 110 Flash Card program.

    This program shows a definition and prompts the user for a "Key Term".
    You also have the option to have the program "remember"
    your answers for a second run through if you would like. 
    This allows you to focus on area's where you need improvement.
    """
    )


def show_menu():
    print(
        """
    Type 'MODE' to change mode.
    Type 'CHAPTERS' to select chapters.
    Type 'START' to begin studying.
    Type 'HELP' to view this menu.
    Type 'DONE' to close the program.
    """
    )


def select_mode(mode):
    # Choose whether to do a single run or multiple runs.
    print()
    selecting = True
    while selecting:
        print(f"You are currently on a {mode} run. ")
        print()
        print(
            'to select or view current setting for whether you would like to do to do one run, a "remembered" run that will omit correct answers from the question pool the the second time around.'
        )
        print()
        change = input("Would you like to change modes (y/n)? ")
        print()
        if change.lower() == "y":
            if mode == "standard":
                mode = "remembered"
            else:
                mode = "standard"
        print(f"You are now on a {mode} run")
        print()
        confirm = input("Would you like to keep this setting (y/n)? ")
        print()
        if confirm.lower() == "y":
            selecting = False
            return mode


def get_chapters():
    # Determine which group of flash cards to draw from to create the test.
    print()
    print(f"Chapters available: \n{CHAPTERS_LIST}")
    chapters = list(
        input(
            "Which chapter(s) would you like to study? Input chapter separated with a space. "
        ).split()
    )
    selection = []
    validate = True
    while validate:
        print()
        for item in chapters:
            if item in CHAPTERS_LIST:
                if item not in selection:  # Prevent duplicate values
                    selection.append(item)
                    print(f"Chapter {item} included")
            else:
                print(f"{item} not found in chapter list")
        print()
        answer = input("Does this look correct? (y/n) ")
        if answer.lower() != "y":
            print("\nAll right, we'll try again.")
            print(f"Chapters available: \n{CHAPTERS_LIST}")
            selection = []
            chapters = list(
                input(
                    "Which chapters would you like to study? input chapter 1, 3, 5, 6 separated with a space. "
                ).split()
            )
            continue
        else:
            print()
            validate = False
            return selection


def get_user_choice():
    while True:
        choice = input("Enter a menu option: ")
        if choice.upper() in MENU_CHOICES:
            return choice.upper()
        else:
            print("Invalid Choice, please choose again")
            print()


main()
