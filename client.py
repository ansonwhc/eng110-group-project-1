import random

class Client:
    def __init__(self):
        self.client_list = []

    def generate_client(self):
        # Generate client as dictionary and then appends it to client_list
        new_client = {"requirements": (random.randint(15, 30), random.choice(["Java", "C#", "Data", "DevOps", "Business"])),
                      "num_of_trainees": 0,
                      "happy": True}
        self.client_list.append(new_client)

    def update_num_of_trainees(self, trainee_obj):
        for idx in range(len(self.client_list)):
            if self.client_list[idx]["happy"] == False:
                continue
            # Generates a random number of trainees they will take for the month
            random_number = random.randint(1, self.client_list[idx]["requirements"][0])

            if trainee_obj.bench[self.client_list[idx]["requirements"][1]] >= random_number:
                self.client_list[idx]["num_of_trainees"] += random_number
                trainee_obj.bench[self.client_list[idx]["requirements"][1]] -= random_number
            else:
                self.client_list[idx]["num_of_trainees"] += trainee_obj.bench[self.client_list[idx]["requirements"][1]]
                trainee_obj.bench[self.client_list[idx]["requirements"][1]] = 0

    def update_when_requirements_not_met(self, trainee_obj):
        # Checks if client has required trainees at the end of twelve months, and changes "happy" to False if not.
        for idx in range(len(self.client_list)):
            if self.client_list[idx]["num_of_trainees"] < self.client_list[idx]["requirements"][0]:
                self.client_list[idx]["happy"] = False
                # Adds all the trainees back to the bench
                trainee_obj.bench[self.client_list[idx]["requirements"][1]] += self.client_list[idx]["num_of_trainees"]
                self.client_list[idx]["num_of_trainees"] = 0 

    def update_returning_clients(self):
        for idx in range(len(self.client_list)):
            if self.client_list[idx]["happy"] == True:
                self.client_list[idx]["num_of_trainees"] = 0