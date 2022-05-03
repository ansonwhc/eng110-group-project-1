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

    def export_popup(self):
        """pop-up window for setting export_file name nad pressing the <export> button"""
        export_win = Toplevel()
        export_win.geometry('300x100')
        export_win.wm_title("Export to csv")

        Label(export_win, text="File name:").grid(row=0, column=0, sticky=NW)

        self.file_name_var = StringVar()
        self.file_name_var.set("simulation_record")

        Entry(export_win, textvariable=self.file_name_var)\
            .place(relx=0.5, rely=0.4, anchor=CENTER, width=250)

        Button(export_win, text="Export",
               command=lambda: (self.simulator.export_to_csv(self.file_name_var.get()),
                                export_win.destroy()))\
            .place(relx=0.7, rely=0.9, anchor="se")

        Button(export_win, text="Cancel", command=export_win.destroy)\
            .place(relx=0.9, rely=0.9, anchor="se")

    def display_export_button(self):
        # bring up a pop-up window to confirm export
        self.export_button = Button(self.root, text='Export to csv', command=self.export_popup)
        self.export_button.grid(row=4, column=0, sticky=NW, columnspan=2)

    def display_next_month_output(self):
        self.display_export_button()
        self.monthly_result = self.simulator.current_month_output
        # prettify
        pretty_text = self.prettify_monthly_output(self.monthly_result, True)
        self.result_var.set(f"Current month: {self.current_month + 1}\n{pretty_text}")

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
        if self.simulator.history:
            self.display_export_button()
            self.num_months = len(self.simulator.history)
            self.current_month = 0
            self.forward_a_month = (self.current_month + 1 == self.num_months)
            self.backward_a_month = (self.current_month == 0)

            pretty_text = self.prettify_monthly_output(self.simulator.history[self.current_month], True)
            self.result_var.set(f"Current month: {self.current_month + 1}\n{pretty_text}")
        else:
            self.result_var.set("Input is not recognised, please input an integer")
            self.duration_var.set("")

    def display_forward_a_month(self):
        # TODO: doesn't work when simulating the next month
        if not self.simulate_next_month:
            if self.current_month + 1 < self.num_months:
                self.current_month += 1
                pretty_text = self.prettify_monthly_output(self.simulator.history[self.current_month], True)
                self.result_var.set(f"Current month: {self.current_month + 1}\n{pretty_text}")

    def display_backward_a_month(self):
        # TODO: doesn't work when simulating the next month
        if not self.simulate_next_month:
            if self.current_month > 0:
                self.current_month -= 1
                pretty_text = self.prettify_monthly_output(self.simulator.history[self.current_month], True)
                self.result_var.set(f"Current month: {self.current_month + 1}\n{pretty_text}")

    def run_sim(self):
        if not self.simulate_next_month:
            self.simulator.reset_history()
        # result_label
        self.result_box = Label(self.root, textvariable=self.result_var, anchor="e", justify=LEFT)
        self.result_box.grid(row=0, column=2, sticky=NW, rowspan=10)

        # get user input
        if self.simulate_next_month:
            open_new_center = (int(self.current_month) % 2 == 0)
            self.simulator.month_simulation(open_new_center)
            self.display_next_month_output()
            self.current_month += 1

        else:
            duration = self.duration_var.get()
            self.duration_var.set("")
            self.simulator.duration_simulation(duration)
            self.display_all_output()

    def set_simulate_month(self):
        # set self.simulate_next_month to its opposite boolean (for the checkbox)
        self.simulate_next_month = not self.simulate_next_month
        self.simulator.reset_history()
        self.reset_current_month()
        if self.simulate_next_month:
            self.run_simulation_button_text_var.set("Simulate Next Month")
            self.duration_var.set("Input here will not will valid")
            self.result_var.set("")
        else:
            self.run_simulation_button_text_var.set("Run Simulation")
            self.duration_var.set("")

    def reset_current_month(self):
        self.current_month = 0

    def create_window(self):
        # TODO: think there should be a better way than using the method place(),
        #  maybe pack() or grid()? \
        #  Because right now it is using relative position rather than absolute

        # create an instance of the Tk class
        self.root = Tk()

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
        self.sim_next_month_checkbox.grid(row=2, column=1, sticky=NW)

        # input_label - for running whole sim
        self.duration_input_label = Label(self.root, text="Enter Month Here:")
        self.duration_input_label.grid(row=0, column=0, sticky=NW, columnspan=2)

        # input_box - if monthly-checkbox is checked, the entry does nothing (preferred)
        self.duration_input_entry = Entry(self.root, textvariable=self.duration_var, width=30)
        self.duration_input_entry.grid(row=1, column=0, sticky=NW, columnspan=2)

        self.forward_button = Button(text="Redirect to next month result",
                                     command=self.display_forward_a_month)
        self.forward_button.grid(row=3, column=1, sticky=NW)
        self.backward_button = Button(text="Redirect to last month result",
                                      command=self.display_backward_a_month)
        self.backward_button.grid(row=3, column=0, sticky=NW)

        # button for when user is ready to run the sim
        self.run_simulation_button = Button(self.root,
                                            textvariable=self.run_simulation_button_text_var,
                                            command=self.run_sim)
        self.run_simulation_button.grid(row=2, column=0, sticky=NW)

        self.root.grid_columnconfigure(4, minsize=100)

        self.root.mainloop()


def main():
    SimulationInterface()


if __name__ == "__main__":
    main()
