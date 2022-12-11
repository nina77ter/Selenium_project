
import pytest


@pytest.fixture(scope='module')
def greet():
    print("\n----------------- SetUp ----------------")
    print('Helloooo Test Master!')
    yield [2,3,4]
    print("\n------------------ TearDown ------------")
    print("fixture steps are completed here.")