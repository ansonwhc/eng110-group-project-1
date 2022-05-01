from multiprocessing.connection import wait
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
        for i in range(len(self.all_centers)):
            for key, value in self.all_centers[i]["trainee"][11].items():
                        self.trainee_obj.bench[key] += value
                        self.all_centers[i]["trainee"][11][key] = 0
            
            # This moves all items in the list to the right (representing a month being added to each trainee)
            self.all_centers[i]["trainee"] = [self.all_centers[i]["trainee"][-1]] + self.all_centers[i]["trainee"][:-1]
            # As trainees have been moved to the bench, the centre may no longer be full.
            total_sum = sum([sum(dictonary.values()) for dictonary in self.all_centers[i]["trainee"]])
            if self.all_centers[i]["type"] == "tech_center" and total_sum < 200:
                self.all_centers[i]["full"] = "no"
            elif self.all_centers[i]["type"] == "bootcamp" and total_sum < 500:
                self.all_centers[i]["full"] = "no"
            elif self.all_centers[i]["type"] == "training_hub" and total_sum < 100:
                self.all_centers[i]["full"] = "no"

    def create_distribution_list(self):
        self.distribute_trainees_list = []
        # Shuffles the centers list for good measure (shuffle randomises the order of items in the list)
        random.shuffle(self.all_centers)
        for course in self.all_centers:
            self.distribute_trainees_list.append(random.randrange(0, 51))

    def distribute_trainees(self, dictionary_with_trainees, distributed_waiting_list=False, redistribute_from_closed_centers=False, waiting_list_index=0):
        # The waiting list has priority. We must try and distribute trainees from this list first.
        for idx, center in enumerate(self.all_centers):

            if center["open"] == "no" or center["full"] == "yes":
                continue

            num_trainees_to_distribute = self.distribute_trainees_list[idx]

            if center["type"] == "tech_center":
                center_course = center["course"]
                new_total = min(dictionary_with_trainees[center_course], num_trainees_to_distribute) + sum([sum(dictonary.values()) for dictonary in self.all_centers[idx]["trainee"]])
                if new_total >= 200:
                    self.all_centers[idx]["full"] = "yes"
                    difference = new_total - 200
                    self.all_centers[idx]["trainee"][waiting_list_index][center_course] += difference
                    dictionary_with_trainees[center_course] -= difference
                    self.distribute_trainees_list[idx] -= difference
                elif num_trainees_to_distribute >= dictionary_with_trainees[center_course]:
                        self.all_centers[idx]["trainee"][waiting_list_index][center_course] += dictionary_with_trainees[center_course]
                        self.distribute_trainees_list[idx] -= dictionary_with_trainees[center_course]
                        dictionary_with_trainees[center_course] = 0
                elif num_trainees_to_distribute < dictionary_with_trainees[center_course]:
                    self.all_centers[idx]["trainee"][waiting_list_index][center_course] += num_trainees_to_distribute
                    dictionary_with_trainees[center_course] -= num_trainees_to_distribute
                    self.distribute_trainees_list[idx] = 0

                if distributed_waiting_list == True:
                    self.update_center_closed_and_full(dictionary_with_trainees, idx)

            elif center["type"] == "bootcamp":
                self.distribute_random_roles(dictionary_with_trainees, idx, waiting_list_index)
                total_sum = sum([sum(dictonary.values()) for dictonary in self.all_centers[idx]["trainee"]])
                if total_sum >= 500:
                    self.all_centers[idx]["full"] = "yes"
                    num_return = total_sum - 500
                    self.return_trainees(dictionary_with_trainees, num_return, idx, distributed_waiting_list)
                else:
                    self.all_centers[idx]["full"] = "no"

                if distributed_waiting_list == True and redistribute_from_closed_centers == False:
                    self.update_center_closed_and_full(dictionary_with_trainees, idx)

            elif center["type"] == "training_hub":
                self.distribute_random_roles(dictionary_with_trainees, idx, waiting_list_index)
                total_sum = sum([sum(dictonary.values()) for dictonary in self.all_centers[idx]["trainee"]])
                if total_sum >= 100:
                    self.all_centers[idx]["full"] = "yes"
                    num_return = total_sum - 100
                    self.return_trainees(dictionary_with_trainees, num_return, idx, distributed_waiting_list)
                else:
                    self.all_centers[idx]["full"] = "no"

                if distributed_waiting_list == True:
                    self.update_center_closed_and_full(dictionary_with_trainees, idx)

        if distributed_waiting_list == False:
            if waiting_list_index == 11:
                return
            else:
                self.distribute_trainees(self.trainee_obj.waiting_list[waiting_list_index+1], False, False, waiting_list_index + 1)
        if distributed_waiting_list == True and redistribute_from_closed_centers == False:
            self.distribute_trainees(dictionary_with_trainees, True, True)
        elif distributed_waiting_list == True and redistribute_from_closed_centers == True:
            self.push_to_waiting_list(dictionary_with_trainees)

    def push_to_waiting_list(self, trainee_dictionary):
        for trainee_key in trainee_dictionary.keys():
            self.trainee_obj.waiting_list[0][trainee_key] += trainee_dictionary[trainee_key]

    def update_center_closed_and_full(self, dictionary_with_trainees, idx):
        total_sum = sum([sum(dictonary.values()) for dictonary in self.all_centers[idx]["trainee"]])
        if self.all_centers[idx]["type"] == "tech_center":
            if total_sum < 25:
                self.all_centers[idx]["open"] = "no"
                self.all_centers[idx]["full"] = "no"
                self.return_trainees(dictionary_with_trainees, total_sum, idx)
            elif total_sum < 200:
                self.all_centers[idx]["full"] = "no"
        elif self.all_centers[idx]["type"] == "bootcamp":
            if total_sum < 25:
                if self.all_centers[idx]["months_less_than_25"] == 2:
                    self.all_centers[idx]["open"] = "no"
                    self.all_centers[idx]["full"] = "no"
                    self.all_centers[idx]["months_less_than_25"] = 3
                    self.return_trainees(dictionary_with_trainees, total_sum, idx)
                else:
                    self.all_centers[idx]["months_less_than_25"] += 1
            elif total_sum < 500:
                self.all_centers[idx]["full"] = "no"
                self.all_centers[idx]["months_less_than_25"] = 0
        elif self.all_centers[idx]["type"] == "training_hub":
            if total_sum < 25:
                self.all_centers[idx]["open"] = "no"
                self.all_centers[idx]["full"] = "no"
                self.num_open_training_hubs -= 1
                self.return_trainees(dictionary_with_trainees, total_sum, idx)
            elif total_sum < 100:
                self.all_centers[idx]["full"] = "no"

    def distribute_random_roles(self, dictionary, center_idx, waiting_list_index):
        if self.distribute_trainees_list[center_idx] >= sum(dictionary.values()):
            for role in dictionary.keys():
                self.all_centers[center_idx]["trainee"][waiting_list_index][role] += dictionary[role]
                self.distribute_trainees_list[center_idx] -= dictionary[role]
                dictionary[role] = 0 
        else:
            while self.distribute_trainees_list[center_idx] != 0:
                sampled_role = random.choice([key for key in dictionary if dictionary[key] > 0])
                num_taken = random.randrange(1, dictionary[sampled_role] + 1)
                if num_taken >= self.distribute_trainees_list[center_idx]:
                    num_taken = self.distribute_trainees_list[center_idx]
                    self.all_centers[center_idx]["trainee"][waiting_list_index][sampled_role] += num_taken
                    dictionary[sampled_role] -= num_taken
                    self.distribute_trainees_list[center_idx] = 0
                else:
                    self.all_centers[center_idx]["trainee"][waiting_list_index][sampled_role] += num_taken
                    self.distribute_trainees_list[center_idx] -= num_taken
                    dictionary[sampled_role] -= num_taken

    def return_trainees(self, dictionary_to_add_trainees, num_trainees, center_idx, return_from_month=0, distributed_waiting_list=True):
        if distributed_waiting_list == False:
            dictionary_to_add_trainees = self.trainee_obj.waiting_list[return_from_month]
        repeat_function = False
        while num_trainees != 0:
            keys_left = [key for key in self.all_centers[center_idx]["trainee"][return_from_month] if self.all_centers[center_idx]["trainee"][return_from_month][key] > 0]
            if keys_left == [] and num_trainees != 0:
                repeat_function = True
                break
            sampled = random.choice(keys_left)
            num_moved = random.randrange(1, self.all_centers[center_idx]["trainee"][return_from_month][sampled] + 1)
            if num_moved >= num_trainees:
                num_moved = num_trainees
                self.all_centers[center_idx]["trainee"][return_from_month][sampled] -= num_moved
                dictionary_to_add_trainees[sampled] += num_moved
                num_trainees = 0
            elif num_trainees > num_moved:
                num_trainees -= num_moved
                self.all_centers[center_idx]["trainee"][return_from_month][sampled] -= num_moved
                dictionary_to_add_trainees[sampled] += num_moved     
        if repeat_function == True:
            self.return_trainees(dictionary_to_add_trainees, num_trainees, center_idx, return_from_month + 1, distributed_waiting_list)