# Programme pseudocode

# input (sim_duration: int)
#   sim_duration: in months

class Simulator:
    def __init__(self,
                 duration : int,
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
        result = 'Nothing for now'
        sim_info = f"Input: {self.duration}"
        # print(sim_info)

        return result, sim_info

    def random_num_trainee_generator(self) -> int:
        # generate a random int [50-100]
        # TODO: accept randint range as an input
        pass
