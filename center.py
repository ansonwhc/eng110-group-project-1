import random

class Center():
    def __init__(self):
        self.center_dictionary = {"training_hubs": {}, "bootcamps": {}, "tech_center": {}}

    def generate_center(self, trainee_dictionary):
        random_num = random.randrange(1,4)
        # Training hubs
        if random_num == 1:
            # If there are three centres open, do not open another training hub
            num_open = len([dictionary for dictionary in self.center_dictionary["training_hubs"] if dictionary['open'] == 'yes'])
            if num_open == 3:
                self.push_to_waiting_list()
            else:
                # Creates a new id for the newly created training hub
                id = len(self.center_dictionary["training_hubs"])
                self.center_dictionary["training_hubs"][str(id)] = {}
                self.center_dictionary["training_hubs"][str(id)]["num_trainees"] = sum(trainee_dictionary.values())
    
    def push_to_waiting_list(self):
        pass

if __name__ == "__main__":
    example_dict = {
        "Java": 5,
        "C#": 3,
        "Data": 2,
        "DevOps": 6,
        "Business": 9
    }

    obj = Center()
    obj.generate_center(example_dict)
    print(obj.center_dictionary)

