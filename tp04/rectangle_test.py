import unittest
from Rectangle import Rectangle

class RectangleTest(unittest.TestCase):

    def test_rectangle_is_created(self):
        r = Rectangle(12,2)
        self.assertIsInstance(r,Rectangle)

    def test_rectangle_is_created_without_parameters(self):
        r = Rectangle()
        self.assertIsInstance(r,Rectangle)
    
    def test_rectangle_is_failed_when_longueur_1(self):
        # r = Rectangle(1,2)
        self.assertRaises(AssertionError,Rectangle,1,1)