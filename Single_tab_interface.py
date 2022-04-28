from tkinter import *
from simulator import Simulator


class SimulationInterface:
    def __init__(self,
                 window_size: str = "600x400"):
        """
        TK interface for running simulations
        """
        # TODO: No implementation on prompting user for errors, e.g. input != numeric
        self.window_size = window_size
        self.simulator = Simulator()
        self.create_window()

    def export_popup(self):
        """pop-up window for setting export_file name nad pressing the <export> button"""
        export_win = Toplevel()
        export_win.geometry('300x100')
        export_win.wm_title("Export to csv")

        Label(export_win, text="File name:").place(relx=0.15, rely=0.15, anchor=CENTER)

        self.file_name_var = StringVar()
        self.file_name_var.set("simulation_record")

        Entry(export_win, textvariable=self.file_name_var)\
            .place(relx=0.5, rely=0.4, anchor=CENTER, width=250)

        Button(export_win, text="Export",
               command=lambda: (self.simulator.export_to_csv(self.file_name_var.get()), export_win.destroy()))\
            .place(relx=0.7, rely=0.9, anchor="se")

        Button(export_win, text="Cancel", command=export_win.destroy)\
            .place(relx=0.9, rely=0.9, anchor="se")

    def update_output(self):
        sim_result, sim_info = self.simulator.current_month_output, self.simulator.simulation_info

        # set variables for TK_instance's Label objects
        pretty_result = '\n'.join([f"{key}: {value}" for key, value in sim_result.items()])  # prettifying
        pretty_info = '\n'.join([f"{key}: {value}" for key, value in sim_info.items()])   # prettifying
        self.result_var.set(pretty_result)
        self.info_var.set(pretty_info)

        # result_label
        Label(self.root, textvariable=self.result_var)\
            .place(relx=0.5, rely=0.5, anchor=CENTER)

        # simulation_info_label
        Label(self.root, textvariable=self.info_var)\
            .place(relx=0.5, rely=0.7, anchor=CENTER)

        # bring up a pop-up window to confirm export
        Button(self.root, text='Export to csv', command=self.export_popup)\
            .place(relx=0.9, rely=0.9, anchor="se")

        # reset input
        self.duration_var.set("")

    def run_sim(self):
        # get user input
        # .get() returns str only?, https://www.tutorialspoint.com/python/tk_entry.htm
        self.monthly_output = False
        duration = self.duration_var.get()
        # self.simulator.record(duration)

        # TODO: print 'Please input an integer' if simulator.input is TypeError
        # assume self.monthly_output is a check box for the user to tick, such that if being checked, the
        # *run-simulation button* will display the monthly result
        # if var1:
        #     Button(self.root, text='123')\
        #         .place(relx=0.9, rely=0.9, anchor="se")
        #
        #     # when checked
        #         # self.simulator.month_simulation()
        #         # Label(textvariable = self.simulator.current_month_output)
        #     pass
        #
        # else:
        #     # self.simulator.duration_simulation()
        #     # Label(self.simulator.current_month_output OR self.history)
        #     # self.simulator.reset(duration)
        #     # self.simulator.record()
        #     # self.final_output()
        #     pass

    def set_simulate_month(self):
        # set self.simulate_next_month to its opposite boolean
        self.simulate_next_month = not self.simulate_next_month
        if self.simulate_next_month:
            self.run_simulation_button_text_var.set("Simulate Next Month")
        else:
            self.run_simulation_button_text_var.set("Run Simulation")

    def create_window(self):
        # TODO: think there should be a better way than using the method place(),
        #  maybe pack() or grid()? \
        #  Because right now it is using relative position rather than absolute

        # create an instance of the Tk class
        self.root = Tk()

        # format the initial windows size
        self.root.geometry(self.window_size)

        # set variables
        self.simulate_next_month = False # whether to simulate full duration or just next month
        self.duration_var = StringVar()
        self.result_var = StringVar()
        self.info_var = StringVar()
        self.sim_next_month_box = IntVar()
        self.run_simulation_button_text_var = StringVar()
        self.run_simulation_button_text_var.set("Run Simulation")

        # checking and un-checking still activates the function
        self.sim_next_month_checkbox = Checkbutton(self.root, text="Simulate next month",
                                                  variable=self.sim_next_month_box,
                                                  command=self.set_simulate_month)
        self.sim_next_month_checkbox.grid(row=0, sticky='e')

        # input_label - for running whole sim
        self.duration_input_label = Label(self.root, text="Enter Month Here:")
        self.duration_input_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        # input_box - if monthly-checkbox is checked, the entry does nothing (preferred)
        self.duration_input_entry = Entry(self.root, textvariable=self.duration_var)
        self.duration_input_entry.place(relx=0.5, rely=0.25, anchor=CENTER)

        # button for when user is ready to run the sim
        self.run_simulation_button = Button(self.root,
                                            textvariable=self.run_simulation_button_text_var,
                                            command=self.run_sim)
        self.run_simulation_button.place(relx=0.5, rely=0.35, anchor=CENTER)

        self.root.mainloop()


def main():
    SimulationInterface()


if __name__ == "__main__":
    main()
