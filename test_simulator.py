# get_num_of_open_centers()
# get_num_of_full_centers()
# get_num_working_trainees()
# get_num_waiting_list()


# generate_new_trainees()
# distribute_trainees()

# open_centers - list
# num_waiting_list - integer


# from tkinter import *
import unittest
import random
from simulator import Simulator
# from Single-tab-interface import SimulationInterface
random.seed(53)

class Simulator_tests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.simulator0 = Simulator("0")
        self.simulator1 = Simulator("1")
        self.simulator3 = Simulator("3")
        self.simulator8 = Simulator("8")
        self.simulator25 = Simulator("25")
        self.simulator_string = Simulator("Hello")
        self.simulator_float = Simulator("4.3")
        self.simulator_negative = Simulator("-34")
        # self.simulation_interface = SimulationInterface()
        # self.simulation_interface.create_window()
        random.seed(102)
        self.simulator101 = Simulator("101")

    # test whether or not the simulator is an instance of the class
    def test_instance(self):
        self.assertIsInstance(self.simulator0, Simulator,
                              "Failed to create an object of the class Simulator.")

    # test the data types of the input for the simulator
    def test_input_type(self):
        self.assertEqual(self.simulator_string.input, TypeError,
                         "The class accepts non-integers as inputs.")
        self.assertEqual(self.simulator_float.input, TypeError,
                         "The class accepts floats as inputs.")
        self.assertEqual(self.simulator_negative.input, TypeError,
                         "The class accepts negative values as inputs.")

    # test the number of open centers
    def test_number_of_open_centers(self):
        self.assertEqual(self.simulator3.get_num_of_open_centers(), 2,
                         "The number of open centers is not correct.")
        self.assertEqual(self.simulator8.get_num_of_open_centers(), 5,
                         "The number of open centers is not correct.")

    # test the number of full centers
    def test_number_of_full_centers(self):
        self.assertEqual(self.simulator8.get_num_of_full_centers(), self.simulator8.open_centers.count(100),
                         "The number of full centers is not correct.")
        self.assertEqual(self.simulator25.get_num_of_full_centers(), self.simulator25.open_centers.count(100),
                         "The number of full centers is not correct.")

    # test the number of working trainees
    def test_number_working_trainees(self):
        self.assertEqual(self.simulator3.get_num_working_trainees(), sum(self.simulator3.open_centers),
                         "The number of trainees currently training is wrong.")
        self.assertEqual(self.simulator8.get_num_working_trainees(), sum(self.simulator8.open_centers),
                         "The number of trainees currently training is wrong.")

    # test how many trainees are waiting on the list
    def test_get_waiting_trainees(self):
        self.assertEqual(self.simulator3.get_num_waiting_list(), self.simulator3.num_waiting_list,
                         "We're getting the wrong number or waiting list trainees")

    # test to see that the centers don't exceed the maximum number of trainees
    def test_centers_do_not_exceed_maximum_trainees(self):
        for centre in self.simulator8.open_centers:
            self.assertLessEqual(centre, 100, "More than 100 trainees found in a training center.")
        for centre in self.simulator25.open_centers:
            self.assertLessEqual(centre, 100, "More than 100 trainees found in a training center.")

    # test that the generate_new_trainees function works
    def test_generate_new_trainees(self):
        for i in range(75):
            self.assertLessEqual(self.simulator3.generate_new_trainees(), 100,
                                 "More than 100 trainees generated in a month.")
            self.assertGreaterEqual(self.simulator3.generate_new_trainees(), 50,
                                    "Fewer than 50 trainees generated in a month.")

    # testing the output where one month was entered in simulator
    def test_simulator1_outputs(self):
        self.assertEqual(self.simulator1.open_centers[0], 13,
                         "Failed to assign trainees to the open center in a Simulator object with input 1.")
        self.assertEqual(self.simulator1.num_waiting_list, 76,
                         "Failed to put extra trainees into the waiting list in a Simulator object with input 1.")

    # tests whether or not a center accepts up to 50 trainees
    def test_centers_accept_up_to_50_trainees(self):
        obj_lst = [self.simulator3, self.simulator8, self.simulator25]
        for obj in obj_lst:
            original_lst = obj.open_centers.copy()
            obj.distribute_trainees(1000)
            for i in range(obj.open_centers):
                added_trainees = obj.open_centers[i] - original_lst[i]
                self.assertLessEqual(added_trainees, 50, "More than 50 trainees assigned to a training center.")

    # tests 0 input in simulator
    def test_simulator0_outputs(self):
        self.assertEqual(self.simulator0.open_centers, [0], "There is an incorrect number of open centres.")
        self.assertEqual(self.simulator0.get_num_of_open_centers(), 1, "This is an incorrect number of open centers.")
        self.assertEqual(self.simulator0.get_num_of_full_centers(), 0, "This is an incorrect number of full centers.")
        self.assertEqual(self.simulator0.get_num_working_trainees(), 0, "This is the wrong number of working trainees.")
        self.assertEqual(self.simulator0.get_num_waiting_list(), 0, "This is the wrong number of people on the waiting "
                                                                    "list.")
    # tests 3 input in simulator
    def test_simulator3_outputs(self):
        self.assertEqual(self.simulator3.open_centers, [90, 78],
                         "Either an incorrect number of open centers or centers not full.")
        self.assertEqual(self.simulator3.get_num_of_open_centers(), 2, "This is an incorrect number of open centers.")
        self.assertEqual(self.simulator3.get_num_of_full_centers(), 0, "This is an incorrect number of full centers.")
        self.assertEqual(self.simulator3.get_num_working_trainees(), 168, "This is the wrong number of working "
                                                                          "trainees.")
        self.assertEqual(self.simulator3.get_num_waiting_list(), 80, "This is the wrong number of people on the "
                                                                     "waiting list.")
    # tests whether the simulator title is a string
    def test_simulator_title_is_string(self):
        title=self.simulation_interface.winfo_toplevel().title()
        self.assertEqual(title, "Simulator")

    # tests 3 input in simulator (Dynamic)
    def test_simulator3_outputs_dynamic(self):
        self.assertEqual(self.simulator3.open_centers, [90, 78], "Either an incorrect number of open centers or"
                                                                   "centers not full.")
        self.assertEqual(self.simulator3.get_num_of_open_centers(), len(self.simulator3.open_centers), "This is an incorrect number of open centers.")
        self.assertEqual(self.simulator3.get_num_of_full_centers(), self.simulator3.open_centers.count(100), "This is an incorrect number of full centers.")
        self.assertEqual(self.simulator3.get_num_working_trainees(), sum(self.simulator3.open_centers), "The number of trainees currently training is wrong.")
        self.assertEqual(self.simulator3.get_num_waiting_list(), self.simulator3.num_waiting_list, "We're getting the wrong number or waiting list trainees")

    # 100 input in simulator using random.seed that will definitely fill up one training center
    def test_simulator101_outputs_static(self):
        for centre in self.simulator101.open_centers:
            self.assertLessEqual(centre, 100, "More than 100 trainees found in a training center.")

    # 101 input in simulator using random.seed that will definitely fill up one training center (dynamic)
    def test_simulator101_outputs_dynamic(self):
        self.assertEqual(self.simulator101.get_num_of_open_centers(), len(self.simulator101.open_centers), "This is an incorrect number of open centers.")
        self.assertEqual(self.simulator101.get_num_of_full_centers(), self.simulator101.open_centers.count(100), "This is an incorrect number of full centers.")
        self.assertEqual(self.simulator101.get_num_working_trainees(), sum(self.simulator101.open_centers), "The number of trainees currently in training is wrong.")
        self.assertEqual(self.simulator101.get_num_waiting_list(), self.simulator101.num_waiting_list, "We're getting the wrong number or waiting list trainees")