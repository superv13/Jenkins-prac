import unittest

from Prog1 import summation
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        test case to add 2 numbers 
        """
        data = [23,56]
        result = summation(data)
        self.assertEqual(result, 79)
if __name__ == '__main__':
    unittest.main()
