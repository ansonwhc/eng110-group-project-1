import random
from trainee import Trainee

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
        monthly_trainees = Trainee.generate_new_trainees()
        max_capacity = {
            "training_hub": 100,
            "bootcamp": 500,
            "tech_center": 200}
        # TODO: if center any center is full add the trainees to another center until all centers are full
        # setting conditions as whether the center are open and have numb_trainees lees than their max limit
        each_center_take_in = []
        for center in self.all_centers:
            center_type = center['type']
            condition_1 = (center['open'] == 'yes')
            num_trainee_in_center = sum(center['trainee'].values())
            condition_2 = (num_trainee_in_center < max_capacity[center_type])
            if condition_1 and condition_2:
                each_center_take_in.append(random.randint(0, 50))
            else:
                each_center_take_in.append(0)

    def assess_availability(self):
        # Assessing whether our center can take the sample number of trainees
        for center, num_take_in in zip(self.all_centers, each_center_take_in):
            center_type = center['type']
            available_num = max_capacity[center_type] - sum(center["trainee"].values()) - num_take_in
            if available_num > 0:
            # Center is still available
                self.available_num_lg_0()
            elif available_num == 0:
            # If they're equal the center is full
                self.available_num_eq_0()
            else:
            # For when sampled number of trainees exceeded the center capacity
                self.available_num_ls_0()
    def available_num_lg_0(self):
        pass

    def available_num_eq_0(self):
        # if/else to determine type
        if center_type == 'tech_center':
        # tech centers: search for specific course on the waiting list and the monthly generated new list
            if waiting_list_dictionary[center["course"]] >= num_take_in:
                center["trainee"][center["course"]] += num_take_in
                waiting_list_dictionary[center["course"]] -= num_take_in
            else:
                center["trainee"][center["course"]] += waiting_list_dictionary[center["course"]]
                num_take_in -= waiting_list_dictionary[center["course"]]
                waiting_list_dictionary[center["course"]] = 0
                if monthly_trainees[center["course"]] >= num_take_in:
                    center["trainee"][center["course"]] += num_take_in
                    monthly_trainees[center["course"]] = 0
                else:
                    center["trainee"][center["course"]] +=  monthly_trainees[center["course"]]
                    monthly_trainees[center["course"]] = 0
        else:
            pass

        # training_hubs or bootcamps: search waiting list and then generated if still not full



    def available_num_ls_0(self):
        pass

            # If the trainee_num is more than the space available in the center, the center will simply not accept it


        # If all centers are full return the trainees to the waiting_list




        # randomly generated trainees need to be allocated to the course types of the waiting_list








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
    print(obj.all_centers)

