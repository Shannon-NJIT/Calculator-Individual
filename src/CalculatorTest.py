import unittest
from Calculator import Calculator
from CSVreader import csvreader
from pprint import pprint


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        addition_list = csvreader('src/UnitTestAddition.csv').data
        for row in addition_list:
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            #pprint(addition_list)

    def test_subtraction(self):
        subtraction_list = csvreader('src/UnitTestSubtraction.csv').data
        pprint(subtraction_list)
        for row in subtraction_list:
            self.assertEqual(self.calculator.subtraction(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            #pprint(subtraction_list)

    def test_multiplication(self):
        multiplication_list = csvreader('src/UnitTestMultiplication.csv').data
        for row in multiplication_list:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            #pprint(multiplication_list)

    def test_square(self):
        square_list = csvreader('src/UnitTestSquare.csv').data
        for row in square_list:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            #pprint(square_list)

    def test_division(self):
        division_list = csvreader('src/UnitTestDivision.csv').data
        for row in division_list:
            self.assertAlmostEqual(self.calculator.division(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
            pprint(division_list)


if __name__ == '__main__':
    unittest.main()
