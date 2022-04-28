from center import Center


# one_single_center = {
#     "open": "yes",
#     "type": "training_hub/bootcamp/tech_center",
#     "trainee": {"java": 0, "C#":0, ...}
# }

# all_centers = [one_single_center #1, one_single_center #2, ...]

class Simulator:
    def __init__(self):
        self.current_month_output = {}
        self.history = []
        self.center_class = Center()
        self.type = ["training_hub", "bootcamp", "tech_center"]
        self.courses = ["Java", "C#", "Data", "DevOps", "Business"]

    def calculate_open_centers(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.type, 0)
        for center in inp:
            if center['open'] == 'yes':
                result[center['type']] += 1
        return result

    def calculate_full_centers(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.type, 0)
        for center in inp:
            if center['open'] == 'yes':
                center_type = center['type']
                if center_type == "training_hub":
                    full_or_not = (sum(center['trainee'].values()) == 100)
                elif center_type == "bootcamp":
                    full_or_not = (sum(center['trainee'].values()) == 500)
                else:
                    full_or_not = (sum(center['trainee'].values()) == 200)
                result[center['type']] += full_or_not
        return result

    def calculate_num_of_trainees(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.courses, 0)
        for center in inp:
            if center['open'] == 'yes':  # just to make sure
                center_trainee = center['trainee']
                for course, num in center['trainee'].items():
                    result[course] += num
        return result


    def calculate_num_of_waiting_list(self):
        return self.center_class.calculate_num_of_waiting_list()

    def calculate_closed_centers(self, inp):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.type, 0)
        for center in inp:
            if center['open'] == 'no':
                result[center['type']] += 1
        return result

    def add_to_history(self):
        self.current_month_output = self.center_class.update_current_month_output()
        self.history.append(self.current_month_output)
        return self.history

    # Pseudocode

    # month_simulation():
        # all computations from center_class
        # self.calculate_open_centers()
        # self.calculate_full_centers()
        # self.calculate_num_of_trainees()
        # self.calculate_num_of_waiting_list()
        # self.calculate_closed_centers()
        # self.current_month_output = center_class_output

    # duration_simulation():
        # for month in duration:
            # month_simulation()


if __name__ == "__main__":
    all_centers = [
        {
            "open": "yes",
            "type": "tech_center",
            "trainee": {"Java": 200}
        },
        {
            "open": "yes",
            "type": "bootcamp",
            "trainee": {"Java": 250, "C#": 4}
        },
        {
            "open": "yes",
            "type": "training_hub",
            "trainee": {"Java": 50, "C#": 50}
        },
        {
            "open": "no",
            "type": "training_hub",
            "trainee": {"Java": 50, "C#": 50}
        }
        ]

    simulator = Simulator()
    open_centers = simulator.calculate_open_centers(all_centers)
    print("open", open_centers)
    closed_centers = simulator.calculate_closed_centers(all_centers)
    print("closed", closed_centers)
    full_centers = simulator.calculate_full_centers(all_centers)
    print("full", full_centers)
    num_trainees = simulator.calculate_num_of_trainees(all_centers)
    print("trainee", num_trainees)
