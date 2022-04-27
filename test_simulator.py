# get_num_of_open_centers()
# get_num_of_full_centers()
# get_num_working_trainees()
# get_num_waiting_list()


# generate_new_trainees()
# distribute_trainees()

# open_centers - list
# num_waiting_list - integer


from tkinter import *
import unittest
from simulator import Simulator

class Simulator_tests(unittest.TestCase):


    # test whether or not the simulator is an instance of the class
    def test_instance(self):
        simulator = Simulator()

        self.assertIsInstance(simulator, Simulator, "Failed to create an object of the class Simulator.")

    # # test the data types of the input for the simulator
    # def test_input_type(self):
    #     self.assertEqual(self.simulator_string.input, False, "The class accepts non-integers as inputs.")
    #     self.assertEqual(self.simulator_float.input, False, "The class accepts floats as inputs.")
    #     self.assertEqual(self.simulator_negative.input, False, "The class accepts negative values as inputs.")

    # test the number of open centres
    def test_number_of_open_centers(self):
        simulator = Simulator()
        self.assertEqual(simulator.calculate_open_centres(), 6,
                         "The number of open centres is not correct.")

    # test the number of full centres
    def test_number_of_full_centers(self):
        simulator = Simulator()
        self.assertEqual(simulator.calculate_full_centres(), 1,
                         "The number of full centres is not correct.")


    # test the number of working trainees
    def test_number_working_trainees(self):
        self.assertEqual(self.simulator3.get_num_working_trainees(), sum(self.simulator3.open_centers), "The number of trainees currently training is wrong.")
        self.assertEqual(self.simulator8.get_num_working_trainees(), sum(self.simulator8.open_centers), "The number of trainees currently training is wrong.")

    # test how many trainees are waiting on the list
    def test_get_waiting_trainees(self):
        self.assertEqual(self.simulator3.get_num_waiting_list(), self.simulator3.num_waiting_list, "We're getting the wrong number or waiting list trainees")


    # # testing the output where one month was entered in simulator
    # def test_simulator1_outputs(self):
    #     self.assertEqual(self.simulator1.open_centers[0], 13, "Failed to assign trainees to the open center in a Simulator object with input 1.")
    #     self.assertEqual(self.simulator1.num_waiting_list, 76, "Failed to put extra trainees into the waiting list in a Simulator object with input 1.")


    #TKinter BELOW

    # tests whether the simulator title is a string
    def test_simulator_title_is_string(self):
        title=self.simulation_interface.winfo_toplevel().title()
        self.assertEqual(title, "Simulator")





