from utils import load_quiz_history, save_quiz_result


def test_quiz_history_round_trip_uses_requested_path(tmp_path):
    history_file = tmp_path / "history.json"

    save_quiz_result("Python Basics", 4, 5, 12.4, history_file)

    history = load_quiz_history(history_file)
    assert len(history) == 1
    assert history[0]["topic"] == "Python Basics"
    assert history[0]["score"] == "4/5"
    assert history[0]["accuracy_percent"] == 80.0
