import unittest
import calc

# create test class,inherit from unittest.testcase
class TestCalc(unittest.TestCase):

# Write TestMethod
    def test_add(self):
        result = calc.add(10, 5) 
        self.assertEqual(result, 15)

# To run the code in the editor directly. 
if __name__ == ' __main__ ':
    unittest.main()