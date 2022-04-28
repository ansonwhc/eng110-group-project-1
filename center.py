import random

class Center():
    def __init__(self):
        self.all_centers = []
        self.waiting_list_dictionary = {
        "Java": 0,
        "C#": 0,
        "Data": 0,
        "DevOps": 0,
        "Business": 0
    }
        self.num_bootcamps = 0
        self.num_open_training_hubs = 0
        self.can_open_training_hub = True
        self.can_open_bootcamp = True

    def centers_available(self):

        if self.num_open_training_hubs == 3:
            self.can_open_training_hub = False
        if self.num_bootcamps == 2:
            self.can_open_bootcamp = False
        
        if self.can_open_training_hub == True and self.can_open_bootcamp == True:
            random_num = random.randrange(1,4)
        elif self.can_open_training_hub == False and self.can_open_bootcamp == True:
            random_num = random.randrange(2, 4)
        elif self.can_open_training_hub == True and self.can_open_bootcamp == False:
            random_num = random.choice([1, 3])
        elif self.can_open_training_hub == False and self.can_open_bootcamp == False:
            random_num = 3
        
        return random_num

    def generate_center(self):
        random_num = self.centers_available()
        # (TODO: Type dictionary {int: type_center})
        # Training hub
        if random_num == 1:
            self.all_centers.append({"open": "yes", "type": "training_hubs", "trainee": {}})
        # Bootcamp
        elif random_num == 2:
            self.all_centers.append({"open": "yes", "type": "bootcamp", "trainee": {}})
        # Tech center
        elif random_num == 3:
            # Determines what course the tech center will be teaching
            course = random.choice(["Java", "C#", "Data", "DevOps", "Business"])
            # Creates a new id for the tech center 
            self.all_centers.append({"open": "yes", "type": "tech_center", "course": course, "trainee": {}})
    
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
    print(obj.all_centers)

