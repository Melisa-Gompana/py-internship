import string

# Function to count words in text
def count_words(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()  # Split into words
    return len(words)  # Return the count of words

# Main program
user_input = input("Please enter a sentence or paragraph: ")  # Get user input

# Check for empty input
if not user_input.strip():
    print("Error: You entered an empty input. Please enter some text.")
else:
    # Count the words and display the result
    word_count = count_words(user_input)
    print(f"The number of words in your input is: {word_count}")
