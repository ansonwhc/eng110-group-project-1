import random
from pprint import pprint


class Center():
    def __init__(self):
        self.all_centers = []
        self.distribute_trainees_list = []
        self.waiting_list_dictionary = {
            "Java": 199,
            "C#": 243,
            "Data": 302,
            "DevOps": 48,
            "Business": 59
        }
        self.max_capacity = {
            "training_hub": 100,
            "bootcamp": 500,
            "tech_center": 200}
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
            random_num = random.randrange(1, 4)
        elif self.can_open_training_hub == False and self.can_open_bootcamp == True:
            random_num = random.randrange(2, 4)
        elif self.can_open_training_hub == True and self.can_open_bootcamp == False:
            random_num = random.choice([1, 3])
        elif self.can_open_training_hub == False and self.can_open_bootcamp == False:
            random_num = 3

        return random_num

    def generate_center(self):
        # random_num = self.centers_available()
        random_num = 2
        # (TODO: Type dictionary {int: type_center})
        # Training hub
        if random_num == 1:
            self.all_centers.append({"open": "yes", "type": "training_hub", "trainee": {
                "Java": 0,
                "C#": 0,
                "Data": 0,
                "DevOps": 0,
                "Business": 0
            }})
        # Bootcamp
        elif random_num == 2:
            self.all_centers.append({"open": "yes", "type": "bootcamp", "trainee": {"Java": 0,
                                                                                    "C#": 0,
                                                                                    "Data": 0,
                                                                                    "DevOps": 0,
                                                                                    "Business": 0
                                                                                    }})
        # Tech center
        elif random_num == 3:
            # Determines what course the tech center will be teaching
            course = random.choice(["Java", "C#", "Data", "DevOps", "Business"])
            # Creates a new id for the tech center 
            self.all_centers.append({"open": "yes", "type": "tech_center", "course": course, "trainee": {course: 0}})

    def push_to_waiting_list(self, trainee):
        for trainee_key in trainee.keys():
            self.waiting_list_dictionary[trainee_key] += trainee[trainee_key]

    def close_center(self):
        for centers in self.all_centers:
            if centers["type"] == "training_hubs" and sum(centers["trainee"].values()) == 100:
                centers["full"] = "yes"
            elif centers["type"] == "bootcamp" and sum(centers["trainee"].values()) == 500:
                centers["full"] = "yes"
            elif centers["type"] == "tech_center" and sum(centers["trainee"].values()) == 200:
                centers["full"] = "yes"
            if centers["type"] == "training_hubs" and sum(centers["trainee"].values()) < 25:
                centers["open"] = "no"
            elif centers["type"] == "bootcamp" and sum(centers["trainee"].values()) < 25:
                centers["months_below_25"] += 1
                if centers["months_below_25"] == 4:
                    centers["open"] = "no"
            elif centers["type"] == "bootcamp" and sum(centers["trainee"].values()) >= 25:
                centers["months_below_25"] = 0
            elif centers["type"] == "tech_center" and sum(centers["trainee"].values()) < 25:
                centers["open"] = "no"

    def distribute(self):
        # Sample the number of trainees each center want to take in
        self.create_distribution_list()   # -> self.distribute_trainees_list
        # Iterating through all_centers
        for index, center in enumerate(self.all_centers):
            # access the number of trainees the current center want to take in
            random_trainee = self.distribute_trainees_list[index]

            open_atm = center['open'] == 'yes'
            if (center['type'] == 'training_hub') and open_atm:
                self.distribute_training_hub(index, random_trainee)

            elif (center['type'] == 'tech_center') and open_atm:
                self.distribute_tech_center(index, random_trainee)

            elif (center['type'] == 'bootcamp') and open_atm:
                self.distribute_bootcamp(index, random_trainee)

    def create_distribution_list(self):
        self.distribute_trainees_list = []
        # Shuffles the centers list for good measure (shuffle randomises the order of items in the list)
        random.shuffle(self.all_centers)
        for center in self.all_centers:
            self.distribute_trainees_list.append(random.randrange(0, 51))

    def distribute_tech_center(self, index: int, random_trainee: int):
        # TODO: add comments
        center = self.all_centers[index]
        if sum(center['trainee'].values()) < self.max_capacity['tech_center']:
            center_course = center['course']
            res = self.waiting_list_dictionary[center_course]
            want_to_accepting = random_trainee
            can_take_in = self.max_capacity['tech_center'] - sum(center['trainee'].values())
            accepting = min([can_take_in, want_to_accepting])  # does it go over the max (max: )
            center['trainee'][center_course] += accepting
            self.waiting_list_dictionary[center_course] -= accepting

    def distribute_training_hub(self, index: int, random_trainee: int):
        # TODO: add comments
        center = self.all_centers[index]
        print("center", center) # good

        if sum(center['trainee'].values()) < self.max_capacity['training_hub']:     # if not full
            res = sum(self.waiting_list_dictionary.values())   # how many on the waiting list
            print("res", res)   # ok?

            want_to_accepting = random_trainee
            print("want_to_take", want_to_accepting)   # good

            can_take_in = self.max_capacity['training_hub'] - sum(center['trainee'].values())
            print("can_take_in", can_take_in)   # ok

            accepting = min([can_take_in, want_to_accepting])   # does it go over the max (max: )
            print("training_hub accepting", accepting)   # good

            for trainee in range(accepting):
                choose_from = [key for key, value in self.waiting_list_dictionary.items() if value > 0]
                print("choose", choose_from)

                sampled_course = random.choice(choose_from)
                print("sampled", sampled_course)

                center['trainee'][sampled_course] += 1
                print("center", center['trainee'])

                self.waiting_list_dictionary[sampled_course] -= 1
                print("waiting", self.waiting_list_dictionary)


    def distribute_bootcamp(self, index: int, random_trainee: int):
        # TODO: add comments
        center = self.all_centers[index]
        if sum(center['trainee'].values()) < self.max_capacity['bootcamp']:
            res = sum(self.waiting_list_dictionary.values())
            want_to_accepting = random_trainee
            can_take_in = self.max_capacity['bootcamp'] - sum(center['trainee'].values())

            accepting = min([can_take_in, want_to_accepting])   # does it go over the max (max: )
            print("training_hub accepting", accepting)   # good
            for trainee in range(accepting):
                choose_from = [key for key, value in self.waiting_list_dictionary.items() if value > 0]
                sampled_course = random.choice(choose_from)
                center['trainee'][sampled_course] += 1
                self.waiting_list_dictionary[sampled_course] -= 1


if __name__ == "__main__":
    example_dict = {
        "Java": 5,
        "C#": 3,
        "Data": 2,
        "DevOps": 6,
        "Business": 9
    }

    obj = Center()
    # for _ in range(5):
    obj.generate_center()

    print("waiting list:", obj.waiting_list_dictionary)
    print("all centers:", obj.all_centers)
    obj.distribute()
    print(obj.distribute_trainees_list)
    print("waiting list:", obj.waiting_list_dictionary)
    print("all centers:", obj.all_centers)


    # print(obj.distribute_training_hub())
    # center_dict = obj.all_centers[0]
    # wait_dict = obj.waiting_list_dictionary
    #
    # print("centre list:", center_dict['trainee'])
    # print("waiting list:", wait_dict)
