import pytest
from unittest.mock import patch, MagicMock
from src.controllers.usercontroller import UserController

"""
@pytest.mark.demo
def test_user_valid_email():
    user = {'email': 'jane.doe'}
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = [user]
    uc = UserController(dao=mockedDAO)
    with patch("re.fullmatch") as mockfullmatch:
        mockfullmatch.return_value = user

        result = uc.get_user_by_email(email="jane.doe")

        assert result == user
"""
def test_user_invalid_email():
    mockedDAO = MagicMock()
    mockedDAO.get.return_value = {'email':'invalid_email'}
    sut = UserController(dao=mockedDAO)
    with pytest.raises(ValueError):
        sut.get_user_by_email(email='invalid_email')      

"""
def test_multiple_email():
    user1 = {'email': 'jane.doe'}
    user2 = {'email': 'jane.doe'}
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = [user1, user2]
    uc = UserController(dao=mockedDAO)
    with patch("re.fullmatch") as mockfullmatch:
        mockfullmatch.return_value = user1

        result = uc.get_user_by_email(email="jane.doe")

        assert result == user1
"""
def test_1_user_valid_email():
    user = [{'email':'dad@gmail.com'}]
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = user
    sut = UserController(dao=mockedDAO)
    result = sut.get_user_by_email(email="dad@gmail.com")
    assert result == user[0]


def test_2_user_valid_email():
    user = [{'email':'dad@gmail.com'}, {'email':'dad@gmail.com'}]
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = user
    sut = UserController(dao=mockedDAO)
    result = sut.get_user_by_email(email="dad@gmail.com")
    assert result == user[0]

def test_0_user_valid_email():
    user = []
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = user
    sut = UserController(dao=mockedDAO)
    result = sut.get_user_by_email(email="dad@gmail.com")
    assert result == None