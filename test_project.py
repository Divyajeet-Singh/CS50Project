import pytest
from unittest.mock import patch
from project import get_user_score, update_user_points, user_interaction, math_question


def test_user_registered():
    assert get_user_score("Kus") == False
    assert get_user_score("Ann") == "100"


def test_update_points():
    assert update_user_points(True, "Kus", 0) == "Points Updated for New User"
    assert update_user_points(False, "Ann", 100) == "Points Updated for Existing User"


def test_user_answer():
    question, result = math_question()

    # Test with the correct answer
    with patch("builtins.input", return_value=str(result)):
        score = user_interaction(question, result, 100)
        assert score == "101"  # score should be incremented

    # Test with an incorrect answer
    with patch("builtins.input", return_value=str(6743678)):
        score = user_interaction(question, result, 100)
        assert str(score) == "100"  # score should remain the same
