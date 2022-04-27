import random


class Trainee:
    pass

    # generate method for trainee class to calculate random number between 50-100 to decide how many trainees
    def generate_new_trainees(self):
        # generate number between 50-100
        num = random.randint(50, 100)

        # create dictionary for group
        dict = {
            "Java": 0,
            "C#": 0,
            "Data": 0,
            "DevOps": 0,
            "Business": 0
        }

        # random assignment of students to courses
        for trainee in range(num):
            course = random.randint(1, 5)
            if course == 1:
                dict['Java'] += 1
            elif course == 2:
                dict['C#'] += 1
            elif course == 3:
                dict['Data'] += 1
            elif course == 4:
                dict['DevOps'] += 1
            elif course == 5:
                dict['Business'] += 1
        return dict




trainee1 = Trainee()
print(trainee1.generate_new_trainees())

    # for the trainee class assign trainees to their course, and outputs a dictionary