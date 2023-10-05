from string import ascii_lowercase
import random
from random import shuffle

# Global variables
NUM_QUESTIONS_MAX_PER_QUIZ = 5
QUESTIONS = {
    "What is the maximum line length recommended by PEP8?": [
        "79", "80", "81", "82"
        ],
    "What is the recommended indentation size in PEP8?": [
        "4 spaces", "2 spaces", "8 spaces", "1 tab"
    ],
    "What is the recommended naming convention for variables in PEP8?": [
        "snake_case", "camelCase", "PascalCase", "kebab-case"
    ],
    "What is the recommended naming convention for classes in PEP8?": [
        "PascalCase", "snake_case", "camelCase", "kebab-case"
    ],
    "What is the recommended naming convention for constants in PEP8?": [
        "UPPER_CASE", "snake_case", "camelCase", "PascalCase"
    ],
    "What is the recommended naming convention for functions in PEP8?": [
        "snake_case", "camelCase", "PascalCase", "kebab-case"
    ],
    "What is the recommended naming convention for modules in PEP8?": [
        "snake_case", "camelCase", "PascalCase", "kebab-case"
    ],
    "What is the recommended naming convention for packages in PEP8?": [
        "snake_case", "camelCase", "PascalCase", "kebab-case"
    ],
    "What is the recommended way to import modules in PEP8?": [
        "import module",
        "from module import function",
        "from module import *",
        "from module import function as f"
    ],
    "What is the recommended way to organize imports in PEP8?": [
        "separate lines",
        "inline",
        "alphabetical order",
        "reverse alphabetical order"
    ],
    "What is the recommended way to write if statements in PEP8?": [
        "one line if statement",
        "multi-line if statement",
        "nested if statement",
        "if-else statement"
    ],
    "What is the recommended way to write for loops in PEP8?": [
        "for item in items:",
        "for i in range(len(items)):",
        "for item in enumerate(items):",
        "for item in items.items():"
    ],
    "What is the recommended way to write while loops in PEP8?": [
        "while condition:",
        "while True:",
        "while i < len(items):",
        "while i in items:"
    ],
    "What is the recommended way to write try-except blocks in PEP8?": [
        "try-except:",
        "try-finally:",
        "try-except-finally:",
        "try-finally-except:"
    ],
    "What is the recommended way to write comments in PEP8?": [
        "# This is a comment",
        "#this is a comment",
        "// This is a comment",
        "/* This is a comment */"
    ],
    "What is the recommended way to write docstrings in PEP8?": [
        "triple quotes", "single quotes", "double quotes", "no quotes"
    ],
    "What is the recommended way to write function arguments in PEP8?": [
        "def function(arg1, arg2):",
        "def function(arg1: type, arg2: type):",
        "def function(*args):",
        "def function(**kwargs):"
    ],
    "What is the recommended way to write function returns in PEP8?": [
        "return value",
        "return (value)",
        "return [value]",
        "return {key: value}"
    ],
    "What is the recommended way to write variable names in PEP8?": [
        "lowercase", "UPPERCASE", "CamelCase", "snake_case"
    ],
    "What is the recommended way to write class names in PEP8?": [
        "PascalCase", "snake_case", "camelCase", "kebab-case"
    ],
    "What is the recommended way to write constant names in PEP8?": [
        "UPPER_CASE", "snake_case", "camelCase", "PascalCase"
    ],
    "What is the recommended way to write function names in PEP8?": [
        "snake_case", "camelCase", "PascalCase", "kebab-case"
    ],
}


def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(question, alternatives):
    print(f"{question}?")
    labled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labled_alternatives:
        print(f"Please enter one of {', '.join(labled_alternatives)}")

    return labled_alternatives[answer_label]

# Shuffle the questions
questions = list(QUESTIONS.items())
shuffle(questions)

# Initial Welcome
print("""Welcome to the Python Quiz!
We will ask you 22 questions about Python and PEP8.

Good luck!""")
input("Press Enter to start the quiz...")

num_questions = min(NUM_QUESTIONS_MAX_PER_QUIZ, len(questions))
quetsions = random.sample(list(QUESTIONS.items()), k=num_questions)

# Print the questions
num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labled_alternatives:
        print(f"Please enter one of {', '.join(labled_alternatives)}")

    answer_label = input("\nChoice? ")
    answer = labled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐️ Correct! ⭐️")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} out of {len(questions)} questions")
