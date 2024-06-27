import unittest
from calculator import TaxCalculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.tax_bracket = {
                        10: '0-9700', 
                        12: '9700-39475', 
                        22: '39475-84200', 
                        24: '84200-160725',
                        32: '160725-204100', 
                        35: '204100-510300',
                        37: '510300-1e15'
                    }

        self.cal = TaxCalculator(self.tax_bracket)

    # BaseClass tests
    def test_low_bracket(self):
        res = self.cal.run(9000)
        etr = res['summary']['effective_tax_rate']
        tax = res['summary']['tax_owed']
        self.assertEqual(etr, 10.0)
        self.assertEqual(tax, 900)

    def test_high_bracket(self):
        res = self.cal.run(9000000)
        etr = res['summary']['effective_tax_rate']
        tax = res['summary']['tax_owed']
        self.assertEqual(etr, 36.61)
        self.assertEqual(tax, 3294988)

if __name__ == '__main__':
    unittest.main()