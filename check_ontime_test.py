import pytest
import System
import Student
import TA
import Professor

#Test if a student can successfully check if an assignment was turned in on time
#This will return false positives if something is actually late
# the Student check_ontime(self,submission_date,due_date): always returns true
def test_checkOntime(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    #You can see the submission date is twelve days late but the function still returns true
    assert (grading_system.usr.check_ontime('1/22/22', '1/10/22')) == False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

