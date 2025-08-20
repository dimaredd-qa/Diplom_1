import pytest
from src.burger import Burger
from unittest.mock import MagicMock
from data.data import Order

class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
        assert burger.bun.get_name() == "Blue bun"
        assert burger.bun.get_price() == 400

    def test_add_ingredient(self, mock_cheese):
        burger = Burger()
        burger.add_ingredient(mock_cheese)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_price() == 40
        assert burger.ingredients[0].get_name() == "Cheese"
        assert burger.ingredients[0].get_type() == "FILLING"

    def test_remove_ingredient(self, burger_with_ingredient):
        burger_with_ingredient.remove_ingredient(0)
        assert burger_with_ingredient.ingredients ==[]

    def test_remove_from_empty_burger(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_remove_invalid_index(self, burger_with_ingredient):
        with pytest.raises(IndexError):
            burger_with_ingredient.remove_ingredient(1)
        assert burger_with_ingredient.ingredients[0].get_name() == "Cheese"

    def test_move_ingredient(self, burger_with_two_ingredients, mock_cheese, mock_jalapeno):
        burger_with_two_ingredients.move_ingredient(0, 1)
        assert burger_with_two_ingredients.ingredients == [mock_jalapeno, mock_cheese]

    @pytest.mark.parametrize("ingredients,expected_price", Order.ingredient_order)
    def test_get_price_parametrized(self, mock_bun, ingredients, expected_price):
        burger = Burger()
        burger.set_buns(mock_bun)
        for ingredient_type, name, price in ingredients:
            ingredient = MagicMock()
            ingredient.get_name.return_value = name
            ingredient.get_type.return_value = ingredient_type
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_cheese):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_cheese)
        expected = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_cheese.get_type().lower()} {mock_cheese.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n"
            f"\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected