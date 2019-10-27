import unittest, csv
from Calculator import Calculator



class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)



if __name__ == '__main__':
    unittest.main()
