# Q19 - Text Analysis Functions
# This program performs multiple analyses on user input text.
# Each operation is separated into functions for better structure.

# -----------------------------
# Text Analysis Functions
# -----------------------------

def count_words(text):
    # Splits text based on spaces and counts words
    return len(text.split())


def count_vowels(text):
    # Counts vowels (a, e, i, o, u)
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


def count_consonants(text):
    # Counts alphabetic characters that are not vowels
    return sum(1 for char in text.lower()
               if char.isalpha() and char not in "aeiou")


def reverse_text(text):
    # Reverses entire string using slicing
    return text[::-1]


def is_palindrome(text):
    # Removes spaces and converts to lowercase
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def remove_vowels(text):
    # Removes vowels from text
    return "".join(char for char in text
                   if char.lower() not in "aeiou")


def word_frequency(text):
    # Creates dictionary counting occurrences of each word
    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def longest_word(text):
    # Finds word with maximum length
    words = text.split()
    return max(words, key=len)


# -----------------------------
# Main Function
# -----------------------------

def analyze_text(text):
    print("\n=== TEXT ANALYSIS RESULTS ===")
    print("Total Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed Text:", reverse_text(text))
    print("Is Palindrome:", is_palindrome(text))
    print("Text Without Vowels:", remove_vowels(text))
    print("Longest Word:", longest_word(text))
    print("Word Frequency:", word_frequency(text))


def main():
    try:
        user_text = input("Enter text: ")

        # Validating empty input
        if user_text.strip() == "":
            print("Text cannot be empty.")
            return

        analyze_text(user_text)

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()