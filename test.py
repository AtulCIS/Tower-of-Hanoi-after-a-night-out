import unittest
from main import app
from main.routes import TowerOfHanoi


class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.assertEqual(app.debug, False)

    def test_exp_one(self):
        """E(2,5,1,3,5) it should be 60"""
        toh = TowerOfHanoi()
        self.assertEqual(toh.get_square_travelled(2, 5, 1, 3, 5), 60)

    def test_exp_two(self):
        """E(3,20,4,9,17) it should be 2358"""
        toh = TowerOfHanoi()
        self.assertEqual(toh.get_square_travelled(3, 20, 4, 9, 17), 2358)

    def test_with_empty_param(self):
        """ it has to return an error since one param is missing """
        toh = TowerOfHanoi()
        self.assertEqual(toh.get_square_travelled("", 20, 4, 9, 17), 2358)

    def test_with_float(self):
        """ it has to return an error since one param is float """
        toh = TowerOfHanoi()
        self.assertEqual(toh.get_square_travelled(3.5, 20, 4, 9, 17), 2358)


if __name__ == "__main__":
    unittest.main()
