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
            result = int(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
        # pprint(addition_list)

    def test_subtraction(self):
        subtraction_list = CsvReader('src/UnitTestSubtraction.csv').data
        for row in subtraction_list:
            result = int(row['Result'])
            self.assertEqual(self.calculator.subtraction(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)
        # pprint(subtraction_list)

    def test_multiplication(self):
        multiplication_list = CsvReader('src/UnitTestMultiplication.csv').data
        for row in multiplication_list:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
        # pprint(multiplication_list)

    def test_square(self):
        square_list = CsvReader('src/UnitTestSquare.csv').data
        for row in square_list:
            result = int(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)
        # pprint(square_list)

    def test_division(self):
        division_list = CsvReader('src/UnitTestDivision.csv').data
        for row in division_list:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.division(row['Value 2'], row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)
        # pprint(division_list)

    def test_sqrt(self):
        sqrt_list = CsvReader('src/UnitTestSquareRoot.csv').data
        for row in sqrt_list:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)
        pprint(sqrt_list)


if __name__ == '__main__':
    unittest.main()
