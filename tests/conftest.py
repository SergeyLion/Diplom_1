import pytest
from bun import Bun
from database import Database
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


@pytest.fixture
def bun():
    bun = Bun("test", 1000.00)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Гагаринский", 500.00)
    return ingredient

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Белая"
    mock_bun.get_price.return_value = 55.00
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = 100.00
    mock_ingredient.get_name.return_value = "Тульский"
    mock_ingredient.get_type.return_value = "SAUCE"
    return mock_ingredient