# Q19 - Text Analysis Functions

def count_words(text):
    return len(text.split())

def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

def count_consonants(text):
    return sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    return "".join(char for char in text if char.lower() not in "aeiou")

def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def longest_word(text):
    words = text.split()
    return max(words, key=len)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", is_palindrome(text))
    print("Without vowels:", remove_vowels(text))
    print("Longest word:", longest_word(text))
    print("Word Frequency:", word_frequency(text))

def main():
    try:
        user_text = input("Enter text: ")
        if user_text.strip() == "":
            print("Text cannot be empty.")
            return
        analyze_text(user_text)

    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()