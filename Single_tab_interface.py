from tkinter import *
from simulator import Simulator


class SimulationInterface:
    def __init__(self,
                 window_size: str = "800x600"):
        """
        TK interface for running simulations
        """

        self.window_size = window_size
        self.simulator = Simulator()
        self.create_window()

        self.duration_input_entry = None
        self.duration_input_label = None
        self.sim_next_month_checkbox = None
        self.run_simulation_button_text_var = None
        self.sim_next_month_box = None
        self.info_var = None
        self.result_var = None
        self.duration_var = None
        self.month_simulated_var = None
        self.root = None
        self.result_box = None
        self.backward_button = None
        self.forward_button = None
        self.backward_a_month = None
        self.run_simulation_button = None
        self.forward_a_month = None
        self.current_month = None
        self.num_months = None
        self.all_month_result = None
        self.monthly_result = None
        self.export_button = None
        self.file_name_var = None
        self.simulate_next_month = None

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

    def display_export_button(self):
        # bring up a pop-up window to confirm export
        self.export_button = Button(self.root, text='Export to csv', command=self.export_popup)
        self.export_button.place(relx=0.9, rely=0.9, anchor="se")

    def display_next_month_output(self):
        self.display_export_button()
        self.monthly_result = self.simulator.current_month_output
        # prettify
        pretty_text = self.prettify_monthly_output(self.monthly_result, True)
        self.result_var.set(pretty_text)

    def prettify_monthly_output(self, result_dict, top=False):
        if not isinstance(result_dict, dict):
            return result_dict
        top_level = '{}\n{}'
        sub_level = '{}: {}'
        if top:
            level = top_level
        else:
            level = sub_level
        pretty = '\n'.join(level.format(k, self.prettify_monthly_output(d))
                           for k, d in result_dict.items())

        return pretty

    def display_all_output(self):
        self.all_month_result = self.simulator.history
        if self.all_month_result:
            self.display_export_button()
            self.num_months = len(self.all_month_result)
            self.current_month = 0
            self.forward_a_month = (self.current_month + 1 == self.num_months)
            self.backward_a_month = (self.current_month == 0)

            pretty_text = self.prettify_monthly_output(self.all_month_result[self.current_month], True)
            self.result_var.set(f"Current month {self.current_month + 1}\n {pretty_text}")

            self.forward_button = Button(text="Show next month result",
                                         command=self.display_forward_a_month)
            self.forward_button.place(relx=0.8, rely=0.8, anchor="e")
            self.backward_button = Button(text="Show last month result",
                                          command=self.display_backward_a_month)
            self.backward_button.place(relx=0.7, rely=0.7, anchor="e")

        else:
            self.result_var.set("Input is not recognised, please input an integer")
            self.duration_var.set("")

    def display_forward_a_month(self):
        if self.current_month + 1 < self.num_months:
            self.current_month += 1
            pretty_text = self.prettify_monthly_output(self.all_month_result[self.current_month], True)
            self.result_var.set(pretty_text)

    def display_backward_a_month(self):
        if self.current_month > 0:
            self.current_month -= 1
            pretty_text = self.prettify_monthly_output(self.all_month_result[self.current_month], True)
            self.result_var.set(pretty_text)

    def run_sim(self):
        # result_label
        self.result_box = Label(self.root, textvariable=self.result_var, anchor="e", justify=LEFT)
        self.result_box.place(relx=0.5, rely=0.5, anchor=CENTER)

        # # simulation_info_label
        # Label(self.root, textvariable=self.info_var) \
        #     .place(relx=0.5, rely=0.7, anchor=CENTER)

        # get user input
        # .get() returns str only?, https://www.tutorialspoint.com/python/tk_entry.htm
        if self.simulate_next_month:
            open_new_center = ((int(self.month_simulated_var.get()) + 1) % 2 == 0)
            self.simulator.month_simulation(open_new_center)
            self.display_next_month_output()

        else:
            duration = self.duration_var.get()
            self.simulator.duration_simulation(duration)
            self.display_all_output()

    def set_simulate_month(self):
        # set self.simulate_next_month to its opposite boolean
        self.simulate_next_month = not self.simulate_next_month
        if self.simulate_next_month:
            self.run_simulation_button_text_var.set("Simulate Next Month")
            self.duration_var.set("Input here will not will valid")
            try:
                self.forward_button.destroy()
                self.backward_button.destroy()
                self.result_var.set("")
            except AttributeError:
                pass
        else:
            self.run_simulation_button_text_var.set("Run Simulation")
            self.duration_var.set("")

    def reset_month_simulated(self):
        self.month_simulated_var.set("0")

    def create_window(self):
        # TODO: think there should be a better way than using the method place(),
        #  maybe pack() or grid()? \
        #  Because right now it is using relative position rather than absolute

        # create an instance of the Tk class
        self.root = Tk()
        self.month_simulated_var = StringVar()
        self.month_simulated_var.set("0")

        # format the initial windows size
        self.root.geometry(self.window_size)

        # set variables
        self.simulate_next_month = False  # whether to simulate full duration or just next month
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
        self.duration_input_entry = Entry(self.root, textvariable=self.duration_var, width=30)
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
