from tkinter import *
from simulator import Simulator


class SimulationInterface:
    def __init__(self,
                 window_size: str = "600x400",
                 monthly_output=False):
        """
        TK interface for running simulations

        :param window_size: intxint, default: 600x400
        :return: TK_interface window
        """
        # TODO: No implementation on prompting user for errors, e.g. input != numeric
        self.window_size = window_size
        self.simulator = Simulator()   # this basically does nothing but to initialise the class, ugly, but MVP
        self.monthly_output = monthly_output
        self.create_window()

    def export_popup(self):
        """pop-up window for setting export_file name nad pressing the <export> button"""
        export_win = Toplevel()
        export_win.geometry('300x100')
        export_win.wm_title("Export to csv")

        Label(export_win, text="File name:").place(relx=0.15, rely=0.15, anchor=CENTER)

        self.file_name_var = StringVar()
        self.file_name_var.set("simulation record")

        Entry(export_win, textvariable=self.file_name_var)\
            .place(relx=0.5, rely=0.4, anchor=CENTER, width=250)

        Button(export_win, text="Export",
               command=lambda: (self.simulator.export_to_csv(self.file_name_var.get()), export_win.destroy()))\
            .place(relx=0.7, rely=0.9, anchor="se")

        Button(export_win, text="Cancel", command=export_win.destroy)\
            .place(relx=0.9, rely=0.9, anchor="se")

    def final_output(self):
        sim_result, sim_info = self.simulator.result, self.simulator.simulation_info

        # set variables for TK_instance's Label objects
        pretty_result = '\n'.join([f"{key}: {value}" for key, value in sim_result.items()])  # prettifying
        pretty_info = '\n'.join([f"{key}: {value}" for key, value in sim_info.items()])
        self.result_var.set(pretty_result)
        self.info_var.set(pretty_info)

        # result_label
        Label(self.root, textvariable=self.result_var) \
            .place(relx=0.5, rely=0.5, anchor=CENTER)

        # simulation_info
        Label(self.root, textvariable=self.info_var) \
            .place(relx=0.5, rely=0.7, anchor=CENTER)

        Button(self.root, text='Export to csv', command=self.popup_bonus) \
            .place(relx=0.9, rely=0.9, anchor="se")

        # reset input
        self.duration_var.set("")

    def monthly_output(self):
        # print monthly progress
        # get data at the end - maybe call self.final_output()

        pass

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

        # TODO: print 'Please input an integer' if simulator.input is TypeError
        if self.monthly_output:
            pass

        else:
            self.simulator.reset(duration)
            self.simulator.record()
            self.final_output()

    def create_window(self):
        # TODO: think there should be a better way than using the method place(),
        #  maybe pack() or grid()? \
        #  Because right now it is using relative position rather than absolute

        # create an instance of the Tk class
        self.root = Tk()

        # format the initial windows size
        self.root.geometry(self.window_size)

        # set variables
        self.duration_var = StringVar()
        self.result_var = StringVar()
        self.info_var = StringVar()

        # input_label
        Label(self.root, text="Enter Here:")\
            .place(relx=0.5, rely=0.2, anchor=CENTER)

        # input_box
        Entry(self.root, textvariable=self.duration_var)\
            .place(relx=0.5, rely=0.25, anchor=CENTER)

        # button for when user is ready to run the sim
        Button(self.root, text='Run simulation', command=self.run_sim)\
            .place(relx=0.5, rely=0.35, anchor=CENTER)

        self.root.mainloop()


def main():
    SimulationInterface()


if __name__ == "__main__":
    main()
