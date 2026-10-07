import unittest
from decimal import Decimal

from app.calculator import calculate, format_result


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate("10", "+", "5"), Decimal("15"))

    def test_subtract(self):
        self.assertEqual(calculate("10", "-", "5"), Decimal("5"))

    def test_multiply(self):
        self.assertEqual(calculate("10", "*", "5"), Decimal("50"))

    def test_divide(self):
        self.assertEqual(calculate("10", "/", "5"), Decimal("2"))

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "division by zero"):
            calculate("10", "/", "0")

    def test_unsupported_operation(self):
        with self.assertRaisesRegex(ValueError, "unsupported operation"):
            calculate("10", "%", "5")

    def test_format_result_removes_trailing_zeros(self):
        self.assertEqual(format_result(Decimal("15.000")), "15")


if __name__ == "__main__":
    unittest.main()
