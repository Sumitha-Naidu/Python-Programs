from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

def only_numbers(char):
    return char.isdigit()

def only_alpha(char):
    if char.isdigit():
        return False
    else:
        return True
    
def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
    name = e1.get()
    branch = e2.get()
    acc=e3.get()
    mob=e4.get()
    if len(acc) != 12:
        messagebox.showerror("Length Error","Account Number should be 12 digits only.")
        e3.focus()
    if len(mob) != 10:
        messagebox.showerror("Length Error","Mobile Number should be 10 digits only.")
        e4.focus()
    if len(acc)==12 and len(mob)==10:
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='mysql password')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
        
            mycursor = connection.cursor()
            sql = "INSERT INTO bank (name, branch, accno, phone) VALUES (%s, %s, %s, %s)"
            val = (name,branch,acc,mob)
            mycursor.execute(sql, val)
            connection.commit()
            print(mycursor.rowcount, "record inserted.")
        except Error as error:
            print("Error while connecting to MySQL", error)

window=Tk()
window.geometry("500x500")
window.title("bank account")

l1=Label(window,text="name",font=("arial",20))
l2=Label(window,text="branch",font=("arial",20))
l3=Label(window,text="Acc no",font=("arial",20))
l4=Label(window,text="mobile no",font=("arial",20))

reg = window.register(only_alpha) 
e1=Entry(window, validate ="key", validatecommand =(reg,'%S'), width=10, font=("arial",15))

reg1 = window.register(only_alpha) 
e2 =Entry(window,width=10, validate ="key", validatecommand =(reg1,'%S'), font=("arial", 15))

reg2 = window.register(only_numbers) 
e3 =Entry(window,width=10, validate ="key", validatecommand =(reg2,'%S'), font=("arial", 15))

reg3 = window.register(only_numbers) 
e4 =Entry(window,width=10, validate ="key", validatecommand =(reg3,'%S'), font=("arial", 15))

b1 = Button(window, text="Insert into Database", command=returnEntry)

l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)
b1.grid(row=5, column=1)

window.mainloop()