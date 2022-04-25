import unittest
from simulator import Simulator

class Simulator_tests(unittest.TestCase):
    
   
    def setUp(self) -> None:
        self.simulator0 = Simulator(0)
        self.simulator3 = Simulator(3)
        self.simulator8 = Simulator(8)
        self.simulator25 = Simulator(25)
        self.simulator_string = Simulator("Hello")
        self.simulator_float = Simulator(4.3)
        self.simulator_negative = Simulator(-34)

    def test_instance(self):
        self.assertIsInstance(self.simulator0, Simulator, "Failed to create an object of the class Simulator.")

    def test_input_type(self):
        self.assertEqual(self.simulator_string.input, False, "The class accepts non-integers as inputs.")
        self.assertEqual(self.simulator_float.input, False, "The class accepts floats as inputs.")
        self.assertEqual(self.simulator_negative.input, False, "The class accepts negative values as inputs.")

    def test_number_of_open_centers(self):
        self.assertEqual(self.simulator3.get_num_of_open_centers(), 2, "The number of open centers is not correct.")
        self.assertEqual(self.simulator8.get_num_of_open_centers(), 5, "The number of open centers is not correct.")

    def test_number_of_full_centers(self):
        self.assertEqual(self.simulator8.get_num_of_full_centers(), self.simulator8.open_centers.count(100), "The number of full centers is not correct.")
        self.assertEqual(self.simulator25.get_num_of_full_centers(), self.simulator25.open_centers.count(100), "The number of full centers is not correct.")

    def test_number_working_trainees(self):
        self.assertEqual(self.simulator3.get_num_working_trainees(), sum(self.simulator3.open_centers), "The number of trainees currently training is wrong.")
        self.assertEqual(self.simulator8.get_num_working_trainees(), sum(self.simulator8.open_centers), "The number of trainees currently training is wrong.")

    def test_centers_do_not_exceed_maximum_trainees(self):
        for centre in self.simulator8.open_centers:
            self.assertLessEqual(centre, 100, "More than 100 trainees found in a training center.")
        for centre in self.simulator25.open_centers:
            self.assertLessEqual(centre, 100, "More than 100 trainees found in a training center.")

    def test_generate_new_trainees(self):
        for i in range(75):
            self.assertLessEqual(self.simulator3.generate_new_trainees(), 100, "More than 100 trainees generated in a month.")
            self.assertGreaterEqual(self.simulator3.generate_new_trainees(), 50, "Fewer than 50 trainees generated in a month.")

    def test_using_waiting_list(self):
        if self.simulator25.open_centers.count(100) < len(self.simulator25.open_centers):
            self.assertEqual(self.simulator25.num_waiting_list, 0, "Trainees from the waiting list are not being assigned to available centers.") 
        if self.simulator8.open_centers.count(100) < len(self.simulator8.open_centers):
            self.assertEqual(self.simulator8.num_waiting_list, 0, "Trainees from the waiting list are not being assigned to available centers.")

    def test_centers_accept_up_to_50_trainees(self):
        obj_lst = [self.simulator3, self.simulator8, self.simulator25]
        for obj in obj_lst:
            original_lst = obj.open_centers.copy()
            obj.distribute_trainees(1000)
            for i in range(obj.open_centers):
                added_trainees = obj.open_centers[i] - original_lst[i]
                self.assertLessEqual(added_trainees, 50, "More than 50 trainees assigned to a training center.")