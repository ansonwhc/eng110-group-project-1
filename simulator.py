<<<<<<< HEAD
class Simulator():
    def __init__(self, number_of_weeks):
        self.weeknumber = number_of_weeks
        pass

import random 
random.seed(101)


# number of trainees generated
print(random.randrange(0, 101))
# number of trainees
print(random.randrange(0, 51))

# number of trainees generated
print(random.randrange(50, 101))
# number of trainees 
print(random.randrange(0, 51))


=======
class Simulator:
    def __init__(self,
                 duration: str):

        # user_input, the duration of the simulation
        self.input = self.check_input_type(duration)

        # internal_variables
        self.open_centers = [0]   # [open_centre_0, open_centre_1, ..., open_centre_n], where each element in the list\
        # represents the number of trainees-in-training in that centre
        self.num_waiting_list = 0   # number of trainees on the waiting list

        if self.input is not TypeError:
            self.result, self.simulation_info = self.simulate()

    def simulate(self, inp: int = None) -> (dict, dict):
        """
        main method for running the simulation

        :param inp: int, default None
        :return: (dict, dict), (output_dict, simulation_info_dict)
        """
        # probably won't be used as for now
        if inp is not None:
            self.input = inp

        for month in range(self.input):
            # sample a number of trainees from 50 to 100
            sampled_num_trainees = self.generate_new_trainees()

            # every two months
            if (month + 1) % 2 == 0:
                # add new center
                self.open_centers.append(0)

            self.distribute_trainees()

        simulation_info = self.update_simulation_info()
        output = {
            "Number of open centers": self.get_num_of_open_centers(),
            "Number of full centers": self.get_num_of_full_centers(),
            "Number of working trainees": self.get_num_working_trainees(),
            "Number of trainees on waiting list": self.get_num_waiting_list()
        }

        return output, simulation_info

    def check_input_type(self, inp: str = None) -> (int | TypeError):
        """
        Checking the type of inputs

        :param inp: str
        :return: int(inp) if input in numeric, else TypeError
        """
        if inp is None:
            inp = self.input

        if not inp.isnumeric():
            output = TypeError
        else:
            output = int(inp)

        return output

    # Anson
    def update_simulation_info(self, inp: dict = None) -> dict:
        """
        this is for updating simulation info for exporting simulation history

        :param inp: dict, default None, e.g. {"Simulation run time (ms)": 0.001}
        :return: dict
        """
        # simulation_info = duration, for now
        sim_info = {
            "Simulated months": self.input
        }
        if inp is not None:
            sim_info = {**sim_info, **inp}

        return sim_info

    def get_num_of_open_centers(self, inp=None) -> int:
        # return the number of open centers
        if inp is None:
            inp = self.open_centers

        # work here ...
        return 0   # to delete

    def get_num_of_full_centers(self, inp=None) -> int:
        # return the number of full centers
        if inp is None:
            inp = self.open_centers
        # work here ...
        return 0    # to delete

    def get_num_working_trainees(self, inp=None) -> int:
        # return the number of working trainees
        if inp is None:
            inp = self.open_centers
        # work here ...
        return 0    # to delete

    def get_num_waiting_list(self, inp=None) -> int:
        # return the number of trainees on the waiting list
        if inp is None:
            inp = self.open_centers
        # work here ...
        return 0    # to delete

    def generate_new_trainees(self,
                              lower_bound=None,
                              upper_bound=None) -> int:
        # generate a number of trainees for each month, from 50 to 100
        # work here ...
        return 0   # to delete

    def distribute_trainees(self):
        # update self.open_centers with our sampled number of trainees
        # work here ...
        pass


# Refactoring Note (later_TODO):
# since our class is supposed to be initialised once, and allows for repeated calls on simulate() method
# it makes sense for us to not run the simulation within the __init__() process
# It leads to us not requiring <duration> for initialising the class, but needing <duration> as an input
# in simulate(), i.e. simulate(duration). But this WILL fail the test, so let's not implement this as for now.
>>>>>>> a931113be63d2f79c3eee44b72b21b6f50772fdc
