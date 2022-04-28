import random

class Center():
    def __init__(self):

        self.center_dictionary = {"training_hubs": {}, "bootcamps": {}, "tech_center": {}}
        self.waiting_list_dictionary = {
        "Java": 0,
        "C#": 0,
        "Data": 0,
        "DevOps": 0,
        "Business": 0
    }


    def generate_center(self):
        random_num = random.randrange(1,4)
        # Training hubs
        print(random_num)
        if random_num == 1:
            # If there are already three training hubs open, do not open another training hub
            num_open = len([dictionary for dictionary in self.center_dictionary["training_hubs"] if dictionary["open"] == "yes"])
            if num_open != 3:
                # Creates a new id for the newly created training hub
                id = len(self.center_dictionary["training_hubs"])
                self.center_dictionary["training_hubs"][str(id)] = {"open": "yes", "type": "training_hubs"}
        # bootcamps
        if random_num == 2:
            # If there are already two bootcamps open, do not open another bootcamp
            num_open = len([dictionary for dictionary in self.center_dictionary["bootcamps"] if dictionary["open"] == "yes"])
            if num_open != 2:
                # Creates a new id for the newly created training hub
                id = len(self.center_dictionary["bootcamps"])
                self.center_dictionary["bootcamps"][str(id)] = {"open": "yes", "type": "bootcamps"}
        # tech centers
        if random_num == 3:
            # Determines what course the tech center will be teaching
            course = random.choice(["Java", "C#", "Data", "DevOps", "Business"])
            # Creates a new id for the tech center 
            id = len(self.center_dictionary["tech_center"])
            self.center_dictionary["tech_center"][str(id)] = {"open": "yes", "type": "tech_center", "course": course}
    
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
    obj.generate_center()
    print(obj.center_dictionary)

