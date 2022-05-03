from center import Center
from trainee import Trainee
import csv
import re
from pprint import pprint

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
        self.trainee_class = Trainee()

        if center_full_requirements is None:
            center_full_requirements = {"training_hub": 100, "bootcamp": 500, "tech_center": 200}
        # {"type_of_center" : num_of_trainees_to_count_as_a_full_center}
        self.center_full_requirements = center_full_requirements
        self.center_type = self.center_full_requirements.keys()

        self.courses = self.center_class.waiting_list_dictionary

    def reset_history(self):
        self.center_class = Center()
        self.current_month_output = {}
        self.history = []

    @staticmethod
    def input_type_check(inp):
        if isinstance(inp, str):
            if not inp.isdigit():
                return TypeError
        elif isinstance(inp, float):
            return TypeError
        return int(inp)

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

    def calculate_num_of_waiting_list(self, inp=None):
        if inp is None:
            inp = self.center_class.waiting_list_dictionary
        num_of_waiting_list = inp.copy()
        return num_of_waiting_list

    def calculate_closed_centers(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.center_type, 0)
        for center in inp:
            if center['open'] == 'no':
                result[center['type']] += 1
        return result

    def month_simulation(self, open_new_center: bool, second_dist=False):
        if not second_dist:
            if open_new_center:
                self.center_class.generate_center()
            self.center_class.create_distribution_list()

        self.center_class.distribute()
        self.center_class.close_center()
        # to be reviewed after center_class

        # all computations from center_class
        num_open_centers = self.calculate_open_centers()
        num_full_centers = self.calculate_full_centers()
        num_of_trainees = self.calculate_num_of_trainees()
        num_of_waiting_list = self.calculate_num_of_waiting_list()
        num_closed_centers = self.calculate_closed_centers()
        current_month_output = {"number of open centers": num_open_centers,
                                "number of closed centers": num_closed_centers,
                                "number of full centers": num_full_centers,
                                "number of trainees": num_of_trainees,
                                "number of trainees on waiting list": num_of_waiting_list}
        self.current_month_output = current_month_output

        if not second_dist:
            new_trainees = self.trainee_class.generate_new_trainees()
            self.center_class.push_to_waiting_list(new_trainees)
            self.month_simulation(False, True)

        elif second_dist:
            self.history.append(self.current_month_output)

    def duration_simulation(self, duration):
        duration = self.input_type_check(duration)
        if duration == TypeError:
            return
        for month in range(duration):
            open_new_center = False
            if month % 2 == 0:
                open_new_center = True
            self.month_simulation(open_new_center, False)


    def export_to_csv(self, file_name="simulation_record", extension="csv"):
        if extension == "csv":
            file_name = re.sub("[^a-zA-Z0-9 /:_]", "", file_name)  # can we not use re?
            with open(f"{file_name}.{extension}", "w", newline="") as file:

                writer = csv.writer(file)
                headers = []
                for monthly_key, monthly_result in self.history[-1].items():
                    headers.extend([f"{monthly_key} -- {key}" for key in monthly_result.keys()])
                    headers.append(f"{monthly_key} -- total")
                writer.writerow(headers)

                for month in self.history:
                    data = []
                    for main_result in month.values():
                        aggregate = 0  # for calculating total
                        for specific_result in main_result.values():
                            data.append(specific_result)
                            aggregate += specific_result
                        data.append(aggregate)
                    writer.writerow(data)

        else:
            return NotImplementedError


if __name__ == "__main__":
    simulator = Simulator()
    simulator.duration_simulation(30)
    pprint(simulator.history)
    print(len(simulator.history))

    # pprint(simulator.history)

    simulator.export_to_csv()
