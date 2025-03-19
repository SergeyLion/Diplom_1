from unittest.mock import Mock
import pytest
from burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun ):
        # Создаем объект бургер
        burger = Burger()
        # Устанавливаем булочку в бургер
        burger.set_buns(mock_bun)
        # Проверяем, что булочка установлена корректно
        assert burger.bun == mock_bun
        assert burger.bun.get_name() == "Белая"
        assert burger.bun.get_price() == 55.00

    def test_add_ingredient(self, mock_ingredient):
        #Создаем объект бургер
        burger = Burger()
        #Добавляем ингредиент
        burger.add_ingredient(mock_ingredient)
        #Проверяем, что ингредиент добавлен корректно
        assert burger.ingredients == [mock_ingredient]
        assert burger.ingredients[0].get_name() == "Тульский"
        assert burger.ingredients[0].get_type() == "SAUCE"
        assert burger.ingredients[0].get_price() == 100.00

    def test_remove_ingredient(self):
        # Создаем мок-объекты для ингредиентов
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()
        # Создаем объект бургер
        burger = Burger()
        # Добавляем мок-ингредиенты в бургер
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        assert len(burger.ingredients) == 3
        #Удаляем 2 ингредиент
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients == [mock_ingredient1, mock_ingredient3]

    def test_move_move_ingredient(self):
        # Создаем мок-объекты для ингредиентов
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()
        # Создаем объект бургер
        burger = Burger()
        # Добавляем мок-ингредиенты в бургер
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        assert len(burger.ingredients) == 3
        assert burger.ingredients == [mock_ingredient1, mock_ingredient2, mock_ingredient3]
        #Меняем индекс у третьего ингредиента на первый
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mock_ingredient3, mock_ingredient1, mock_ingredient2]

    def test_get_price(self, mock_bun):
        # Создаем мок-объекты для ингредиентов и булочки
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient1.get_price.return_value = 100.00
        mock_ingredient2.get_price.return_value = 123.00
        # Создаем объект бургер
        burger = Burger()
        # Добавляем мок-ингредиенты в бургер
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.set_buns(mock_bun)
        assert burger.get_price() == 333.00

    # Параметризация тестовых случаев
    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredients_data, expected_receipt",
        [
            # Тест 1: Один ингредиент
            (
                    "Белая булочка",  # Название булочки
                    100.0,  # Цена булочки
                    [("Соус", "Кетчуп", 50.0)],  # Список ингредиентов (тип, название, цена)
                    # Ожидаемый чек
                    "(==== Белая булочка ====)\n"
                    "= соус Кетчуп =\n"
                    "(==== Белая булочка ====)\n"
                    "\n"
                    "Price: 250.0"
            ),
            # Тест 2: Несколько ингредиентов
            (
                    "Черная булочка",  # Название булочки
                    150.0,  # Цена булочки
                    [("Начинка", "Котлета", 200.0), ("Соус", "Горчица", 30.0)],  # Список ингредиентов
                    # Ожидаемый чек
                    "(==== Черная булочка ====)\n"
                    "= начинка Котлета =\n"
                    "= соус Горчица =\n"
                    "(==== Черная булочка ====)\n"
                    "\n"
                    "Price: 530.0"
            ),
            # Тест 3: Без ингредиентов
            (
                    "Сэндвич булочка",  # Название булочки
                    80.0,  # Цена булочки
                    [],  # Пустой список ингредиентов
                    # Ожидаемый чек
                    "(==== Сэндвич булочка ====)\n"
                    "(==== Сэндвич булочка ====)\n"
                    "\n"
                    "Price: 160.0"
            ),
        ]
    )
    def test_get_receipt(self, bun_name, bun_price, ingredients_data, expected_receipt):
        # Создаем мок для булочки
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        # Создаем моки для ингредиентов
        mock_ingredients = []
        for ingredient_type, ingredient_name, ingredient_price in ingredients_data:
            mock_ingredient = Mock()
            mock_ingredient.get_type.return_value = ingredient_type
            mock_ingredient.get_name.return_value = ingredient_name
            mock_ingredient.get_price.return_value = ingredient_price
            mock_ingredients.append(mock_ingredient)

        # Создаем объект бургера
        burger = Burger()
        burger.set_buns(mock_bun)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)

        # Вызываем метод get_receipt и проверяем результат
        receipt = burger.get_receipt()
        assert receipt == expected_receipt

