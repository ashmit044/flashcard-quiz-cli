import pytest

from utils import deck_filename, load_quiz_history, save_quiz_result


def test_deck_filename_cannot_escape_deck_directory():
    assert deck_filename("../private/Study Deck") == "private_study_deck.json"
    assert "/" not in deck_filename("../private/Study Deck")


def test_deck_filename_rejects_names_without_letters_or_numbers():
    with pytest.raises(ValueError, match="letters or numbers"):
        deck_filename("../---")


def test_quiz_history_round_trip_uses_requested_path(tmp_path):
    history_file = tmp_path / "history.json"

    save_quiz_result("Python Basics", 4, 5, 12.4, history_file)

    history = load_quiz_history(history_file)
    assert len(history) == 1
    assert history[0]["topic"] == "Python Basics"
    assert history[0]["score"] == "4/5"
    assert history[0]["accuracy_percent"] == 80.0
