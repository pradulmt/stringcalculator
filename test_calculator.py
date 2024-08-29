from stringcalculator import add


class TestCalculator:
    def test_empty_string(self):
        assert add("") == 0

    def test_length1(self):
        assert add("1") == 1

    def test_length2(self):
        assert add("1,5") == 6