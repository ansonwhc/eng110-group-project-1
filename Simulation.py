class Simulator:
    def __init__(self,
                 duration: int,
                 **kwargs):
        # for now, we only have duration as input (monthly expected)
        self.duration = duration

        # this is for when we need to pass more different variables to methods
        for key, value in kwargs.items():
            setattr(self, key, value)

        # TODO: add internal variables

        # This is purely for easy TK interface access for now
        self.result, self.sim_info = self.simulate()

    def simulate(self):
        sim_info = f"\
        Simulation info:\n\
        Duration: {self.duration} months\n\
        "

        num_centres = int(min([self.duration * 75 / 100,
                               self.duration/2]))

        num_full_centres = int(min([self.duration * 75 // 100,
                                    num_centres]))

        num_training_trainees = int(min([self.duration * 75,
                                         num_centres * 100]))

        num_waiting_trainees = self.duration * 75 - num_training_trainees
        result = f"\
        (Demo) Number of open centres: {num_centres}\n\
        (Demo) Number of full centres: {num_full_centres}\n\
        (Demo) Number of trainees in training: {num_training_trainees}\n\
        (Demo) Number of trainees on the waiting list: {num_waiting_trainees}"
        # print(sim_info)

        return result, sim_info

    def random_num_trainee_generator(self) -> int:
        # generate a random int [50-100]
        # TODO: set lower_bound, and upper_bound for randint
        pass

    def random_num_trainee_acceptance(self) -> int:
        # generate a random int [0-50]
        # TODO: set lower_bound, and upper_bound for randint
        pass
