import pytest
from unittest.mock import patch, MagicMock
from src.controllers.usercontroller import UserController

def test_0_user_valid_email():
    user = []
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = user
    sut = UserController(dao=mockedDAO)
    result = sut.get_user_by_email(email="dad@gmail.com")
    assert result == None

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


def test_user_invalid_email():
    mockedDAO = MagicMock()
    sut = UserController(dao=mockedDAO)
    with pytest.raises(ValueError):
        sut.get_user_by_email(email='invalid_email')

