# Flashcard Quiz CLI

## About

Flashcard Quiz CLI is a simple command-line Python application designed to help students learn and review technical terms through interactive flashcards. Users can take randomized quizzes, track their percentage scores, and create custom flashcard decks stored in JSON files.

I created this project as a first-year B.Tech CSE (AI & ML) student to practice Python core concepts such as file input/output handling, dictionary storage, user input parsing, loops, and modular functions.

## Features

- Interactive quiz mode with randomized question order
- Custom flashcard creation saved as JSON files in sample_data/
- Automatic score and percentage accuracy calculation
- Local study history tracking to log quiz performance over time
- Clean terminal user interface built using Python standard library

## Installation

1. Clone this repository to your local machine:
   git clone https://github.com/ashmi-cse/flashcard-quiz-cli.git

2. Navigate into the project folder:
   cd flashcard-quiz-cli

3. Run the application (no third-party dependencies required):
   python main.py

## Usage

Run the program with `python main.py`. An interactive terminal menu will give you the following options:

1. Take a Quiz - Select a flashcard deck (e.g. Python Basics or AI/ML Terms), set question limits, and answer prompts.
2. Add New Flashcard - Add question and answer pairs to existing decks or create a new topic deck.
3. View Study History & Stats - View a history of past quiz dates, topics, score percentages, and total quizzes completed.
4. Exit - Exit the application.

## Future Improvements

- Add multiple-choice answer modes alongside free-text input
- Add a countdown timer for answering each flashcard question
- Export study session records to a CSV report file

## Author

ashmi-cse
