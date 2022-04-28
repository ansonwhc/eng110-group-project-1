from center import Center
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

        if center_full_requirements is None:
            center_full_requirements = {"training_hub": 100, "bootcamp": 500, "tech_center": 200}
        # {"type_of_center" : num_of_trainees_to_count_as_a_full_center}
        self.center_full_requirements = center_full_requirements
        self.center_type = self.center_full_requirements.keys()

        self.courses = self.center_class.waiting_list_dictionary

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
            out = inp.copy()
        return out

    def calculate_closed_centers(self, inp=None):
        if inp is None:
            inp = self.center_class.all_centers
        result = dict.fromkeys(self.center_type, 0)
        for center in inp:
            if center['open'] == 'no':
                result[center['type']] += 1
        return result

    def month_simulation(self, open_new_center: bool):
        if open_new_center:
            self.center_class.generate_center()
        each_center_take_in = self.center_class.distribution_sampling_center_in_take()
        self.center_class.assess_availability(each_center_take_in)
        self.center_class.push_to_waiting_list({
            "Java": 4,
            "C#": 6,
            "Data": 15,
            "DevOps": 32,
            "Business": 9})
        # to be reviewed after center_class
        print(self.center_class.all_centers)
        # all computations from center_class
        num_open_centers = self.calculate_open_centers()
        num_full_centers = self.calculate_full_centers()
        num_of_trainees = self.calculate_num_of_trainees()
        num_of_waiting_list = self.calculate_num_of_waiting_list()
        # print(num_of_waiting_list)
        num_closed_centers = self.calculate_closed_centers()
        current_month_output = {"number of open centers": num_open_centers,
                                "number of closed centers": num_closed_centers,
                                "number of full centers": num_full_centers,
                                "number of trainees": num_of_trainees,
                                "number of trainees on waiting list": num_of_waiting_list}
        self.history.append(current_month_output)
        self.current_month_output = current_month_output

    def duration_simulation(self, duration):
        for month in range(duration):
            open_new_center = False
            if (month + 1) % 2 == 0:
                open_new_center = True
            self.month_simulation(open_new_center)

    def export_to_csv(self, file_name="simulation_record", extension="csv"):
        if extension == "csv":
            file_name = re.sub("[^a-zA-Z0-9 /:_]", "", file_name)   # can we not use re?
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
                        aggregate = 0   # for calculating total
                        for specific_result in main_result.values():
                            data.append(specific_result)
                            aggregate += specific_result
                        data.append(aggregate)
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

    # simulator = Simulator()
    # open_centers = simulator.calculate_open_centers(all_centers)
    # print("open", open_centers)
    # closed_centers = simulator.calculate_closed_centers(all_centers)
    # print("closed", closed_centers)
    # full_centers = simulator.calculate_full_centers(all_centers)
    # print("full", full_centers)
    # num_trainees = simulator.calculate_num_of_trainees(all_centers)
    # print("trainee", num_trainees)
    # simulator.month_simulation(False)
    # print("no gen month output")
    # pprint(simulator.current_month_output)
    # simulator.month_simulation(True)
    # print("gen month output")
    # pprint(simulator.current_month_output)
    simulator = Simulator()
    simulator.duration_simulation(5)
    # pprint(simulator.history)

    simulator.export_to_csv()
