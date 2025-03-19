


class TestDatabase:

    def test_database_return_len_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_buns_returns_correct_list(self, database):
        buns = database.available_buns()
        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]
        for bun_list, (expected_name, expected_price) in zip(buns, expected_buns):
            assert bun_list.name == expected_name
            assert bun_list.price == expected_price

    def test_available_ingredients_returns_correct_lust(self, database):
        ingredients = database.available_ingredients()
        expected_ingredients = [
            ("hot sauce", 100),
            ("sour cream", 200),
            ("chili sauce", 300),
            ("cutlet", 100),
            ("dinosaur", 200),
            ("sausage",300)
        ]
        for ingredient_list, (expected_name, expected_price) in zip(ingredients, expected_ingredients):
            assert ingredient_list.name == expected_name
            assert ingredient_list.price == expected_price
