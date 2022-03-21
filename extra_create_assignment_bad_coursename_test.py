import pytest
import System
import Student
import TA
import Professor
import Staff

#Tests if the program allows for a TA to creat an assignment with a 
#fake course name
def test_create_assignment_bad_course(grading_system):
    usernameta = 'cmhbf5'
    passwordta = 'bestTA'
    grading_system.login(usernameta,passwordta)
    grading_system.usr.create_assignment('assignment4', '04/20/69', 'this_is_not_a_course')
    assert grading_system.courses['this_is_not_a_course']['assignments']['assignment4']['due_date'] == '04/20/69' 


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

