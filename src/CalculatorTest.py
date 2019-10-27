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
            pprint(addition_list)


if __name__ == '__main__':
    unittest.main()
