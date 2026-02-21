# Q17 - Palindrome Checker
# Checks if word/number is palindrome

def main():
    try:
        user_input = input("Enter word/number: ")
        cleaned_input = user_input.lower()

        reversed_input = cleaned_input[::-1]

        print("Original:", user_input)
        print("Reversed:", reversed_input)

        if cleaned_input == reversed_input:
            print("Result: PALINDROME")
        else:
            print("Result: NOT PALINDROME")

    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()