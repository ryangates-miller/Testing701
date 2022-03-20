import pytest
import json
import System
import Professor
import TA
import Student

#This checks to see if a student can view assignments for a course
#The view_assignment() function will always return a false positive
#because the code take any parameter and returns the assignments
#for 'comp_sci'
def test_view_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.view_assignments('this_is_not_a_course')
    #This assertion returns an error because user hdjsr7 is not taking 'this_is_not_a_course
    #but the function above accepted it as a course parameter
    assert "this_is_not_a_course" in grading_system.users['hdjsr7']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
