import pytest

print('start the sample test scenario')
def test_greet_user():
    print('hello user!')
    assert 'hello' == 'hello'

def test_scenario1():
    print('scenario 1 started..')
    assert 2 == 3, 'scenario failed'
