import random

# Word categories
words = {
    "Animals": ["elephant", "giraffe", "kangaroo", "zebra", "penguin"],
    "Countries": ["canada", "brazil", "japan", "france", "germany"],
    "Movies": ["inception", "titanic", "avatar", "gladiator", "joker"]
}

# ASCII Art for hangman stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Function to display the hangman
def display_hangman(tries):
    return hangman_stages[tries]

# Hint system
def provide_hint(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return f"Hint: The word contains the letter '{letter}'."
    return "No hints available."

# Main hangman game
def hangman():
    print("Welcome to Hangman!")
    print("Choose a category:")
    categories = list(words.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    category_choice = int(input("Enter the number of your choice: ")) - 1
    category = categories[category_choice]
    word = random.choice(words[category])
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    tries = 0
    max_tries = 6

    print(f"\nCategory: {category}")
    print(display_hangman(tries))
    print(" ".join(guessed_word))

    while tries < max_tries and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = letter
            print("Correct!")
        else:
            guessed_letters.add(guess)
            tries += 1
            print(f"Wrong! You have {max_tries - tries} tries left.")
        
        print(display_hangman(tries))
        print(" ".join(guessed_word))

        if tries < max_tries and "_" in guessed_word:
            hint = input("Would you like a hint? (yes/no): ").lower()
            if hint == "yes":
                print(provide_hint(word, guessed_letters))

    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Run the game
hangman()