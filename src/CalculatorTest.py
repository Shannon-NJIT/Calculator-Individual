import unittest
from Calculator import Calculator
from CSVreader import CsvReader
from pprint import pprint


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        addition_list = CsvReader('src/UnitTestAddition.csv').data
        for row in addition_list:
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        # pprint(addition_list)

    def test_subtraction(self):
        subtraction_list = CsvReader('src/UnitTestSubtraction.csv').data
        for row in subtraction_list:
            self.assertEqual(self.calculator.subtraction(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        # pprint(subtraction_list)

    def test_multiplication(self):
        multiplication_list = CsvReader('src/UnitTestMultiplication.csv').data
        for row in multiplication_list:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        # pprint(multiplication_list)

    def test_square(self):
        square_list = CsvReader('src/UnitTestSquare.csv').data
        for row in square_list:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        # pprint(square_list)

    def test_division(self):
        division_list = CsvReader('src/UnitTestDivision.csv').data
        for row in division_list:
            self.assertAlmostEqual(self.calculator.division(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
        # pprint(division_list)

    def test_sqrt(self):
        sqrt_list = CsvReader('src/UnitTestSquareRoot.csv').data
        for row in sqrt_list:
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
        pprint(sqrt_list)


if __name__ == '__main__':
    unittest.main()
