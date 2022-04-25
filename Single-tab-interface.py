from tkinter import *


class Simulator:
    """Pretending to be the actual simulation script"""
    def __init__(self, duration):
        self.duration = duration
        self.result = None
        self.result, self.sim_info = self.simulate()

    def simulate(self):
        result = 'Nothing for now'
        sim_info = f"Input: {self.duration}"

        return result, sim_info


class SimulationInterface:
    def __init__(self):
        # TODO: No implementation on prompting user for errors, e.g. input != numeric
        self.create_window()

    def run_sim(self):
        # NOTE regarding class attributes initialisation:
        # 1. current implementation leverages the command argument in Button,
        #    where to my understanding it accepts callables, but it does not return anything.
        # 2. Since we cannot return anything within this callable, we either create a new label box,\
        #    or we need to set attributes such that the TK_instance will have access to our returned variables
        # ==> Hence the attributes setting within this method

        # get user input
        # .get() returns str only?, https://www.tutorialspoint.com/python/tk_entry.htm
        # maybe self.duration_var = IntVar() works,
        # but we have not implemented any error handling, so it doesn't help for now.
        duration = self.duration_var.get()

        # changing user input to int
        # TODO: assert duration_var isnumeric (could be done within Simulation class)
        duration = int(duration)

        # pass the input onto the class
        simulator = Simulator(duration)
        sim_result, sim_info = simulator.result, simulator.sim_info
        self.result_var.set(sim_result)
        self.info_var.set(sim_info)

        # result_label
        Label(self.root, textvariable=self.result_var)\
            .place(relx=0.5, rely=0.6, anchor=CENTER)

        # simulation_info
        Label(self.root, textvariable=self.info_var)\
            .place(relx=0.5, rely=0.65, anchor=CENTER)

        # reset input
        self.duration_var.set("")

    def create_window(self):
        # TODO: think there should be a better way than using the method place(),
        #  maybe pack() or grid()? \
        #  Because right now it is using relative position rather than absolute

        # TODO: Export button - for exporting input, simulation info, outputs

        # create an instance of the Tk class
        self.root = Tk()

        # format the initial windows size
        self.root.geometry("600x400")

        # set variables
        self.duration_var = StringVar()
        self.result_var = StringVar()
        self.info_var = StringVar()
        #
        # # create our frame
        # frame = Frame(root, width=300, height=300)
        # frame.grid(row=0, column=0, sticky="NW")

        # input_label
        Label(self.root, text="Enter Here:")\
            .place(relx=0.5, rely=0.3, anchor=CENTER)

        # input_box
        Entry(self.root, textvariable=self.duration_var)\
            .place(relx=0.5, rely=0.35, anchor=CENTER)

        # button for when user is ready to run the sim
        Button(self.root, text='Run simulation', command=self.run_sim)\
            .place(relx=0.5, rely=0.45, anchor=CENTER)

        self.root.mainloop()


if __name__ == "__main__":
    interface = SimulationInterface()
