



class TestIngredient:

    def test_ingredient_get_type(self, ingredient):
        assert ingredient.get_type() == "SAUCE"

    def test_ingredient_get_name(self, ingredient):
        assert ingredient.get_name() == "Гагаринский"

    def test_ingredient_get_price(self, ingredient):
        assert ingredient.get_price() == 500.00