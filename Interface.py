from tkinter import *
from tkinter import messagebox
from Simulation import SGCentresSimulation




def run_sim():
    # TODO: assert duration_var isdigit
    duration = int(duration_var.get())
    # pass onto the class
    Sim = SGCentresSimulation(duration)

    duration_var.set(0)


if __name__ == "__main__":
    root = Tk()
    # formatting
    root.geometry("600x400")

    duration_var = StringVar()

    # label on the left
    duration_label = Label(root, text='Simulation Duration')
    # input box next to the label
    duration_entry = Entry(root, textvariable=duration_var)
    # button for when user is ready to run the sim
    sub_btn = Button(root, text='Run Simulation', command=run_sim)

    # format
    duration_label.grid(row=0, column=0)
    duration_entry.grid(row=0, column=1)
    sub_btn.grid(row=2, column=1)

    root.mainloop()
