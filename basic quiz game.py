def ask_question(question, options, correct_option):
    """Displays a question, validates user input, and provides feedback."""
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Validate user input
    while True:
        try:
            user_input = int(input("\nEnter the number of your answer: "))
            if 1 <= user_input <= len(options):
                return user_input == correct_option
            else:
                print(f"Please enter a valid option number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def quiz():
    """Main function to run the quiz game."""
    # List of questions, options, and correct answers
    questions = [
        {
            "question": "What is the capital of Canada?",
            "options": ["Toronto", "Ottawa", "Vancouver", "Montreal"],
            "correct": 2  # 'Ottawa' is the correct answer (index 2)
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct": 2  # 'Mars' is the correct answer (index 2)
        },
        {
            "question": "Which ocean is the largest?",
            "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
            "correct": 3  # 'Pacific' is the correct answer (index 3)
        }
    ]

    # Initialize score
    score = 0

    # Loop through each question
    for q in questions:
        correct = ask_question(q["question"], q["options"], q["correct"])
        
        if correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was option {q['correct']}.\n")

    # Display final score
    print(f"\nYour final score is {score}/{len(questions)}.")
    
    # Provide feedback based on performance
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score >= len(questions) // 2:
        print("Good job! You got more than half right.")
    else:
        print("Better luck next time! Keep practicing.")

if __name__ == "__main__":
    print("Welcome to the Multiple-Choice Quiz Game!")
    quiz()
    print("Thank you for playing!")
