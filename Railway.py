from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import stdDatabase

class Passenger :
    def __init__(self, root):

        self.root = root
        self.root.title("Railway Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        PsgID = StringVar()
        Name = StringVar()
        Gender = StringVar()
        DoB = StringVar()
        Age = StringVar()
        From = StringVar()
        To = StringVar()
        Mobile = StringVar()
#=============================================================Function==========================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Railways Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtPsgID.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtLna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtFrom.delete(0, END)
            self.txtTo.delete(0, END)
            self.txtMob.delete(0, END)

        def AddData():
            if(len(PsgID.get())!=0):
                    c1 = 3
                    if (From.get() == "Mumbai" and To.get() == "Chennai"):
                        messagebox.showinfo("Cost", "Yor cost is Rs. 2000")
                        messagebox.showinfo("Details","Travelling from Mumbai to Chennai\nDeparture time: 09:00hrs(01/04/2020)\nArrival time: 06:45am(02/04/2020)")
                    elif (From.get() == "Mumbai" and To.get() == "Hyderabad"):
                        messagebox.showinfo("Cost", "Yor cost is Rs. 1000")
                        messagebox.showinfo("Details","Travelling from Mumbai to Hyderabad\nDeparture time: 09:00hrs(01/04/2020)\nArrival time:11:05am(02/04/2020)")
                    elif (From.get() == "Mumbai" and To.get() == "Delhi"):
                        messagebox.showinfo("Cost", "Yor cost is Rs. 2500")
                        messagebox.showinfo("Details","Travelling from Mumbai to Delhi\nDeparture time: 09:00hrs(01/04/2020)\nArrival time:01:05am(02/04/2020)")
                    elif (From.get() == "Chennai" and To.get() == "Mumbai"):
                        messagebox.showinfo("Cost", "Yor cost is Rs. 2000")
                        messagebox.showinfo("Details","Travelling from Chennai to Mumbai\nDeparture time: 09:00hrs(01/04/2020)\nArrival time: 06:45am(02/04/2020)")
                    elif (From.get() == "Hyderabad" and To.get() == "Mumbai"):
                        messagebox.showinfo("Cost", "Yor cost is Rs. 1000")
                        messagebox.showinfo("Details","Travelling from Hyderabad to Mumbai\nDeparture time: 09:00hrs(01/04/2020)\nArrival time:11:05am(02/04/2020)")
                    elif (From.get() == "Delhi" and To.get() == "Mumbai"):
                        messagebox.showinfo("Cost", "Yor cost is Rs. 2500")
                        messagebox.showinfo("Details","Travelling from Delhi to Mumbai\nDeparture time: 09:00hrs(01/04/2020)\nArrival time:01:05am(02/04/2020)")


                    if(Gender.get() == "Female" or Gender.get() == "Male"):
                        stdDatabase.addStdRec(PsgID.get(), Name.get(), Gender.get(), DoB.get(), Age.get(), From.get(),To.get(), Mobile.get())
                        passengerlist.delete(0, END)
                        passengerlist.insert(END,(PsgID.get(), Name.get(), Gender.get(), DoB.get(), Age.get(), From.get(), To.get(), Mobile.get()))
                        messagebox.showinfo("Success", "Ticket Booked Successfully")

                    else:
                        messagebox.showinfo("Error", "Please enter Male or Female")
        def DisplayData():
            passengerlist.delete(0,END)
            for row in stdDatabase.viewData():
                passengerlist.insert(END,row,str(""))

        def passengerrec(event):
            global sd
            searchPsg = passengerlist.curselection()[0]
            sd = passengerlist.get(searchPsg)

            self.txtPsgID.delete(0, END)
            self.txtPsgID.insert(END,sd[1])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sd[2])
            self.txtLna.delete(0, END)
            self.txtLna.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtFrom.delete(0, END)
            self.txtFrom.insert(END, sd[6])
            self.txtTo.delete(0, END)
            self.txtTo.insert(END, sd[7])
            self.txtMob.delete(0, END)
            self.txtMob.insert(END, sd[8])

        def DeleteData():
            if (len(PsgID.get()) != 0):
                stdDatabase.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            passengerlist.delete(0, END)
            for row in stdDatabase.searchData(PsgID.get(), Name.get(), Gender.get(), DoB.get(), Age.get(), From.get(), To.get(), Mobile.get()):
                passengerlist.insert(END,row,str(""))
            messagebox.showinfo("Details Found")

        def update():
            if (len(PsgID.get()) != 0):
                stdDatabase.deleteRec(sd[0])
            if (len(PsgID.get()) != 0):
                stdDatabase.addStdRec(PsgID.get(), Name.get(), Gender.get(), DoB.get(), \
                                      Age.get(), From.get(), To.get(), Mobile.get())
                passengerlist.delete(0, END)
                passengerlist.insert(END, (PsgID.get(), Name.get(), Gender.get(), DoB.get(), \
                                       Age.get(), From.get(), To.get(), Mobile.get()))

