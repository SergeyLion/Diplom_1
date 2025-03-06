



class TestBun:

    def test_bun_get_name(self, bun):
        assert bun.get_name() == "test"


    def test_bun_get_price(self, bun):
        assert bun.get_price() == 1000.00
