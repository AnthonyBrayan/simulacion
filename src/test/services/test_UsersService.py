#Importamos pytes
import pytest

#Importamos Service
from src.services.UsersService import UsersService

@pytest.fixture(scope='session')
def users():
    return UsersService.get_user()

def test_get_user_not_none(users):
    assert users != None

def test_get_user_isinstance_of_list(users):
    assert isinstance(users,list)

# def test_get_user_has_elements(users):
#     assert len(users) > 0

