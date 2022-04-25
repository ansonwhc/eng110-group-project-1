import tkinter as tk

window = tk.Tk()
window.title("Sparta Global Trainee Simulator")
window.geometry("500x200")
window.resizable(width=0, height=0)


def return_entry(arg=None):
    """Gets the result from Entry and return it to the Label"""
    result = my_entry.get()
    if result.isdigit():
        res = int(result) * 2
        result_label.config(text=res)
        my_entry.delete(0, tk.END)
    else:
        result_label.config(text="Incorrect input")


my_entry = tk.Entry(window, width=20)
my_entry.focus()
my_entry.bind("<Return>", return_entry)
my_entry.pack()

enter_entry = tk.Button(window, text="Simulate", width=10, command=return_entry)
enter_entry.pack()

result_label = tk.Label(window, text="")
result_label.pack(fill=tk.X)

window.mainloop()

#
# frame_test = tk.Frame(master=window)
# test_ent = tk.Entry(master=frame_test,
#                     bg="white",
#                     width=25,
#                     )
# test_ent.get()
# test_btn = tk.Button(master=window,
#                      text="Simulate",
#                      command=a_fn()
#                      )
# test_lbl = tk.Label(master=window,
#                     text="Test")
#
# test_lbl.grid(row=2, column=0, pady=0)
# test_ent.grid(row=0, column=0)
# frame_test.grid(row=0, column=0, padx=130, pady=50)
# test_btn.grid(row=1, column=0, pady=0)
