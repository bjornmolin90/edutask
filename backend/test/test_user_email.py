import pytest
from unittest.mock import patch, MagicMock
from src.controllers.usercontroller import UserController

@pytest.mark.unit
def test_0_user_valid_email():
    """
    Test-case for not entering an email
    Should return None since the Database can't return any match, but the get_user_by_email function in usercontroller.py isn't written correctly
    """
    user = []
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = user
    sut = UserController(dao=mockedDAO)
    result = sut.get_user_by_email(email="dad@gmail.com")
    assert result == None


@pytest.mark.unit
def test_1_user_valid_email():
    """
    Test case for entering one valid email
    Should return the email
    """
    user = [{'email':'dad@gmail.com'}]
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = user
    sut = UserController(dao=mockedDAO)
    result = sut.get_user_by_email(email="dad@gmail.com")
    assert result == user[0]


@pytest.mark.unit
def test_2_user_valid_email():
    """
    Test-case for entering two valid emails
    Should return the first user email
    """
    user = [{'email':'dad@gmail.com'}, {'email':'dad@gmail.com'}]
    mockedDAO = MagicMock()
    mockedDAO.find.return_value = user
    sut = UserController(dao=mockedDAO)
    result = sut.get_user_by_email(email="dad@gmail.com")
    assert result == user[0]


@pytest.mark.unit
def test_user_invalid_email():
    """
    Test-case for entering an invalid email
    ValueError should be raised
    """
    mockedDAO = MagicMock()
    sut = UserController(dao=mockedDAO)
    with pytest.raises(ValueError):
        sut.get_user_by_email(email='invalid_email')

