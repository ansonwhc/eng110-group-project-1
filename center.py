import random
from trainee import Trainee

class Center():

    def __init__(self):
        self.trainee_obj = Trainee()
        self.all_centers = []
        self.distribute_trainees_list = []
        self.num_bootcamps = 0
        self.num_open_training_hubs = 0
        self.can_open_training_hub = True
        self.can_open_bootcamp = True

    def get_random_available_center(self):
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
        trainee_list = []
        for i in range(12):
            trainee_list.append({"Java": 0, "C#": 0, "Data": 0, "DevOps": 0, "Business": 0})

        random_num = self.get_random_available_center()
        # Training hub
        if random_num == 1:
            self.all_centers.append({"type": "training_hub", "open": "yes", "full": "no", "trainee": trainee_list})
            self.num_open_training_hubs += 1
        # Bootcamp
        elif random_num == 2:
            self.all_centers.append({"type": "bootcamp", "open": "yes", "full": "no", "months_less_than_25": 0, "trainee": trainee_list})
            self.num_bootcamps += 1
        # Tech center
        elif random_num == 3:
            # Determines what course the tech center will be teaching
            course = random.choice(["Java", "C#", "Data", "DevOps", "Business"])
            self.all_centers.append({"type": "tech_center", "open": "yes", "full": "no", "type": "tech_center", "course": course, "trainee": trainee_list})

    def update_months_trained(self):
        for i in range(self.all_centers):
            for key, value in self.all_centers[i]["trainee"][11].items():
                        self.trainee_obj.bench[key] += value
                        self.all_centers[i]["trainee"][11][key] = 0
            
            # This moves all items in the list to the right (representing a month being added to each trainee)
            self.all_centers[i]["trainee"] = [self.all_centers[i]["trainee"][-1]] + self.all_centers[i]["trainee"][:-1]

    def create_distribution_list(self):
        self.distribute_trainees_list = []
        # Shuffles the centers list for good measure (shuffle randomises the order of items in the list)
        random.shuffle(self.all_centers)
        for course in self.all_centers:
            self.distribute_trainees_list.append(random.randrange(0, 51))

    def distribute_trainees(self, dictionary_with_trainees, distributed_waiting_list=False, redistribute_from_closed_centers=False):
        # The waiting list has priority. We must try and distribute trainees from this list first.

        for idx, center in enumerate(self.all_centers):

            if center["open"] == "no" or center["full"] == "yes":
                continue

            num_trainees_to_distribute = self.distribute_trainees_list[idx]

            if center["type"] == "tech_center":
                center_course = center["course"]
                new_total = min(dictionary_with_trainees[center_course], num_trainees_to_distribute) + sum([dictonary[center_course] for dictonary in self.all_centers[idx]["trainee"]])
                if new_total >= 200:
                    self.all_centers[idx]["full"] = "yes"
                    difference = new_total - 200
                    self.all_centers[idx]["trainee"][0][center_course] += difference
                    dictionary_with_trainees[center_course] -= difference
                    self.distribute_trainees_list[idx] -= difference
                elif num_trainees_to_distribute >= dictionary_with_trainees[center_course]:
                        self.all_centers[idx]["trainee"][0][center_course] += dictionary_with_trainees[center_course]
                        self.distribute_trainees_list[idx] -= dictionary_with_trainees[center_course]
                        dictionary_with_trainees[center_course] = 0
                elif num_trainees_to_distribute < dictionary_with_trainees[center_course]:
                    self.all_centers[idx]["trainee"][0][center_course] += num_trainees_to_distribute
                    dictionary_with_trainees[center_course] -= num_trainees_to_distribute
                    self.distribute_trainees_list[idx] = 0

                if distributed_waiting_list == True:
                    if self.all_centers[idx]["trainee"][center_course] < 25:
                        self.all_centers[idx]["open"] = "no"
                        self.return_trainees(dictionary_with_trainees, self.all_centers[idx]["trainee"][0][center_course], idx)

            elif center["type"] == "bootcamp":
                self.distribute_random_roles(dictionary_with_trainees, idx)
                total_sum = sum([sum(dictonary.values()) for dictonary in self.all_centers[idx]["trainee"]])
                if total_sum >= 500:
                    self.all_centers[idx]["full"] = "yes"
                    num_return = total_sum - 500
                    self.return_trainees(dictionary_with_trainees, num_return, idx)
                
                if distributed_waiting_list == True and redistribute_from_closed_centers == False:
                    if total_sum < 25:
                        if self.all_centers[idx]["months_less_than_25"] == 2:
                            self.all_centers[idx]["open"] = "no"
                            self.all_centers[idx]["months_less_than_25"] = 0
                            self.return_trainees(dictionary_with_trainees, total_sum, idx, True)
                        else:
                            self.all_centers[idx]["months_less_than_25"] += 1

            elif center["type"] == "training_hub":
                self.distribute_random_roles(dictionary_with_trainees, idx)
                total_sum = sum([sum(dictonary.values()) for dictonary in self.all_centers[idx]["trainee"]])
                if total_sum >= 100:
                    self.all_centers[idx]["full"] = "yes"
                    num_return = total_sum - 100
                    self.return_trainees(dictionary_with_trainees, num_return, idx)

                if distributed_waiting_list == True:
                    if total_sum < 25:
                        self.all_centers[idx]["open"] = "no"
                        self.num_open_training_hubs -= 1
                        self.return_trainees(dictionary_with_trainees, total_sum, idx)

        if distributed_waiting_list == True and redistribute_from_closed_centers == False:
            self.distribute_trainees(dictionary_with_trainees, True, True)
        elif distributed_waiting_list == True and redistribute_from_closed_centers == True:
            self.push_to_waiting_list(dictionary_with_trainees)

    def push_to_waiting_list(self, trainee_dictionary):
        for trainee_key in trainee_dictionary.keys():
            self.trainee_obj.waiting_list_dictionary[trainee_key] += trainee_dictionary[trainee_key]

    def distribute_random_roles(self, dictionary, center_idx):
        num_trainees_to_distribute = self.distribute_trainees_list[center_idx]
        if num_trainees_to_distribute >= sum(dictionary.values()):
            for role in dictionary.keys():
                self.all_centers[center_idx]["trainee"][0][role] += dictionary[role]
                num_trainees_to_distribute -= dictionary[role]
                dictionary[role] = 0 
        else:
            while num_trainees_to_distribute != 0:
                sampled_role = random.choice([key for key in dictionary if dictionary[key] > 0])
                num_taken = random.randrange(1, dictionary[sampled_role] + 1)
                if num_taken >= num_trainees_to_distribute:
                    num_taken = num_trainees_to_distribute
                    self.all_centers[center_idx]["trainee"][0][sampled_role] += num_taken
                    dictionary[sampled_role] -= num_taken
                    num_trainees_to_distribute = 0
                else:
                    self.all_centers[center_idx]["trainee"][0][sampled_role] += num_taken
                    num_trainees_to_distribute -= num_taken
                    dictionary[sampled_role] -= num_taken

    def return_trainees(self, dictionary_to_add_trainees, num_trainees, center_idx, closed_bootcamp=False, return_from_month=0):
        while num_trainees != 0:
            keys_left = [key for key in self.all_centers[center_idx]["trainee"][return_from_month] if self.all_centers[center_idx]["trainee"][return_from_month][key] > 0]
            if keys_left == []:
                break
            sampled = random.choice(keys_left)
            num_moved = random.randrange(1, self.all_centers[center_idx]["trainee"][return_from_month][sampled] + 1)
            if num_moved >= num_trainees:
                num_moved = num_trainees
                self.all_centers[center_idx]["trainee"][return_from_month][sampled] -= num_moved
                dictionary_to_add_trainees[sampled] += num_moved
                num_trainees = 0
            else:
                num_trainees -= num_moved
                self.all_centers[center_idx]["trainee"][return_from_month][sampled] -= num_moved
                dictionary_to_add_trainees[sampled] += num_moved     

        if return_from_month == 3:
            return
        if closed_bootcamp == True:
            self.return_trainees(dictionary_to_add_trainees, num_trainees, center_idx, True, return_from_month + 1)

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

