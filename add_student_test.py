import pytest
import json
import System
import Staff
import Student
import Professor
import TA

#Test if a professor can successfully add a student to a class
def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('yted91', 'databases')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

