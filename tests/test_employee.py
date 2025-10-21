from employee import Employee

def test_give_default_raise():
    arbejder = Employee('emil','bartels', 50000)
    arbejder.give_raise()
    assert arbejder.salary == 55000 

def test_give_custom_raise():
    arbejder_jonas = Employee('jonas', 'vindahl', 600000, 8888)
    arbejder_jonas.give_raise()
    assert arbejder_jonas.salary == 608888