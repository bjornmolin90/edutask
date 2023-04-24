import pytest
from unittest.mock import patch, MagicMock
from src.util.dao import DAO
from pymongo.errors import WriteError

@pytest.fixture
@pytest.mark.integration
@patch('src.util.dao.getValidator', autospec=True)
def sut(mockedValidator):
    """
    Returns a dict in the format of a MongoDB collection validator
    """
    mockedValidator.return_value = {"$jsonSchema": {
        "bsonType": "object",
        "required": ["name"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "the first name of a user must be determined",
            }}}
    }
    sut = DAO("test")
    return sut


@pytest.mark.integration
def test_dao_valid_document(sut):
    """
    Test-case for a valid collection validator
    """
    data = {"name" : "Namn"}
    returned_doc = sut.create(data)
    assert returned_doc["name"] == "Namn"


@pytest.mark.integration
def test_dao_invalid_document_and_clear_collection(sut):
    """
    Test-case for mismatch on the required validator name
    Should return WriteError
    """
    data = {"missing_name" : "Namn"}
    with pytest.raises(WriteError):
        sut.create(data)


@pytest.mark.integration
def test_dao_int_validator(sut):
    """
    Test-case for mismatch on the required bsonType, using INT instead of STR
    Should return WriteError
    """
    data = {"name" : 1}
    with pytest.raises(WriteError):
        sut.create(data)
    sut.drop()