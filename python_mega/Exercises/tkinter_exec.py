import tkinter as tk

window = tk.Tk()

def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.delete("1.0", tk.END)
    t1.insert(tk.END, miles)

def kg_to_ounce():
    res = float(e2_value.get()) * 35.274
    t2.delete("1.0", tk.END)
    t2.insert(tk.END, res)

def kg_to_pound():
    res = float(e3_value.get()) * 2.20462
    t3.delete("1.0", tk.END)
    t3.insert(tk.END, res)

b1 = tk.Button(window, text="Convert KM - ML", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = tk.Text(window, height=1, width=20)
t1.grid(row=0, column=2)

b2 = tk.Button(window, text="Convert KG - ONC", command=kg_to_ounce)
b2.grid(row=1, column=0)

e2_value = tk.StringVar()
e2 = tk.Entry(window, textvariable=e2_value)
e2.grid(row=1, column=1)

t2 = tk.Text(window, height=1, width=20)
t2.grid(row=1, column=2)

b3 = tk.Button(window, text="Convert KG - PND", command=kg_to_pound)
b3.grid(row=2, column=0)

e3_value = tk.StringVar()
e3 = tk.Entry(window, textvariable=e3_value)
e3.grid(row=2, column=1)

t3 = tk.Text(window, height=1, width=20)
t3.grid(row=2, column=2)

window.mainloop()
