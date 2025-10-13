from unittest.mock import MagicMock
import pytest
from src.burger import Burger


@pytest.fixture
def mock_bun():
    bun_mock = MagicMock()
    bun_mock.get_name.return_value = "Blue bun"
    bun_mock.get_price.return_value = 400
    return bun_mock

@pytest.fixture
def mock_cheese():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 40
    ingredient.get_name.return_value = "Cheese"
    ingredient.get_type.return_value = "FILLING"
    return ingredient

@pytest.fixture
def mock_jalapeno():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 30
    ingredient.get_name.return_value = "Jalapeno"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient

@pytest.fixture
def burger_with_ingredient(mock_cheese):
    burger = Burger()
    burger.add_ingredient(mock_cheese)
    return burger

@pytest.fixture
def burger_with_two_ingredients(mock_cheese, mock_jalapeno):
    burger = Burger()
    burger.add_ingredient(mock_cheese)
    burger.add_ingredient(mock_jalapeno)
    return burger