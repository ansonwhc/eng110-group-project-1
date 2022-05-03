import random


class Center():
    def __init__(self):
        self.all_centers = []
        self.distribute_trainees_list = []
        self.waiting_list_dictionary = {
            "Java": 1,
            "C#": 2,
            "Data": 30,
            "DevOps": 4,
            "Business": 5
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
        random_num = 1
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

    def distribution_sampling_center_in_take(self):
        # deciding how many trainees to send to each center
        # sample_dic = {
        #     "Java": 14,
        #     "C#": 13,
        #     "Data": 12,
        #     "DevOps": 6,
        #     "Business": 10 }
        # try a code to assess if the centers are full or not
        # TODO: if center any center is full add the trainees to another center until all centers are full
        # setting conditions as whether the center are open and have numb_trainees lees than their max limit
        each_center_take_in = []
        for center in self.all_centers:
            center_type = center['type']
            condition_1 = (center['open'] == 'yes')
            num_trainee_in_center = sum(center['trainee'].values())
            condition_2 = (num_trainee_in_center < self.max_capacity[center_type])
            if condition_1 and condition_2:
                each_center_take_in.append(random.randint(0, 50))
            else:
                each_center_take_in.append(0)

    # def assess_availability(self):
    #     # Assessing whether our center can take the sample number of trainees
    #     for center, num_take_in in zip(self.all_centers, each_center_take_in):
    #         center_type = center['type']
    #         available_num = max_capacity[center_type] - sum(center["trainee"].values()) - num_take_in
    #         if available_num > 0:
    #             # Center is still available
    #             self.available_num_lg_0()
    #         elif available_num == 0:
    #             # If they're equal the center is full
    #             self.available_num_eq_0()
    #         else:
    #             # For when sampled number of trainees exceeded the center capacity
    #             self.available_num_ls_0()

    def create_distribution_list(self):
        self.distribute_trainees_list = []
        # Shuffles the centers list for good measure (shuffle randomises the order of items in the list)
        random.shuffle(self.all_centers)
        for center in self.all_centers:
            self.distribute_trainees_list.append(random.randrange(0, 51))

    def distribute_tech_centers(self):
        # Iterating through all_centers
        for index, center in enumerate(self.all_centers):
            # How many trainees a center it can take
            random_trainee = self.distribute_trainees_list[index]
            # Iterating through all courses in the waiting list
            for course in self.waiting_list_dictionary:
                # Finding matching courses
                if course == center['course']:
                    # Grabbing the number of trainees from the matching course
                    res = self.waiting_list_dictionary[course]
                    # If number of trainees in the course is less than 200, keep adding the min number of trainees
                    if center['trainee'][course] < 200:
                        # accepting = min([res, (200 - res)])
                        accepting = min([min([res, (200 - res)]), random_trainee])
                        center['trainee'][course] += accepting
                        self.waiting_list_dictionary[course] -= accepting

            # If the trainee_num is more than the space available in the center, the center will simply not accept it
            # If all centers are full return the trainees to the waiting_list
            # randomly generated trainees need to be allocated to the course types of the waiting_list

    def distribute_training_hub(self):
        self.create_distribution_list()
        for index, center in enumerate(self.all_centers):
            random_trainee = self.distribute_trainees_list[index]
            if sum(center['trainee'].values()) < self.max_capacity['training_hub']:
                res = sum(self.waiting_list_dictionary.values())
                accepting = min([min([res, (self.max_capacity['training_hub'] - res)]), random_trainee])
                for trainee in range(accepting):
                    choose_from = [key for key, value in self.waiting_list_dictionary.items() if value > 0]
                    sampled_course = random.choice(choose_from)
                    center['trainee'][sampled_course] += 1
                    self.waiting_list_dictionary[sampled_course] -= 1

    def distribute_bootcamp(self):
        self.create_distribution_list()
        for index, center in enumerate(self.all_centers):
            random_trainee = self.distribute_trainees_list[index]
            if sum(center['trainee'].values()) < self.max_capacity['bootcamp']:
                res = sum(self.waiting_list_dictionary.values())
                accepting = min([min([res, (self.max_capacity['bootcamp'] - res)]), random_trainee])
                for trainee in range(accepting):
                    choose_from = [key for key, value in self.waiting_list_dictionary.items() if value > 0]
                    sampled_course = random.choice(choose_from)
                    center['trainee'][sampled_course] += 1
                    self.waiting_list_dictionary[sampled_course] -= 1


# distribute from the waiting_list
# (random 0 - 50) -> random = 1 -> 1 =10 %, 4 = 40 % ,6 = 60% -> 100% ->


# while the number of trainees is >= 0
# then we would run all of the while codes


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
    obj.all_centers[0]['type'] == 'training_hub'
    print("waiting list:",obj.waiting_list_dictionary)
    print(obj.distribute_training_hub())
    center_dict = obj.all_centers[0]
    wait_dict = obj.waiting_list_dictionary

    print("centre list:", center_dict['trainee'])
    print("waiting list:", wait_dict)
