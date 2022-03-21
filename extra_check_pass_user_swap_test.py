import pytest
import System
import Student
import TA
import Professor
import json

#Checks if a valid password within the system can be used with a valid username it does not belong to 
def test_pass_w_user_swap(grading_system):

    #Valid TA's username
    usernameta = 'cmhbf5'
    #Valid password of a user 'calyam' with role 'professor'
    passwordprof = '#yeet'
    #If this returns True then a user can login with someone else's password
    assert grading_system.check_password(usernameta,passwordprof)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

