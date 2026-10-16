import json
import os
import re
import time
from datetime import datetime
from pathlib import Path


DEFAULT_HISTORY_FILE = Path(__file__).resolve().parent / "quiz_history.json"


def deck_filename(topic_name):
    """Create a safe, portable JSON filename from a user-provided topic."""
    slug = re.sub(r"[^a-z0-9_-]+", "_", topic_name.lower()).strip("_-")
    if not slug:
        raise ValueError("Topic name must contain letters or numbers.")
    return f"{slug}.json"

# Helper function to clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load flashcards from a JSON file
def load_deck(filepath):
    """
    Reads a flashcard JSON file and returns a list of question dictionaries.
    """
    if not os.path.exists(filepath):
        print(f"Error: Could not find deck file at {filepath}")
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            cards = json.load(f)
            return cards
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON file {filepath}. It might be corrupted.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Save flashcards to a JSON file
def save_deck(filepath, cards):
    """
    Saves a list of flashcard dictionaries to a JSON file.
    """
    try:
        # Create folder if it doesn't exist
        folder = os.path.dirname(filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(cards, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving flashcard deck: {e}")
        return False

# Load history log of past quiz attempts
def load_quiz_history(history_file=DEFAULT_HISTORY_FILE):
    if not os.path.exists(history_file):
        return []
    try:
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

# Save a completed quiz session to history
def save_quiz_result(topic_name, score, total_questions, duration_seconds, history_file=DEFAULT_HISTORY_FILE):
    history = load_quiz_history(history_file)
    
    # Calculate percentage accuracy
    accuracy = round((score / total_questions) * 100, 1) if total_questions > 0 else 0
    
    # Create record dictionary
    record = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "topic": topic_name,
        "score": f"{score}/{total_questions}",
        "accuracy_percent": accuracy,
        "time_seconds": round(duration_seconds, 1)
    }
    
    history.append(record)
    
    try:
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
        print("Quiz result saved to history!")
    except Exception as e:
        print(f"Failed to save quiz history: {e}")

# Display past study session statistics
def display_history_stats(history_file=DEFAULT_HISTORY_FILE):
    history = load_quiz_history(history_file)
    
    if not history:
        print("\n--- No Quiz History Found ---")
        print("Take your first quiz to track your progress!\n")
        return
        
    print("\n" + "=" * 55)
    print("                STUDY SESSION HISTORY")
    print("=" * 55)
    print(f"{'Date':<18} | {'Topic':<15} | {'Score':<7} | {'Accuracy':<8}")
    print("-" * 55)
    
    total_quizzes = len(history)
    total_accuracy_sum = 0
    
    for entry in history:
        date = entry.get("date", "N/A")
        topic = entry.get("topic", "General")
        # Truncate topic if too long
        if len(topic) > 15:
            topic = topic[:12] + "..."
        score = entry.get("score", "0/0")
        accuracy = entry.get("accuracy_percent", 0)
        total_accuracy_sum += accuracy
        
        print(f"{date:<18} | {topic:<15} | {score:<7} | {accuracy}%")
        
    print("-" * 55)
    avg_accuracy = round(total_accuracy_sum / total_quizzes, 1) if total_quizzes > 0 else 0
    print(f"Total Quizzes Completed: {total_quizzes}")
    print(f"Average Accuracy: {avg_accuracy}%")
    print("=" * 55 + "\n")
