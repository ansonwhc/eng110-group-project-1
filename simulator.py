class Simulator:
    def __init__(self,
                 duration: str,
                 file_name: str = None):
        self.input = duration
        self.record_list = [0]

        if file_name is None:
            self.file_name = "record_file"

        if not self.input.isnumeric():
            self.input = TypeError
        else:
            self.input = int(self.input)

        self.result, self.simulation_info = self.simulate()

        # internal_variables
        self.open_centers = []
        self.num_waiting_list = 0

    def simulate(self, inp=None):
        if inp is not None:
            self.input = inp

        # simulation_info = self.update_simulation_info()
        output = []
        simulation_info = ""   # temporary placeholder
        #
        # for month in range(self.input):
        #     # sample a number of trainees from 50 to 100
        #     sampled_num_trainees = self.generate_new_trainees()
        #
        #     # every two months
        #     if (month + 1) % 2 == 0:
        #         # add new center
        #         self.open_centers.append(0)
        #
        #     self.distribute_trainees()
        #
        # output.extend([self.get_num_of_open_centers(),
        #                self.get_num_of_full_centers(),
        #                self.get_num_working_trainees(),
        #                self.get_num_waiting_list()])

        # self.record()
        return output, simulation_info

    # Anson
    def update_simulation_info(self, inp):
        # self.simulation_info = duration, for now
        # return simulation info
        pass

    def record(self):
        # write to a csv file
        # f"{self.file_name}.csv"
        pass

    def get_num_of_open_centers(self, inp=None) -> int:
        if inp is None:
            inp = self.open_centers

        # work here ...
        return 0   # to delete

    def get_num_of_full_centers(self, inp=None) -> int:
        if inp is None:
            inp = self.open_centers
        # work here ...
        return 0    # to delete

    def get_num_working_trainees(self, inp=None) -> int:
        if inp is None:
            inp = self.open_centers
        # work here ...
        return 0    # to delete

    def get_num_waiting_list(self, inp=None) -> int:
        if inp is None:
            inp = self.open_centers
        # work here ...
        return 0    # to delete

    def generate_new_trainees(self,
                              lower_bound=None,
                              upper_bound=None) -> int:
        # work here ...
        return 0   # to delete

    def distribute_trainees(self):
        # update self.open_centers
        # work here ...
        pass
