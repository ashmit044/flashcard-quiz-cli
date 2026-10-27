import json

import pytest

from utils import (
    deck_filename,
    display_history_stats,
    load_deck,
    load_quiz_history,
    save_quiz_result,
)


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


@pytest.mark.parametrize(
    "payload",
    [
        '{"sessions": []}',
        '[null]',
        '[{"date":"today","topic":"Python","score":"1/1",'
        '"accuracy_percent":NaN,"time_seconds":1}]',
    ],
)
def test_invalid_quiz_history_is_rejected_without_overwriting_existing_data(
    tmp_path, capsys, payload
):
    history_file = tmp_path / "history.json"
    history_file.write_text(payload, encoding="utf-8")

    with pytest.raises(ValueError, match="Quiz history"):
        load_quiz_history(history_file)

    assert not save_quiz_result("Python Basics", 1, 1, 5, history_file)
    assert history_file.read_text(encoding="utf-8") == payload
    assert "left unchanged" in capsys.readouterr().out


def test_corrupt_json_history_is_reported_to_stats_view(tmp_path, capsys):
    history_file = tmp_path / "history.json"
    history_file.write_text("{broken", encoding="utf-8")

    display_history_stats(history_file)

    assert "Could not display quiz history" in capsys.readouterr().out


@pytest.mark.parametrize(
    "payload",
    [
        {"question": "What is Python?", "answer": "A language."},
        [None],
        [{"question": "What is Python?"}],
        [{"question": "What is Python?", "answer": 42}],
        [{"question": "  ", "answer": "A language."}],
        [{"question": "What is Python?", "answer": "  "}],
    ],
)
def test_load_deck_rejects_invalid_json_structure(tmp_path, capsys, payload):
    deck_file = tmp_path / "invalid_deck.json"
    deck_file.write_text(json.dumps(payload), encoding="utf-8")

    assert load_deck(deck_file) == []
    assert "Error:" in capsys.readouterr().out