#=============================================================FRAMES============================================================

        MainFrame = Frame(self.root, bg = "cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Railway Management System", bg = "Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=10, width = 1350, height = 70, padx=18, pady=10, bg="Ghost White", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1,width = 1300,height = 400, padx = 20, pady = 20, relief = RIDGE , bg = "cadet blue")
        DataFrame.pack(side = BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White",
                                   font=('arial', 20,'bold'), text="Passenger Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31,pady = 3, relief=RIDGE, bg="Ghost White",
                                    font=('arial', 20,'bold'), text="Passenger Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

#=================================================Labels and Entry Widget========================================================

        self.lblPsgID = Label(DataFrameLEFT, font = ('arial', 20, 'bold'), text="Passenger ID:", padx=2, pady=2, bg="Ghost White")
        self.lblPsgID.grid(row=0, column=0, sticky = W)
        self.txtPsgID = Entry(DataFrameLEFT, font = ('arial', 20, 'bold'), textvariable=PsgID, width=39)
        self.txtPsgID.grid(row=0, column=1)

        self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Name:", padx=2, pady=2, bg="Ghost White")
        self.lblFna.grid(row=1, column=0, sticky=W)
        self.txtFna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Name, width=39)
        self.txtFna.grid(row=1, column=1)

        self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=2, bg="Ghost White")
        self.lblLna.grid(row=2, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtLna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth:", padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblFrom = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="From:", padx=2, pady=2, bg = "Ghost White")
        self.lblFrom.grid(row=5, column=0, sticky=W)
        self.txtFrom = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=From, width=39)
        self.txtFrom.grid(row=5, column=1)

        self.lblTo = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="To:", padx=2, pady=2, bg = "Ghost White")
        self.lblTo.grid(row=6, column=0, sticky=W)
        self.txtTo = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=To, width=39)
        self.txtTo.grid(row=6, column=1)

        self.lblMob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile No.:", padx=2, pady=2, bg = "Ghost White")
        self.lblMob.grid(row=7, column=0, sticky=W)
        self.txtMob = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMob.grid(row=7, column=1)

#=================================================Listbox & ScrollBar Widget========================================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        passengerlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        passengerlist.bind('<<ListboxSelect>>', passengerrec)
        passengerlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command =  passengerlist.yview)

#=================================================Button Widget=====================================================================

        self.btnToDate = Button(ButtonFrame, text="Book Ticket", font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=AddData)
        self.btnToDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 12, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 12, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 12, 'bold'), height=1, width=10, bd=4, command = iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':

    username = input("Enter your username:\n")
    password = input("Enter your password:\n")

    u1 = "poojamangal"
    p1 = "pmangal"

    u2 = "devanshimehta"
    p2 = "dmehta"

    u3 = "kshitijk"
    p3 = "kkavimandan"

    if((username == u1 and password == p1) or (username == u2 and password == p2) or (username == u3 and password == p3)):
        print("Login successfull")
        root = Tk()
        application = Passenger(root)
        root.mainloop()
    else:
        print("Incorrect username or password")
