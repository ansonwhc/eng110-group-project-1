import random
class Client:
    def __init__(self):
        self.client_list = []

    def generate_client(self):
        # Generate client as dictionary and then appends it to client_list
        new_client = {"client_num": len(self.client_list) + 1,
                      "requirements": (random.randint(15, 30), random.choice(["Java", "C#", "Data", "DevOps", "Business"])),
                      "num_of_trainees": 0,
                      "happy": False}
        self.client_list.append(new_client)

    def update_num_of_trainees(self, client, num):
        # Add num to client["num_of_clients"]
        # Assumption: trainee class handles checking that num <= spaces available.
        client["num_of_clients"] += num


client1 = Client()
