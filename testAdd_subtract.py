import unittest

from add_subtract import add, subtract

class TestAddSubtract(unittest.TestCase):
    """Class to test add and subtract functions"""
    def test_add_funtion(self):
        """Tests that the add function works as expected"""
        self.assertEqual(add(1,2), 3)
    
    def test_subtract_function(self):
        """Tests that the subtract function works as expected"""
        self.assertEqual(subtract(3,1), 2)


    def test_TypeError_is_raised(self):
        with self.assertRaises(TypeError):
            add(2.3, 'girl')
            subtract([2, 5],4)


if __name__ == '__main__':
    unittest.main(exit = False)
