import os
import random
import time
from pathlib import Path
from utils import (
    clear_screen,
    load_deck,
    save_deck,
    save_quiz_result,
    display_history_stats,
    deck_filename,
)

BASE_DIR = Path(__file__).resolve().parent
SAMPLE_DATA_DIR = BASE_DIR / "sample_data"

def get_available_decks():
    """Returns a list of JSON deck filenames in the sample_data directory."""
    if not os.path.exists(SAMPLE_DATA_DIR):
        os.makedirs(SAMPLE_DATA_DIR)
        
    files = os.listdir(SAMPLE_DATA_DIR)
    json_files = [f for f in files if f.endswith(".json")]
    return json_files

def select_deck():
    """Allows user to pick a deck from available JSON files."""
    decks = get_available_decks()
    
    if not decks:
        print("No flashcard decks found in the sample_data folder.")
        return None, None
        
    print("\n--- Available Flashcard Decks ---")
    for index, filename in enumerate(decks, 1):
        topic_name = filename.replace(".json", "").replace("_", " ").title()
        print(f"{index}. {topic_name} ({filename})")
        
    print("-" * 35)
    choice = input("Select a deck number (or 'b' to go back): ").strip()
    
    if choice.lower() == 'b':
        return None, None
        
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(decks):
            selected_file = decks[idx]
            filepath = SAMPLE_DATA_DIR / selected_file
            topic_name = selected_file.replace(".json", "").replace("_", " ").title()
            return filepath, topic_name
        else:
            print("Invalid choice number.")
            return None, None
    except ValueError:
        print("Please enter a valid number.")
        return None, None

def run_quiz():
    """Runs an interactive quiz session."""
    filepath, topic_name = select_deck()
    if not filepath:
        return
        
    cards = load_deck(filepath)
    if not cards:
        print("This deck is empty or could not be loaded!")
        input("\nPress Enter to return to main menu...")
        return
        
    print(f"\nLoaded deck '{topic_name}' with {len(cards)} cards.")
    
    # Ask user how many questions they want to attempt
    num_input = input(f"How many questions would you like to attempt? (1-{len(cards)}, default: all): ").strip()
    if num_input.isdigit():
        num_q = int(num_input)
        num_q = max(1, min(num_q, len(cards)))
    else:
        num_q = len(cards)
        
    # Shuffle cards for randomness
    shuffled_cards = list(cards)
    random.shuffle(shuffled_cards)
    selected_cards = shuffled_cards[:num_q]
    
    print("\nStarting Quiz... Type your answer and press Enter.")
    print("--------------------------------------------------")
    
    score = 0
    start_time = time.time()
    
    for i, card in enumerate(selected_cards, 1):
        question = card.get("question", "")
        correct_answer = card.get("answer", "").strip()
        
        print(f"\nQuestion {i} of {num_q}:")
        print(f"  {question}")
        
        user_ans = input("Your Answer: ").strip()
        
        # Check answer (case-insensitive)
        if user_ans.lower() == correct_answer.lower():
            print("  [CORRECT] Good job!")
            score += 1
        else:
            print(f"  [INCORRECT] Correct answer: {correct_answer}")
            
    end_time = time.time()
    elapsed_seconds = end_time - start_time
    
    # Calculate score percentage
    pct = round((score / num_q) * 100, 1)
    
    print("\n" + "=" * 40)
    print("               QUIZ SUMMARY")
    print("=" * 40)
    print(f" Topic: {topic_name}")
    print(f" Score: {score} out of {num_q} ({pct}%)")
    print(f" Time Taken: {round(elapsed_seconds, 1)} seconds")
    
    if pct == 100:
        print(" Performance: Perfect score! Excellent work!")
    elif pct >= 70:
        print(" Performance: Good job! Keep practicing!")
    else:
        print(" Performance: Needs review. Try again soon!")
    print("=" * 40)
    
    # Ask to save results
    save_opt = input("\nWould you like to save this result to history? (y/n): ").strip().lower()
    if save_opt == 'y':
        save_quiz_result(topic_name, score, num_q, elapsed_seconds)
        
    input("\nPress Enter to return to main menu...")

def add_new_flashcard():
    """Allows user to add a new card to an existing or new deck."""
    print("\n--- Add New Flashcard ---")
    print("1. Add to existing deck")
    print("2. Create a new topic deck")
    
    choice = input("Select option (1/2): ").strip()
    
    if choice == "1":
        filepath, topic_name = select_deck()
        if not filepath:
            return
        cards = load_deck(filepath)
    elif choice == "2":
        raw_name = input("Enter new topic name (e.g. Data Structures): ").strip()
        if not raw_name:
            print("Topic name cannot be empty.")
            return
        try:
            filename = deck_filename(raw_name)
        except ValueError as error:
            print(error)
            return
        filepath = SAMPLE_DATA_DIR / filename
        topic_name = raw_name.title()
        cards = []
    else:
        print("Invalid option.")
        return
        
    print(f"\nAdding flashcard to '{topic_name}'...")
    question = input("Enter question prompt: ").strip()
    answer = input("Enter correct answer: ").strip()
    
    if not question or not answer:
        print("Question and Answer cannot be empty!")
        input("\nPress Enter to return...")
        return
        
    cards.append({
        "question": question,
        "answer": answer
    })
    
    if save_deck(filepath, cards):
        print(f"\nSuccess! Added new card to '{topic_name}' (Total cards: {len(cards)}).")
    else:
        print("\nFailed to save card.")
        
    input("\nPress Enter to return to main menu...")

def main():
    """Main CLI program loop."""
    while True:
        clear_screen()
        print("==========================================")
        print("        FLASHCARD QUIZ CLI APP")
        print("==========================================")
        print("  1. Take a Quiz")
        print("  2. Add New Flashcard")
        print("  3. View Study History & Stats")
        print("  4. Exit")
        print("==========================================")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            run_quiz()
        elif choice == "2":
            add_new_flashcard()
        elif choice == "3":
            display_history_stats()
            input("Press Enter to return to main menu...")
        elif choice == "4":
            print("\nThank you for studying! Good luck with your learning journey.")
            break
        else:
            print("Invalid input. Please choose a option between 1 and 4.")
            time.sleep(1)

if __name__ == "__main__":
    main()
