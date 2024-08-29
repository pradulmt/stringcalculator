from stringcalculator import add


class TestCalculator:
    def test_empty_string(self):
        assert add("") == 0

    def test_length1(self):
        assert add("1") == 1

    def test_length2(self):
        assert add("1,5") == 6

    def test_long_string(self):
        assert add("1,2,3,4,5,6,7,8,9,10") == 55

    def test_newline_split(self):
        assert add("1\n2,3") == 6

    def test_different_delimiters1(self):
        assert add("//;\n1;2") == 3

    def test_different_delimiters2(self):
        assert add("//#\n7#7#7") == 21
