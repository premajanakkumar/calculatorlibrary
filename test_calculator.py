import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subsract(4, 2)

    def test_multiply(self):
        assert 8 == calculator.multiply(4, 2)

    def test_divide(self):
        assert 2 == calculator.divide(4, 2)
