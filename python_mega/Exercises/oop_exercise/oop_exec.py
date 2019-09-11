import tkinter as tk
import contextlib

from oop_backend import Database

"""
APP 5 CONVERTED TO OOP.
DB App with graphical interface, that manages book entries.
"""

database = Database("book.db")


class Window(object):

    def __init__(self, window):
        self.window = window
        l1 = tk.Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = tk.Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = tk.Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = tk.Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = tk.StringVar()
        self.e1 = tk.Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = tk.StringVar()
        self.e2 = tk.Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = tk.StringVar()
        self.e3 = tk.Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = tk.StringVar()
        self.e4 = tk.Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.list1 = tk.Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1 = tk.Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        b1 = tk.Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = tk.Button(window, text="Search entry",
                    width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = tk.Button(window, text="Add Entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = tk.Button(window, text="Update", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = tk.Button(window, text="Delete", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = tk.Button(window, text="Close", width=12, command=self.close_command)
        b6.grid(row=7, column=3)


    def get_selected_row(self, event):
        with contextlib.suppress(IndexError):
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0, tk.END)
            self.e1.insert(tk.END, self.selected_tuple[1])
            self.e2.delete(0, tk.END)
            self.e2.insert(tk.END, self.selected_tuple[2])
            self.e3.delete(0, tk.END)
            self.e3.insert(tk.END, self.selected_tuple[3])
            self.e4.delete(0, tk.END)
            self.e4.insert(tk.END, self.selected_tuple[4])

    def view_command(self):
        self.list1.delete(0, tk.END)
        for row in database.view_all():
            self.list1.insert(tk.END, row)

    def search_command(self):
        self.list1.delete(0, tk.END)
        for row in database.search_entry(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(tk.END, row)

    def add_command(self):
        database.add_entry(self.title_text.get(), self.author_text.get(),
                        self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, tk.END)
        self.list1.insert(tk.END, (self.title_text.get(), self.author_text.get(),
                            self.year_text.get(), self.isbn_text.get()))

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(),
                        self.author_text.get(), self.year_text.get(), self.isbn_text.get())

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def close_command(self):
        self.window.destroy()


window = tk.Tk()
Window(window)
window.mainloop()
