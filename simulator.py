from centre import Centre

class Simulator:
    def __init__(self):
        self.centre_class = Centre()

    def calculate_open_centres(self):
        return self.centre_class.calculate_open_centres()

    def calculate_full_centres(self):
        return self.centre_class.calculate_full_centres()