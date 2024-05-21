# Solve Math questions and get points
#### Video Demo:  [https://youtu.be/CLG3mfti2T4]
#### Description:
This project is a fun and interactive game that challenges users with random arithmetic questions. The user is expected to provide answers rounded to the nearest whole number. The game keeps track of the user's score and saves the details of each question and answer to a file. It also includes a feature to greet the user and maintain a personalized score history.
##### Features
Random Arithmetic Questions: The game generates random arithmetic questions using various operators such as addition, subtraction, multiplication, division, and exponentiation.
User Interaction: The user is prompted to answer the questions, and the game provides feedback based on the correctness of the answer.
Score Tracking: The game keeps track of the user's score and saves it along with the questions and answers to a file.
Personalized Experience: The game greets the user by name and maintains a personalized score history.
Error Handling: The game handles errors gracefully, such as invalid input or division by zero.
##### Installation
To install the necessary dependencies, run:
```
bash
pip install cowsay
```
##### Usage
To start the game, run the following command:
```
bash
python project.py
```

##### Example
```
python
What's your name? John
 _______________
< WELCOME, John >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Question: 3+5*2-1
Answer: 12
Well Done!
Press 'Y' to continue: y
Question: 4**2/2+3
Answer: 11
Better luck next time :)
Press 'Y' to continue: n
```
##### Project Structure
project.py: The main script that runs the game.
user_score.txt: A file that stores the user's score and the questions and answers.
##### Functions
###### main()
The main function that initializes the game, greets the user, and manages the game loop.
###### get_user_score(player)
Retrieves the user's score from the user_score.txt file. If the user is not found, it returns False.
update_user_points(new_user, user_name, score)
Updates the user's score in the user_score.txt file. If the user is new, it adds a new entry.
###### math_question()
Generates a random arithmetic question and returns the question string and the correct answer.
###### user_interaction(question, answer, score)
Handles the user interaction for answering a question. It updates the score based on the correctness of the answer.
###### Testing
The project includes unit tests to ensure the correctness of the functions. The tests are written using pytest and can be found in the test_project.py file.
Running Tests
To run the tests, use the following command:
```
bash
pytest test_project.py
```

###### Test Cases
test_user_registered: Tests if the user is registered and retrieves the correct score.
test_update_points: Tests the functionality of updating user points for both new and existing users.
test_user_answer: Tests the user interaction function with both correct and incorrect answers.
Example Test Code
```
python
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
```
#### Conclusion
This project is a simple yet engaging way to practice arithmetic skills while keeping track of progress. The personalized experience and score tracking make it a fun and motivating game for users of all ages.
