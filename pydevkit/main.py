from pydevkit.calculator import calculate
from pydevkit.password_generator import generate_password
from pydevkit.text_tools import analyze_text


def calculator_menu():
    print("\n--- Calculator ---")
    print("Examples: 20+80, 50-15, 10*5, 100/4")

    expression = input("Enter expression: ")

    try:
        result = calculate(expression)
        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


def password_menu():
    print("\n--- Password Generator ---")

    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)

        print("Generated password:", password)

    except ValueError as error:
        print("Error:", error)


def text_menu():
    print("\n--- Text Analyzer ---")

    text = input("Enter your text: ")

    result = analyze_text(text)

    print("Words:", result["words"])
    print("Characters:", result["characters"])
    print("Lines:", result["lines"])


def main():
    while True:
        print("\n========================")
        print("       PyDevKit 🐍")
        print("========================")
        print("1. Calculator")
        print("2. Password Generator")
        print("3. Text Analyzer")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            calculator_menu()

        elif choice == "2":
            password_menu()

        elif choice == "3":
            text_menu()

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()