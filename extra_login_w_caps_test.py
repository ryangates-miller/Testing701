import pytest
import System
import Student
import TA
import Professor

#Tests if the program allows people to login with correct 
#usernames if there are capital letters
def test_login_w_caps(grading_system):
    username = 'Cmhbf5'
    password = 'bestTA'
    grading_system.login(username,password)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

