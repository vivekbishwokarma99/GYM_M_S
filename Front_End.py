import tkinter
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
                        Client_Info_Back_End.insert(self.name.get(),
                                                    self.address.get(),
                                                    self.mobile_number.get(),
                                                    self.email_address.get(),
                                                    self.date_of_birth.get(),
                                                    self.gender.get())
                        self.listbox.delete(0, END)
                        self.listbox.insert(END, (self.name.get(),
                                                    self.address.get(),
                                                    self.mobile_number.get(),
                                                    self.email_address.get(),
                                                    self.date_of_birth.get(),
                                                    self.gender.get()))


                def Display():
                        self.listbox.delete(0, END)
                        for row in Client_Info_Back_End.view():
                            self.listbox.insert(END, row, str(' '))


                def Exit():
                        Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                        if Exit <=0:
                            self.master.destroy()
                            return


                def Delete():
                    if(len(self.name.get()) !=0):
                        Client_Info_Back_End.delete(selected_tuple[0])
                        Display()


                def Update():
                    if(len(self.name.get()) !=0):
                        Client_Info_Back_End.delete(selected_tuple[0])
                    if (len(self.name.get()) != 0):
                        Client_Info_Back_End.insert(self.name.get(),
                                                    self.address.get(),
                                                    self.mobile_number.get(),
                                                    self.email_address.get(),
                                                    self.date_of_birth.get(),
                                                    self.gender.get())

                        self.listbox.delete(0, END)
                        self.listbox.insert(END,   (self.name.get(),
                                                    self.address.get(),
                                                    self.mobile_number.get(),
                                                    self.email_address.get(),
                                                    self.date_of_birth.get(),
                                                    self.gender.get()))

# Adding Frames
                        self.Client_Main_Frame = LabelFrame(self.master, width=1300, height=500, font=('arial', 20, 'bold'), \
                                                            bg='#99c2ff', bd=15, relief='ridge')
                        self.Client_Main_Frame.grid(row=0, column=0, padx=10, pady=20)

                        self.Client_Main_Frame1 = LabelFrame(self.Client_Main_Frame, width=600, height=400, font=('arial', 15, 'bold'), \
                                                            bg='#99c2ff', bd=10, relief='ridge', text='CLIENT DETAILS')
                        self.Client_Main_Frame1.grid(row=1, column=0, padx=10)

                        self.Client_Main_Frame2 = LabelFrame(self.Client_Main_Frame, width=750, height=400, font=('arial', 15, 'bold'), \
                                                             bg='#99c2ff', bd=10, relief='ridge', text='CLIENT RECORDS')
                        self.Client_Main_Frame2.grid(row=2, column=0, padx=5)

                        self.Client_Main_Frame3 = LabelFrame(self.Client_Main_Frame, width=1200, height=100, font=('arial', 15, 'bold'), \
                                                             bg='#99c2ff', bd=13, relief='ridge')
                        self.Client_Main_Frame3.grid(row=2, column=0, padx=10)





                        self.lbl_Name = Label(self.Student_Frame_1, text='Name', font=('arial', 20,'bold'), bg='#99c2ff')
                        self.lbl_Name.grid(row=0, column=0, sticky=W, padx=20, pady=10)
                        self.lbl_Address = Label(self.Student_Frame_1, text='Address', font=('arial', 20, 'bold'), bg='#99c2ff')
                        self.lbl_Address.grid(row=0, column=0, sticky=W, padx=20, pady=10)
                        self.lbl_Mobile_Number = Label(self.Student_Frame_1, text='Mobile No.', font=('arial', 20, 'bold'), bg='#99c2ff')
                        self.lbl_Mobile_Number.grid(row=0, column=0, sticky=W, padx=20, pady=10)
                        self.lbl_Email_Address = Label(self.Student_Frame_1, text='Email Address', font=('arial', 20, 'bold'), bg='#99c2ff')
                        self.lbl_Email_Address.grid(row=0, column=0, sticky=W, padx=20, pady=10)
                        self.lbl_Date_Of_Birth = Label(self.Student_Frame_1, text='Date of Birth', font=('arial', 20, 'bold'), bg='#99c2ff')
                        self.lbl_Date_Of_Birth.grid(row=0, column=0, sticky=W, padx=20, pady=10)
                        self.lbl_Gender= Label(self.Student_Frame_1, text='Gender', font=('arial', 20, 'bold'), bg='#99c2ff')
                        self.lbl_Gender.grid(row=0, column=0, sticky=W, padx=20, pady=10)


                        self.Button_ADD = Button(self.Client_Main_Frame3, text = 'ADD', font=(arial, 17,'bold'), width=8, command= Add(), relief=GROOVE)
                        self.Button_ADD.grid(row=0, column=0, padx=10, pady=10)

                        self.Button_UPDATE = Button(self.Client_Main_Frame3, text='UPDATE', font=(arial, 17, 'bold'), width=8,
                                                 command=Update(), relief=GROOVE)
                        self.Button_UPDATE.grid(row=0, column=4, padx=10, pady=10)

                        self.Button_DELETE = Button(self.Client_Main_Frame3, text='DELETE', font=(arial, 17, 'bold'),
                                                    width=8, command=Delete(), relief=GROOVE)
                        self.Button_DELETE.grid(row=0, column=6, padx=10, pady=10)

                        self.Button_EXIT = Button(self.Client_Main_Frame3, text='EXIT', font=(arial, 17, 'bold'),
                                                    width=8, command=Exit(), relief=GROOVE)
                        self.Button_EXIT.grid(row=0, column=8, padx=10, pady=10)



                        self.scrollbar = Scrollbar(self.Client_Main_Frame2)
                        self.scrollbar.grid(row=0, column=1, sticky='ns')

                        self.listbox = Listbox(self.Client_Main_Frame2, width=75, height=20, font=('arial',12, 'bold'))
                        self.listbox.bind('<<ListboxSelect', Client_Record())
                        self.listbox.grid(row=0, column=0)
                        self.scrollbar.config(command=self.listbox.yview)

                    info()

















