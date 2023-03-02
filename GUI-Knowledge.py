from tkinter import * 
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')


B1 = ttk.Button(GUI,text='peet')
B1.pack(ipadx=20,ipady=20)


#B2 = Button(GUI,text='Tong')
#B2.pack()

B2 = ttk.Button(GUI,text='peth')
#B2.pack(ipadx=20,ipady=20)
B2.place(x=50,y=200)

L1 = Label(GUI,text='Program',font=('Angsana New',30),fg = 'green')
L1.place(x=30,y=20)


def Button2():
    text = 'OK'
    messagebox.showinfo('Name',text)
    #messagebox.showwarning('Name',text)
    #messagebox.showerror('Name',text)

#FB1 = LabelFrame(GUI,text='Fullname')
FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='Tong',command = Button2)
B2.pack(ipadx=20,ipady=20)



def Button3():
    text = 'No'
    messagebox.showinfo('Last',text)
    #messagebox.showwarning('Name',text)
    #messagebox.showerror('Name',text)

#FB2 = LabelFrame(GUI,text='Fullname')
FB2 = Frame(GUI)
FB2.place(x=100,y=100)
B3 = ttk.Button(FB2,text='Peth',command = Button3)
B3.pack(ipadx=20,ipady=20)





GUI.mainloop()
