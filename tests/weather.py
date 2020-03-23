import tkinter as tk
import requests

HEIGHT = 800
WIDTH = 600

def test_function(entry):
	print("This is the entry:", entry)




root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()



frame = tk.Frame(root, bg='gray', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Label(frame, font=40, text='Megacorp Springfield MAS', bg='gray')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="System Config", font=40)
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()