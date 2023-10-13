#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import reverse_string 
from src.question_b.question_b import use_global, global_var 
from src.question_c.question_c import get_assessment_value, get_tax_assessed 
from src.question_d.question_d import get_fahrenheit



#class tests_strings(unittest.TestCase):
class test_config(unittest.TestCase):



    def test_hello_world(self):
        input_string = "Hello, World!"
        result = reverse_string(input_string)
        self.assertEqual(result, "!dlroW ,olleH")

    def test_hello(self):
        input_string = "hello"
        result = reverse_string(input_string)
        self.assertEqual(result, "olleh")








# Global variable to be modified
    global_var = 5

# Function to modify the global variable
    def use_global():
        global global_var
        global_var += 10 


    def test_global_variable_modification(self):
        # Get the initial value of the global variable
        initial_value = global_var

        use_global()
        
        self.assertEqual(global_var, initial_value) 



    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)

    def test_get_tax_assessed(self):
       self.assertEqual(round(get_tax_assessed(6000), 2), 43.20)
       self.assertEqual(round(get_tax_assessed(10000), 2), 72.00)
   


    def test_get_fahrenheit(self):
        self.assertEqual(get_fahrenheit(0), 32)
        self.assertEqual(get_fahrenheit(5), 41)
        self.assertEqual(get_fahrenheit(10), 50)

