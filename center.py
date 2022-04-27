import random

class Center():
    def __init__(self):
        self.center_dictionary = {"training_hubs": {}, "bootcamps": {}, "tech_center": {}}

    def generate_center(self, num_trainees):
        random_num = random.randrange(0,3)
        id = len(self.center_dictionary["training_hubs"])
        print(id)

obj = Center()
obj.generate_center(5)

        





