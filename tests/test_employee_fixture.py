from employee import Employee
import pytest

@pytest.fixture
def arbejder():
    """En Employee instance der hedder arbejder"""
    arbejder = Employee('emil', 'bartels', 50000)
    return arbejder

    
def test_give_default_raise(arbejder):
    """Test der tjekker for en default raise på 5000"""
    arbejder.give_raise()
    assert arbejder.salary == 55000 

def test_give_custom_raise(arbejder):
    """Test der tjekker for en raise på custom value på 8888"""
    arbejder.salaryraise = 8888
    arbejder.give_raise()
    assert arbejder.salary == 58888