import pytest
import json
import System
import Staff
import Student
import Professor
import TA

#Test if a student can successfully submit an assignment
def test_submit(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','untitled_assignment', '03/01/20')
    assert "assignment1" in grading_system.users['hdjsr7']['courses']['cloud_computing'] 
    assert "untitled_assignment" in grading_system.users['hdjsr7']['courses']['cloud_computing']['assignment1']['submission']
    assert "03/01/20" in grading_system.users['hdjsr7']['courses']['cloud_computing']['assignment1']['submission_date']


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

