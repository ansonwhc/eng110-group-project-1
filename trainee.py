import random
class Trainee:

    def __init__(self):
        self.waiting_list_dictionary = {"Java": 0, "C#": 0, "Data": 0, "DevOps": 0, "Business": 0}
        self.bench = {"Java": 0, "C#": 0, "Data": 0, "DevOps": 0, "Business": 0}
        self.generated_trainees = {}

    def generate_new_trainees(self):

        # Generates a number between 50-100.
        num = random.randint(50, 100)
        # Creates dictionary for group.
        self.generated_trainees = {"Java": 0, "C#": 0, "Data": 0, "DevOps": 0, "Business": 0}

        # Randomly assigns students to courses.
        for i in range(num):
            course = random.randint(1, 5)
            if course == 1:
                self.generated_trainees['Java'] += 1
            elif course == 2:
                self.generated_trainees['C#'] += 1
            elif course == 3:
                self.generated_trainees['Data'] += 1
            elif course == 4:
                self.generated_trainees['DevOps'] += 1
            elif course == 5:
                self.generated_trainees['Business'] += 1
