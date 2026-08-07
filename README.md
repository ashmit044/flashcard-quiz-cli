# 🪪 Flashcard Quiz CLI

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Interface-CLI-green?style=flat-square" alt="CLI" />
  <img src="https://img.shields.io/badge/License-MIT-orange?style=flat-square" alt="License" />
</p>

An interactive command-line Python application designed to help Computer Science students learn and review AI, Machine Learning, and programming concepts through interactive flashcards and randomized quizzes.

---

## 🌟 Features

- 🎯 **Interactive Quizzes**: Take randomized flashcard quizzes across multiple CS topics.
- 📂 **Custom Decks**: Load JSON flashcard decks or create new custom question-answer cards directly in the CLI.
- 📊 **Score & Performance Tracking**: Automatically calculates quiz accuracy percentages and keeps track of study history.
- ⚙️ **Zero External Dependencies**: Built entirely using standard Python modules (`json`, `random`, `datetime`).

---

## 📁 Decks Included

Sample flashcard decks are stored in `sample_data/`:
- `python_basics.json`: Fundamental Python concepts (lists, dictionaries, loops, functions).
- `ai_ml_terms.json`: Essential AI/ML terms (Supervised Learning, Overfitting, Gradient Descent, Loss Function).

---

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/ashmit044/flashcard-quiz-cli.git
cd flashcard-quiz-cli
```

### 2. Run the Application
No extra package installation required! Standard Python 3 is all you need:
```bash
python main.py
```

---

## 💻 Menu Options

1. **Take a Quiz**: Select a deck, answer questions, and view your score percentage upon completion.
2. **Add New Flashcard**: Add custom questions and answers to existing or new JSON decks.
3. **View Study History & Stats**: Inspect your past quiz scores and overall performance history.
4. **Exit**: Exit the program.

---

## 🛠️ Project Structure

```text
flashcard-quiz-cli/
├── main.py              # Interactive CLI menu and quiz logic
├── utils.py             # File I/O helpers and score calculations
├── requirements.txt     # Dependency definition
├── sample_data/         # JSON flashcard deck files
│   ├── ai_ml_terms.json
│   └── python_basics.json
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

---

## 📚 What I Learned

Building this project helped reinforce key Python fundamentals:
- Reading and writing structured JSON data files with `json`.
- Handling user input validation and exceptions with `try/except`.
- Working with dictionaries, lists, and randomized sampling using `random`.
- Formatting clean command-line text output.

---

## 📄 License

Distributed under the MIT License.
