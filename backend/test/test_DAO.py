import pytest
from unittest.mock import patch, MagicMock
from src.util.dao import DAO
from pymongo.errors import WriteError

@pytest.fixture
@patch('src.util.dao.getValidator', autospec=True)
def sut(mockedValidator):
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

def test_dao_valid_document(sut):
    data = {"name" : "Namn"}
    returned_doc = sut.create(data)
    assert returned_doc["name"] == "Namn"

def test_dao_invalid_document_and_clear_collection(sut):
    data = {"missing_name" : "Namn"}
    with pytest.raises(WriteError):
        sut.create(data)
    sut.drop()
