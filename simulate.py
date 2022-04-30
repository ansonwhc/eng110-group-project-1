import random
import time
from tkinter import *
from trainee import Trainee
from center import Center

class Simulate():

    def __init__(self):
        # Creates objects of the trainee and center classes which will be used
        # in order to get the customer's requested output.
        self.obj_trainee = Trainee()
        self.obj_center = Center()
        # The input is how many months the simulation will run for.
        self.input = 0
        # Instantiates an object of the Tkinter class. We will use this object
        # to customise our GUI.
        self.root = Tk()
        # Sets the window's height and width
        self.root.geometry("265x600")
        # Sets the background to black
        self.root.configure(background='black')
        # This will be the area the user can type how many months
        # they want simulated into.
        self.input_box = None
        # This list will store all the output the customer wants
        self.output_strings = []
        # Displays the text found in the above list onto the GUI.
        self.output_text_gui = None
        '''
        Creates all of the main containers used for tkinter.
        Placing buttons into these containers ensures they stay
        stationary rather than moving around if the output text
        takes up a lot of space.
        '''
        self.top_frame = None
        self.bottom_frame = None

    def run_simulation(self, record_every_month=False):
        for i in range(1, self.input + 1, 1):
            if i == 1 and record_every_month == True:
                self.check_output_file_exists()
                self.start_line_output_file()
            # Because i starts at 1, every time i is odd, we want
            # to open a new training centre (one gets opened every
            # two months).
            if i % 2 != 0:
                self.obj_center.generate_center()
            # Generates a new random set of trainees for the month.
            trainee_generated = self.obj_trainee.generate_new_trainees()
            # Generates a list which tracks how many trainees each
            # centre will accept for the month.
            self.obj_center.create_distribution_list()
            # First distributes trainees from the waiting list beacause this has priority.
            self.obj_center.distribute_trainees(self.obj_center.waiting_list_dictionary)
            # After distributing from the waiting list, we then distribute from the trainees
            # generated this month.
            self.obj_center.distribute_trainees(trainee_generated, distributed_waiting_list=True)
            if record_every_month == True:
                # If we are recording every month, we will update the GUI interface during
                # this current iteration.
                self.output_to_gui_and_logs(i, True)
                if self.output_text_gui != None:
                    # We completely destroy the previous output text (if it exists) because
                    # tkinter sometimes has trouble replacing the text with the new
                    # output text we want displayed on the screen.
                    self.output_text_gui.destroy()
                self.output_text_gui = Label(self.bottom_frame, text="\n".join(map(str, self.output_strings)), fg='white')
                self.output_text_gui.configure(background='black')
                self.output_text_gui.grid(row=2,column=0)
                # Updates the GUI to show the new changes to the output text.
                self.root.update()
                # We do not want to go straight to the next iteration. We allow the script
                # to pause here for a bit so the user can see the information displayed
                # for the current month.
                time.sleep(1.3)
                self.write_to_output_file(self.output_strings)
                if i == self.input:
                    self.end_line_output_file()
                    
        # If we don't want to show output for every month, we just show the final output
        if record_every_month == False:
            self.output_to_gui_and_logs(i, False)
        
    def gui_interface(self):
        # Creates the main containers we will store our buttons and labels inside.
        self.top_frame = Frame(self.root, bg='black', width=10, height=5, pady=3)
        self.btm_frame = Frame(self.root, width=200, height=200, pady=3)
        self.top_frame.grid(row=0, sticky="ew")

        # Creates the widgets for the top frame (ones for the bottom frame are produced
        # in the functions self.straight_to_final_output() and self.month_by_month_breakdown())
        label = Label(self.top_frame, text="Enter a number of months: ")
        label.grid(row=0, column=0,padx=2)
        self.input_box = Entry(self.top_frame, width=5)
        self.input_box.grid(row=1, column=0, padx=2, sticky="ew")
        btn = Button(self.top_frame, text="Final output", command=self.straight_to_final_output)
        btn.grid(row=1,column=1,padx=0,pady=2)
        btn1 = Button(self.top_frame, text="Output per month", command=self.month_by_month_breakdown)
        btn1.grid(row=0,column=1,padx=0,pady=0)

        # Creates the window. This method will loop forever, waiting for events from the user, 
        # until the user exits the program – either by closing the window, or by terminating 
        # the program with a keyboard interrupt in the console (CTRL C).
        self.root.mainloop()

    def straight_to_final_output(self):
        # In the input box we have created, the user can actually type whatever they want.
        # If it is not a valid number, it will just be ignored.
        if self.input_box.get().isdigit():
            # If the month entered is 0, the input will also be ignored.
            if int(self.input_box.get()) > 0:
                if self.output_text_gui != None:
                    self.output_text_gui.destroy()
                self.obj_center = Center()
                self.input = int(self.input_box.get())
                self.run_simulation()
                self.output_text_gui = Label(self.bottom_frame, text="\n".join(map(str, self.output_strings)), fg='white')
                self.output_text_gui.configure(background='black')
                self.output_text_gui.grid(row=2,column=0)

    def month_by_month_breakdown(self):
        if self.input_box.get().isdigit():
            if int(self.input_box.get()) > 0:
                self.obj_center = Center()
                self.input = int(self.input_box.get())
                self.run_simulation(record_every_month=True)

    def output_to_gui_and_logs(self, month_num, every_month):
        if every_month == False:
            self.check_output_file_exists()
            self.start_line_output_file()

        # Ensures our output_strings list is empty before we fill it up.  
        self.output_strings = []
        # Fills up the list with all of the requested output.
        self.output_strings.append("\n===========MONTH {month}===========".format(month=month_num))
        self.output_strings.append("=====Open Centres=====")
        for key, value in self.output_centers("open", "yes").items():
            self.output_strings.append(str(key) + ": " + str(value))
        self.output_strings.append("")
        self.output_strings.append("=====Closed Centres=====")
        for key, value in self.output_centers("open", "no").items():
            self.output_strings.append(str(key) + ": " + str(value))
        self.output_strings.append("")
        self.output_strings.append("=====Full Centres=====")
        for key, value in self.output_centers("full", "yes").items():
            self.output_strings.append(str(key) + ": " + str(value))
        self.output_strings.append("")
        self.output_strings.append("=====Working Trainees=====")
        for key, value in self.output_working_trainees(self.obj_center.all_centers).items():
            self.output_strings.append(str(key) + ": " + str(value))
        self.output_strings.append("")
        self.output_strings.append("=====Waiting List=====")
        for key, value in self.obj_center.waiting_list_dictionary.items():
            self.output_strings.append(str(key) + ": " + str(value))

        if every_month == False:
            self.write_to_output_file(self.output_strings)
            self.end_line_output_file()

    def output_centers(self, key, value):
        '''
        The key parameter of this function should have the same name as
        one of the keys found in the dictionaries of the Center.all_centers 
        list. For example, if data for open centres gets requested, the 
        argument passed in for key would be "open" (and the value argument 
        would be "yes").
        '''
        breakdown = {}
        for center in self.obj_center.all_centers:
            if center[key] == value:
                if center["type"] == "tech_center":
                    string = "Tech Centre teaching " + str(center["course"])
                elif center["type"] == "training_hub":
                    string = "Training Hub"
                else:
                    string = "Bootcamp"
                # This bit helps us avoid key errors. If the string does not
                # exist in the dictionary, it gets created with a value of 1.
                if string not in breakdown:
                    breakdown[string] = 1
                # If it already exists, we instead increment the key's value by 1.
                else:
                    breakdown[string] += 1
        return breakdown

    def output_working_trainees(self, centre_list):
        dict = {"Java": 0, "C#": 0, "Data": 0, "DevOps": 0, "Business": 0}
        for centre in centre_list:
            for key in centre["trainee"].keys():
                dict[key] += centre["trainee"][key]
        return dict

    def check_output_file_exists(self):
        '''
        If the file does not exist in the present working directory,
        a "FileNotFoundError" exception will be thrown. In such a case, 
        the log.txt file will be created (though nothing will be written
        to this text file).
        '''
        try:
            opened_file = open("log.txt", "r")
            opened_file.close()
        except FileNotFoundError:
            with open("log.txt", "w") as f:
                pass
    
    def write_to_output_file(self, string_lst):
        # "a" here stands for append. This way when we write 
        # to the file, we will not delete anything
        # currently written inside it.
        with open("log.txt", "a") as f:
            for string in string_lst:
                f.write("\n" + string + "\n")

    def start_line_output_file(self):
        with open("log.txt", "a") as f:
            f.write("\n---------------Start of simulation---------------\n")

    def end_line_output_file(self):
        with open("log.txt", "a") as f:
            f.write("\n---------------End of simulation---------------\n")

simulate_obj = Simulate()
simulate_obj.gui_interface()