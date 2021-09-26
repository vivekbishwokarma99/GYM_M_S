from tkinter import *
from tkinter import messagebox
import random
from tkinter import colorchooser
from tkinter import ttk

class Client_Information():
        def __init__(self, master):
            self.master = master
            self.master.title('GYM Management System')
            self.master.geometry('1366x786+0+0')

            def info():

                self.name = StringVar()
                self.address = StringVar()
                self.mobile_number = StringVar()
                self.email_address = StringVar()
                self.date_of_birth = StringVar()
                self.gender = StringVar()



                def Client_Record(event):
                    try:
                            global selected_tuple

                            index = self.listbox.curselection()[0]
                            selected_tuple = self.listbox.get(index)

                            self.Text_Entry_name.delete(0,END)
                            self.Text_Entry_name.insert(END, selected_tuple[1])
                            self.Text_Entry_address.delete(0, END)
                            self.Text_Entry_address.insert(END, selected_tuple[2])
                            self.Text_Entry_mobile_number.delete(0, END)
                            self.Text_Entry_mobile_number.insert(END, selected_tuple[3])
                            self.Text_Entry_email_address.delete(0, END)
                            self.Text_Entry_email_address.insert(END, selected_tuple[4])
                            self.Text_Entry_date_of_birth.delete(0, END)
                            self.Text_Entry_date_of_birth.insert(END, selected_tuple[5])
                            self.Text_Entry_gender.delete(0, END)
                            self.Text_Entry_gender.insert(END, selected_tuple[6])
                    except IndexError:
                            pass

                def Add():
                    if(len(self.name.get()) !=0):
                        Client_info_Back_End.insert(self.name.get(),
                                                    self.address.get(),
                                                    self.mobile_number.get(),
                                                    self.email_address.get(),
                                                    self.date_of_birth.get(),
                                                    self.gender.get())
                        self.listbox.delete(0, END)
                        self.listbox.insert(END, self.name.get(),
                                                 self.address.get(),
                                                 self.mobile_number.get(),
                                                 self.email_address.get(),
                                                 self.date_of_birth.get(),
                                                 self.gender.get())






