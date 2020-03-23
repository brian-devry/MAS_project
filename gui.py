#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Mar 22, 2020 11:08:08 PM CDT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
    Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 12"
        font11 = "-family {Segoe UI} -size 9 -weight bold -underline 1"  \
            ""
        font12 = "-family {Segoe UI} -size 16 -weight bold"
        font9 = "-family {Segoe UI} -size 18"

        top.geometry("1059x807+457+130")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.112, relheight=0.743
                , relwidth=0.85)
        self.Canvas1.configure(background="#c0c0c0")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.267, rely=0.1, height=71, width=451)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Megacorp Springfield MAS System''')

        self.Frame1 = tk.Frame(self.Canvas1)
        self.Frame1.place(relx=0.089, rely=0.317, relheight=0.558, relwidth=0.33)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.202, rely=0.03, height=31, width=174)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Sensor Overview''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.034, rely=0.209, height=21, width=84)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Smoke 1:''')

        self.Label3_1 = tk.Label(self.Frame1)
        self.Label3_1.place(relx=0.034, rely=0.269, height=21, width=84)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#d9d9d9")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Smoke 2:''')

        self.Label3_2 = tk.Label(self.Frame1)
        self.Label3_2.place(relx=0.034, rely=0.328, height=21, width=84)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#d9d9d9")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Smoke 3:''')

        self.Label3_3 = tk.Label(self.Frame1)
        self.Label3_3.place(relx=0.034, rely=0.448, height=21, width=84)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Monoxide 1:''')

        self.Label3_3 = tk.Label(self.Frame1)
        self.Label3_3.place(relx=0.034, rely=0.507, height=21, width=84)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Monoxide 2:''')

        self.Label3_3 = tk.Label(self.Frame1)
        self.Label3_3.place(relx=0.034, rely=0.627, height=21, width=84)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Static 1:''')

        self.Label3_3 = tk.Label(self.Frame1)
        self.Label3_3.place(relx=0.034, rely=0.687, height=21, width=84)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Static 2:''')

        self.Label3_3 = tk.Label(self.Frame1)
        self.Label3_3.place(relx=0.034, rely=0.806, height=21, width=84)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Heat 1:''')

        self.Label3_3 = tk.Label(self.Frame1)
        self.Label3_3.place(relx=0.303, rely=0.209, height=21, width=84)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(font=font11)
        self.Label3_3.configure(foreground="#008000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Good''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.303, rely=0.269, height=21, width=84)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 9 -weight bold -underline 1")
        self.Label3_4.configure(foreground="#008000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Good''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.303, rely=0.328, height=21, width=84)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 9 -weight bold -underline 1")
        self.Label3_4.configure(foreground="#008000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Good''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.303, rely=0.448, height=21, width=84)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 9 -weight bold -underline 1")
        self.Label3_4.configure(foreground="#008000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Good''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.303, rely=0.507, height=21, width=84)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 9 -weight bold -underline 1")
        self.Label3_4.configure(foreground="#008000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Good''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.303, rely=0.627, height=21, width=84)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 9 -weight bold -underline 1")
        self.Label3_4.configure(foreground="#008000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Good''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.303, rely=0.687, height=21, width=84)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 9 -weight bold -underline 1")
        self.Label3_4.configure(foreground="#008000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Good''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.303, rely=0.806, height=21, width=84)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 9 -weight bold -underline 1")
        self.Label3_4.configure(foreground="#008000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Good''')

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(relx=0.622, rely=0.417, height=184, width=207)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''System Configuration''')
        self.Button1.configure(wraplength="150")

if __name__ == '__main__':
    vp_start_gui()



