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

def test_dao_invalid_property_type(sut):
    data = {"name" : 1}
    with pytest.raises(WriteError):
        sut.create(data)
    sut.drop()

""" class Test_DAO():
    @pytest.fixture
    @patch('src.util.dao.getValidator', autospec=True)
    def sut(self, mockedValidator):
        mockedValidator.return_value = {"$jsonSchema": {
            "bsonType": "object",
            "required": ["name"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "the first name of a user must be determined",
                }}}
        }
        yield DAO("test")

    def test_dao_valid_document(self, sut):
        valid_doc = sut
        valid_doc.create({"name" : "Namn"})
        assert valid_doc["name"] == "Namn"

    def test_dao_invalid_property_type(self, sut):
        with pytest.raises(WriteError):
            sut.create({"name" : 1})

    def test_dao_invalid_document(self, sut):
        with pytest.raises(WriteError):
            sut.create({"missing_name" : "Namn"}) """


    

""" @pytest.fixture
def create_user(sut):
    data = {"name" : "Namn"}
    returned_doc = sut.create(data)
    yield returned_doc
    sut.drop()



def test_dao_valid_document(create_user):
    test = sut.create(data)
    assert test["name"] == "Namn"

def test_dao_invalid_property_type(sut):
    data = {"name" : 1}
    with pytest.raises(WriteError):
        sut.create(data)

def test_dao_invalid_document(sut):
    data = {"missing_name" : "Namn"}
    with pytest.raises(WriteError):
        sut.create(data) """


