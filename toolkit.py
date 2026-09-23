# Personal Mini-Toolkit
# A collection of simple tools for everyday practice.


# Tool 1: Simple Calculator
# This tool performs basic calculations using two numbers.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print(f"Sorry, {operation} is not a valid operation.")
        return

    print(f"The answer is {answer}.")


# Tool 2: To-Do List
# This tool lets the user add, view, and remove tasks from a list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Remove task")
        print("4. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' has been added.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' has been removed.")
            else:
                print(f"Sorry, '{task}' is not on your list.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print(f"Sorry, {choice} is not a valid option.")


# Tool 3: Number Guessing Game
# This tool uses a loop and conditionals to let the user guess a number.
def guessing_game():
    secret_number = 7
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("Guess the secret number between 1 and 10!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print(f"{guess} is too low. Try again!")
        else:
            print(f"{guess} is too high. Try again!")


# Tool 4: Name Formatter
# This tool formats a name and gives the user a friendly greeting.
def name_formatter():
    print("\n--- Name Formatter ---")

    name = input("Enter your full name: ")
    formatted_name = name.strip().title()

    print(f"Your formatted name is: {formatted_name}.")
    print(f"Nice to meet you, {formatted_name}!")


# Main menu
print("========================================")
print("      WELCOME TO MY MINI-TOOLKIT")
print("========================================")

while True:
    print("\nChoose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Name Formatter")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        guessing_game()
    elif choice == "4":
        name_formatter()
    elif choice == "5":
        print("Thanks for using my Mini-Toolkit. Goodbye!")
        break
    else:
        print(f"Sorry, {choice} is not on the menu. Please choose 1 to 5.")