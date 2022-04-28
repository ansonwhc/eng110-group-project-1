from center import Center
import csv
import re


# one_single_center = {
#     "open": "yes",
#     "type": "training_hub/bootcamp/tech_center",
#     "trainee": {"java": 0, "C#":0, ...}
# }

# all_centers = [one_single_center #1, one_single_center #2, ...]

class Simulator:
    def __init__(self,
                 center_full_requirements: dict = None):
        self.current_month_output = {}
        self.history = []
        self.center_class = Center()

        if center_full_requirements is None:
            center_full_requirements = {"training_hub": 100, "bootcamp": 500, "tech_center": 200}
        # {"type_of_center" : num_of_trainees_to_count_as_a_full_center}
        self.center_full_requirements = center_full_requirements
        self.center_type = self.center_full_requirements.keys()

        self.courses = ["Java", "C#", "Data", "DevOps", "Business"]

    def calculate_open_centers(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.center_type, 0)
        for center in inp:
            if center['open'] == 'yes':
                result[center['type']] += 1
        return result

    def calculate_full_centers(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.center_type, 0)
        for center in inp:
            if center['open'] == 'yes':
                # getting the total number of trainees in that center
                num_of_trainees = sum(center['trainee'].values())
                # getting the max number of trainees
                max_num_of_trainees = self.center_full_requirements[center['type']]
                full_or_not = (num_of_trainees == max_num_of_trainees)
                # add to our result
                result[center['type']] += full_or_not
        return result

    def calculate_num_of_trainees(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.courses, 0)
        for center in inp:
            if center['open'] == 'yes':  # just to make sure
                for course, num in center['trainee'].items():
                    result[course] += num
        return result

    def calculate_num_of_waiting_list(self):
        return self.center_class.calculate_num_of_waiting_list()

    def calculate_closed_centers(self, inp):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.center_type, 0)
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

    def export_to_csv(self, file_name="simulation record", extension="csv"):
        if extension == "csv":
            file_name = re.sub("[^a-zA-Z0-9 /:]", "", file_name)   # can we not use re?
            with open(f"{file_name}.{extension}", "w", newline="") as file:

                writer = csv.writer(file)
                writer.writerow(self.record_dict["headers"])

                for data in self.record_dict["data"]:
                    writer.writerow(data)
        else:
            return NotImplementedError

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
