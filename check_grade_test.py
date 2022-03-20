import pytest
import json
import System
import Staff
import Student
import Professor
import TA

#Test if a student can successfully view course grade
def test_check_grade(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.check_grades('cloud_computing')

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

