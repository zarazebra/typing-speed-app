from tkinter import *
from tkinter import ttk


def restart():
    pass


root = Tk()
root.title("Average Typing Speed")
root.geometry("800x600-550+250")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="N, W, E, S")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

example_txt_label = ttk.Label(root, text="Example text")
example_txt_label.grid(column=0, row=0)

typing_txt_entry = ttk.Entry(root)
typing_txt_entry.focus()
typing_txt_entry.grid(column=0, row=1)

restart_button = ttk.Button(root, text="Restart", command=restart)
restart_button.grid(column=0, row=3)


root.mainloop()
