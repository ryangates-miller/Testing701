import pytest
import System
import Student
import TA
import Professor

#Tests if the program allows people to login with correct 
#usernames if there is white space
def test_login_w_white_space(grading_system):
    username = ' cmhbf5 '
    password = 'bestTA'
    grading_system.login(username,password)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
