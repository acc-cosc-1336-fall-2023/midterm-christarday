#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

      def test_reverse_string_hello(self):
        self.assertEqual(reverse_string("hello"), "olleh")
       



if __name__ == '__main__':
    unittest.main()
