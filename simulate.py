import random
import time
from tkinter import *
from trainee import Trainee
from center import Center

class Simulate():

    def __init__(self, input):
        self.obj_trainee = Trainee()
        self.obj_center = Center()
        self.input = input
        self.root = Tk()
        self.root.geometry("300x600")
        self.root.configure(background='black')
        self.e = None
        self.strings = []
        self.label = None
        self.top_frame = None
        self.bottom_frame = None

    def run_simulation(self):
        self.check_output_file_exists()
        self.start_line_output_file()
        self.strings = []
        for i in range(1, self.input + 1, 1):
            if i % 2 == 0 or i == 1:
                self.obj_center.generate_center()
            trainee_generated = self.obj_trainee.generate_new_trainees()
            self.obj_center.create_distribution_list()
            self.obj_center.distribute_trainees(self.obj_center.waiting_list_dictionary)
            self.obj_center.distribute_trainees(trainee_generated, distributed_waiting_list=True)
        self.strings.append("==MONTH {month}==".format(month=i))
        self.strings.append("=Open Centers==")
        for key, value in self.output_centers("open", "yes").items():
            self.strings.append(str(key) + ": " + str(value))
        self.strings.append("=Closed Centers=")
        for key, value in self.output_centers("open", "no").items():
            self.strings.append(str(key) + ": " + str(value))
        self.strings.append("=Full Centers=")
        for key, value in self.output_centers("full", "yes").items():
            self.strings.append(str(key) + ": " + str(value))
        self.strings.append("=Working Trainees=")
        for key, value in self.output_working_trainees(self.obj_center.all_centers).items():
            self.strings.append(str(key) + ": " + str(value))
        self.strings.append("=Waiting List=")
        for key, value in self.obj_center.waiting_list_dictionary.items():
            self.strings.append(str(key) + ": " + str(value))

        self.write_to_output_file(self.strings)
        self.end_line_output_file()

    def gui_interface(self):
        
        self.top_frame = Frame(self.root, bg='black', width=10, height=5, pady=3)
        self.btm_frame = Frame(self.root, width=200, height=200, pady=3)
        self.top_frame.grid(row=0, sticky="ew")
        

        label = Label(self.top_frame, text="Enter a number of months: ")
        label.grid(row=0, column=0,padx=2)
        self.e = Entry(self.top_frame, width=5)
        self.e.grid(row=1, column=0, padx=2, sticky="ew")
        btn = Button(self.top_frame, text="Final output", command=self.click)
        btn.grid(row=1,column=1,padx=0,pady=2)

        btn1 = Button(self.top_frame, text="Output per month", command=self.slow_click)
        btn1.grid(row=0,column=1,padx=0,pady=0)

        self.root.mainloop()

    def click(self):
        if self.e.get().isdigit():
            if int(self.e.get()) >= 0:
                if self.label != None:
                    self.label.destroy()
                self.obj_center = Center()
                self.input = int(self.e.get())
                self.run_simulation()
                self.label = Label(self.bottom_frame, text="\n".join(map(str, self.strings)), fg='white')
                self.label.configure(background='black')
                self.label.grid(row=2,column=0)

    def slow_click(self):
        if self.e.get().isdigit():
            if int(self.e.get()) >= 0:
                self.obj_center = Center()
                self.input = int(self.e.get())
                self.check_output_file_exists()
                self.start_line_output_file()
                for i in range(1, self.input + 1, 1):
                    self.strings = []
                    if i % 2 == 0 or i == 1:
                        self.obj_center.generate_center()
                    trainee_generated = self.obj_trainee.generate_new_trainees()
                    self.obj_center.create_distribution_list()
                    self.obj_center.distribute_trainees(self.obj_center.waiting_list_dictionary)
                    self.obj_center.distribute_trainees(trainee_generated, distributed_waiting_list=True)
                    self.strings.append("==MONTH {month}==".format(month=i))
                    self.strings.append("=Open Centers==")
                    for key, value in self.output_centers("open", "yes").items():
                        self.strings.append(str(key) + ": " + str(value))
                    self.strings.append("=Closed Centers=")
                    for key, value in self.output_centers("open", "no").items():
                        self.strings.append(str(key) + ": " + str(value))
                    self.strings.append("=Full Centers=")
                    for key, value in self.output_centers("full", "yes").items():
                        self.strings.append(str(key) + ": " + str(value))
                    self.strings.append("=Working Trainees=")
                    for key, value in self.output_working_trainees(self.obj_center.all_centers).items():
                        self.strings.append(str(key) + ": " + str(value))
                    self.strings.append("=Waiting List=")
                    for key, value in self.obj_center.waiting_list_dictionary.items():
                        self.strings.append(str(key) + ": " + str(value))
                    if self.label != None:
                        self.label.destroy()
                    self.label = Label(self.bottom_frame, text="\n".join(map(str, self.strings)), fg='white')
                    self.label.configure(background='black')
                    self.label.grid(row=2,column=0)
                    self.root.update()
                    time.sleep(1.3)
                    self.write_to_output_file(self.strings)
                self.end_line_output_file()

    def output_centers(self, key, value):
        breakdown = {}
        for center in self.obj_center.all_centers:
            if center[key] == value:
                if center["type"] == "tech_center":
                    string = "Tech Centre teaching " + str(center["course"])
                elif center["type"] == "training_hub":
                    string = "Training Hub"
                else:
                    string = "Bootcamp"
                if string not in breakdown:
                    breakdown[string] = 1
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
        try:
            opened_file = open("log.txt", "r")
            opened_file.close()
        except FileNotFoundError:
            with open("log.txt", "w") as f:
                pass
    
    def write_to_output_file(self, string_lst):
        with open("log.txt", "a") as f:
            for string in string_lst:
                f.write("\n" + string + "\n")

    def start_line_output_file(self):
        with open("log.txt", "a") as f:
            f.write("\n---------------Start of simulation---------------\n")

    def end_line_output_file(self):
        with open("log.txt", "a") as f:
            f.write("\n---------------End of simulation---------------\n")

simulate_obj = Simulate(30)
simulate_obj.gui_interface()