# Q3 - String Manipulator
# Author: Amulya Grace Daki
# Description: Performs various operations on a sentence

def main():
    try:
        sentence = input("Enter a sentence: ")

        if sentence.strip() == "":
            print("Sentence cannot be empty.")
            return

        # Basic Calculations
        characters_with_spaces = len(sentence)
        characters_without_spaces = len(sentence.replace(" ", ""))
        words_list = sentence.split()
        total_words = len(words_list)

        first_word = words_list[0]
        last_word = words_list[-1]
        reversed_sentence = sentence[::-1]

        # Display Results
        print("\n=== STRING ANALYSIS ===")
        print("Original:", sentence)
        print("Characters (with spaces):", characters_with_spaces)
        print("Characters (without spaces):", characters_without_spaces)
        print("Total words:", total_words)
        print("UPPERCASE:", sentence.upper())
        print("lowercase:", sentence.lower())
        print("TitleCase:", sentence.title())
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Reversed:", reversed_sentence)

    except Exception as error:
        print("An error occurred:", error)

if __name__ == "__main__":
    main()