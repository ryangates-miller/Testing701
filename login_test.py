import pytest
import System
import Student
import TA
import Professor

#Tests if the program correctly logs in with valid credentials
#and assigns correct user data when logging in
def test_login(grading_system):
    usernameta = 'cmhbf5'
    passwordta = 'bestTA'
    grading_system.login(usernameta,passwordta)
    assert isinstance( grading_system.usr,TA.TA) == True
    usernameprof ='goggins'
    passwordprof = 'augurrox'
    grading_system.login(usernameprof,passwordprof)
    assert isinstance( grading_system.usr, Professor.Professor) == True
    usernamestud ='hdjsr7'
    passwordstud = 'pass1234'
    grading_system.login(usernamestud,passwordstud)
    assert isinstance( grading_system.usr, Student.Student) == True



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

