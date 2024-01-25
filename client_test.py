import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    """Class to perform unit test on methods in client3 module"""

    def test_getdatapoint_calculateprice(self):
        """"Unit test for getDataPoint method in client3.py"""
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            self.assertEqual(getDataPoint(
                quote), (quote['stock'], quote['top_bid']['price'], (quote['top_ask']['price']+quote['top_bid']['price'])/2))

    def test_getdatapoint_calculatepricebidgreaterthanask(self):
        """"Unit test for getDataPoint method in client3.py"""
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            self.assertEqual(getDataPoint(
                quote), (quote['stock'], quote['top_bid']['price'], (quote['top_ask']['price']+quote['top_bid']['price'])/2))

    def test_get_ration(self):
        """Tests the ratio calculation function in getDataPoint()"""
        price_a = 1
        price_b = 2
        self.assertEqual(getRatio(price_a=price_a, price_b=price_b), 1/2)


if __name__ == '__main__':
    unittest.main()
