# get_num_of_open_centers()
# get_num_of_full_centers()
# get_num_working_trainees()
# get_num_waiting_list()


# generate_new_trainees()
# distribute_trainees()

# open_centers - list
# num_waiting_list - integer


import tkinter *
import unittest
import random
from simulator import Simulator
from Single-tab-interface import SimulationInterface
random.seed(53)

class Simulator_tests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.simulator0 = Simulator(0)
        self.simulator1 = Simulator(1)
        self.simulator3 = Simulator(3)
        self.simulator8 = Simulator(8)
        self.simulator25 = Simulator(25)
        self.simulator_string = Simulator("Hello")
        self.simulator_float = Simulator(4.3)
        self.simulator_negative = Simulator(-34)
        self.simulation_interface = SimulationInterface()
        self.simulation_interface.create_window()

    def test_using_waiting_list(self):
        if self.simulator25.open_centers.count(100) < len(self.simulator25.open_centers):
            self.assertEqual(self.simulator25.num_waiting_list, 0, "Trainees from the waiting list are not being assigned to available centers.") 
        if self.simulator8.open_centers.count(100) < len(self.simulator8.open_centers):
            self.assertEqual(self.simulator8.num_waiting_list, 0, "Trainees from the waiting list are not being assigned to available centers.")

    def test_simulator1_outputs(self):
        self.assertEqual(self.simulator1.open_centers[0], 13, "Failed to assign trainees to the open center in a Simulator object with input 1.")
        self.assertEqual(self.simulator1.num_waiting_list, 65, "Failed to put extra trainees into the waiting list in a Simulator object with input 1.")

    # testing the output where one month was entered in simulator
    def test_simulator1_outputs(self):
        self.assertEqual(self.simulator1.open_centers[0], 13, "Failed to assign trainees to the open center in a Simulator object with input 1.")
        self.assertEqual(self.simulator1.num_waiting_list, 76, "Failed to put extra trainees into the waiting list in a Simulator object with input 1.")

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
        self.assertEqual(self.simulator3.open_centers, [90, 78], "Either an incorrect number of open centers or"
                                                                   "centers not full.")
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





