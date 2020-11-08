import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff_1(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        test_param = "fdgd"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuuf_3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number.")        
        
    def test_do_stuuf_4(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number.")        

if __name__ == "__main__":
    unittest.main()
