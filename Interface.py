from tkinter import *
from tkinter import messagebox
from Simulation import Simulator

# simple and sweet, as long as it is easily readable


def run_sim():
    # get user input
    duration = duration_var.get()      # .get() returns str, https://www.tutorialspoint.com/python/tk_entry.htm

    # changing user input to int
    # TODO: assert duration_var isdigit
    duration = int(duration)

    # pass onto the class
    sim = Simulator(duration)

    # get and set our result_var
    result_var.set(sim.result)

    # reset duration_var
    duration_var.set("")


if __name__ == "__main__":
    # creating an instance of the Tk class
    root = Tk()

    # formatting
    root.geometry("600x400")

    # specifying variables
    duration_var = StringVar()
    result_var = StringVar()

    # label on the left
    duration_label = Label(root, text='Simulation duration')

    # input box next to the label
    duration_entry = Entry(root, textvariable=duration_var)

    # button for when user is ready to run the sim
    submit_button = Button(root, text='Run simulation', command=run_sim)

    # TODO: some output box for result_var

    # format
    duration_label.grid(row=0, column=0)
    duration_entry.grid(row=0, column=1)
    submit_button.grid(row=2, column=1)

    root.mainloop()
