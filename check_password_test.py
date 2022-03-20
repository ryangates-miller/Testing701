import pytest
import System
import Student
import TA
import Professor
import json

#Checks if passwords are the same, should return false with whitespace or different capitalization
def test_pass(grading_system):
    usernameta1 = 'cmhbf5'
    passwordta1 = 'bestTA'
    assert grading_system.check_password(usernameta1,passwordta1) == True
    usernameta2 = 'cmhbf5'
    passwordta2 = 'BESTTA'
    assert grading_system.check_password(usernameta2,passwordta2) == False
    usernameta3 = 'cmhbf5'
    passwordta3 = ' BESTTA'
    assert grading_system.check_password(usernameta3,passwordta3) == False
    usernameprof = 'calyam'
    passwordprof = '#yeet'
    assert grading_system.check_password(usernameprof,passwordprof) == True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

