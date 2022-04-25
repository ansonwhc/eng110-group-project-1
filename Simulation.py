# Programme pseudocode

# input (sim_duration: int)
#   sim_duration: in months

class Simulator:
    def __init__(self,
                 duration : int,
                 **kwargs):
        # for now, we only have duration as input (monthly expected)
        self.duration = duration
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.result = self.simulate()
        # TODO: add internal variables

    def simulate(self):
        # print(f"Running Simulation, duration {self.duration}")

        result = "some result"
        return result

    def random_num_trainee_generator(self) -> int:
        # generate a random int [50-100]
        # TODO: accept randint range as an input
        pass
