import unittest
from context import btc2fiat

class TestBTCMethods(unittest.TestCase):

    def test_coindesk(self):
        price = btc2fiat.get_coindesk(0.3, '2018-10-08')
        self.assertAlmostEqual(price, 1986.72039)

    def test_coinmarketcap(self):
        price = btc2fiat.get_coinmarketcap(0.3, '2018-10-08')
        self.assertAlmostEqual(price, 1995.669)

    def test_offline(self):
        price = btc2fiat.get_offline(0.3, '2018-10-08')
        self.assertAlmostEqual(price, 1981.425)

    def test_value(self):
        price = btc2fiat.get_value(0.3, '2018-10-08')
        self.assertAlmostEqual(price, 1986.72039)

if __name__ == '__main__':
    unittest.main()