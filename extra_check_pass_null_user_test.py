import pytest
import System
import Student
import TA
import Professor
import json

#Checks if a valid password can be returned to a null user field
def test_pass_null_user(grading_system):

    #Null in python is None
    username = None
    #Valid password of a user 'calyam' with role 'professor'
    passwordprof = '#yeet'
    #If this returns True then a user can find valid passwords if the username
    #field is left blank
    assert grading_system.check_password(username,passwordprof)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

