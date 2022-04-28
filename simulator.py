from centre import Centre


# one_single_centre = {
#     "open": "yes",
#     "type": "training_hub/bootcamp/tech_centre",
#     "trainee": {"java": 0, "C#":0, ...}
# }

# all_centres = [one_single_centre #1, one_single_centre #2, ...]

class Simulator:
    def __init__(self):
        self.current_month_output = {}
        self.history = []
        self.centre_class = Centre()
        self.type = ["training_hub", "bootcamp", "tech_centre"]
        self.courses = ["Java", "C#", "Data", "DevOps", "Business"]

    def calculate_open_centres(self, inp=None):
        if inp is None:
            inp = self.centre_class.all_centres
        result = dict.fromkeys(self.type, 0)
        for centre in inp:
            if centre['open'] == 'yes':
                result[centre['type']] += 1
        return result

    def calculate_full_centres(self):
        return self.centre_class.calculate_full_centres()

    def calculate_num_of_trainees(self):
        return self.centre_class.calculate_num_of_trainees()

    def calculate_num_of_waiting_list(self):
        return self.centre_class.calculate_num_of_waiting_list()

    def calculate_closed_centres(self):
        return self.centre_class.calculate_closed_centres()

    def add_to_history(self):
        self.current_month_output = self.centre_class.update_current_month_output()
        self.history.append(self.current_month_output)
        return self.history

    # Pseudocode

    # month_simulation():
        # all computations from centre_class
        # self.calculate_open_centres()
        # self.calculate_full_centres()
        # self.calculate_num_of_trainees()
        # self.calculate_num_of_waiting_list()
        # self.calculate_closed_centres()
        # self.current_month_output = centre_class_output

    # duration_simulation():
        # for month in duration:
            # month_simulation()


if __name__ == "__main__":
    all_centres = [
        {
            "open": "yes",
            "type": "training_hub",
            "trainee": {"java": 0, "C#":0}
        },
        {
            "open": "yes",
            "type": "bootcamp",
            "trainee": {"java": 0, "C#": 0}
        }
        ]

    simulator = Simulator()
    open_centres = simulator.calculate_open_centres(all_centres)
    print(open_centres)