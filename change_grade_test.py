import pytest
import System
import Student
import TA
import Professor
import Staff

#Tests if the program correctly updates the grade for a specified student
#and changes the database
def test_grade_change(grading_system):
    usernameta = 'cmhbf5'
    passwordta = 'bestTA'
    grading_system.login(usernameta,passwordta)
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 100)
    assert grading_system.users['yted91']['courses']['software_engineering']['assignment1']['grade'] == 100
    


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

