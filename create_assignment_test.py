import pytest
import System
import Student
import TA
import Professor
import Staff

#Tests if the program correctly updates the grade for a specified student
#and changes the database
def test_create_assignment(grading_system):
    usernameta = 'cmhbf5'
    passwordta = 'bestTA'
    grading_system.login(usernameta,passwordta)
    grading_system.usr.create_assignment('assignment4', '04/20/69', 'cloud_computing')
    assert grading_system.courses['cloud_computing']['assignments']['assignment4']['due_date'] == '04/20/69' 


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


