import unittest
from <class> import <file>

class Simulator_tests(unittest.TestCase):
    
   
    def setUp(self) -> None:
        self.simulator0 = Simulator(0)
        self.simulator3 = Simulator(3)
        self.simulator8 = Simulator(8)
        self.simulator_string = Simulator("Hey, how you doing?)


    def test_instance(self):
        self.assertIsInstance(self.simulator0, Simulator, "This object is not an instance of a Simulator")

    def test_input_null(self):
        self.assertEqual(self.simulator_string.input, False, "The class accepts non-integers as inputs")

    def test_number_of_open_centers(self):
        self.assertEqual(self.simulator3.get_num_of_open_centers(), 2, "The number of open centers is not correct")
        self.assertEqual(self.simulator8.get_num_of_open_centers(), 5, "The number of open centres is not correct.")

    def test_centres_do_not_exceed_maximum_trainees(self):
        for centre in self.simulator3.open_centers.values():
            self.assertLessEqual(centre, 100, "At least one test has more than 100 trainees")
        for centre in self.simulator8.open_centers.values():
            self.assertLessEqual(centre, 100, "At least one test has more than 100 trainees")