from centre import Centre


class Simulator:
    def __init__(self):
        self.current_month_output = {}
        self.history = []
        self.centre_class = Centre()

    def calculate_open_centres(self):
        return self.centre_class.calculate_open_centres()

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
