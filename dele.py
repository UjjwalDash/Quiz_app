from tkinter import *
import sqlite3
import tkinter.messagebox
mem1=Tk()
mem1.title('Quiz')
mem1.maxsize(1000,300)
mem1.configure(bg='Powder Blue')
member=Frame(mem1,bg='Powder Blue',bd=5)
member.pack(side=TOP)
btnfra=Frame(mem1,bg='Powder Blue',bd=5)
btnfra.pack(side=BOTTOM)
mno=StringVar()
def reset():
    mno.set('')
def exi():
    mem1.destroy()
def delete():
    a=mno.get()
    crr=sqlite3.connect('QUIZ.db')
    c=crr.cursor()
    c.execute('select* from quize')
    l=c.fetchall()
    d={}
    for row in l:
        d[row[0]]=row[1],row[2],row[3],row[4],row[5]
    try:
        b=d[a]
        A=b[0]
        B=b[1]
        C=b[2]
        D=b[3]
        Ans=b[4]
        try:
            
            cnx=sqlite3.connect('QUIZ.db')
            Cursor=cnx.cursor()
            Qry=("DELETE FROM quize WHERE question='%s'"%(a))
            Cursor.execute(Qry)
            cnx.commit()
            Cursor.close()
            tkinter.messagebox.showinfo('program',"Question Deleted Successfully........")
            reset()
        except:
            tkinter.messagebox.showinfo('program',"Question does not exist........")
    except:
        tkinter.messagebox.showinfo("program",'No such No such Question  found')
question=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Question:')
question.grid(row=0,column=0)
questiontxt=Entry(member,font=('arial 16 bold'),textvar=mno,width=50,justify=LEFT,bd=8)
questiontxt.grid(row=0,column=1)
btn=Button(btnfra,text='Delete',font=('arial 16 bold'),command=delete,bd=8,pady=5,
           bg='Orange',width=10)
btn.grid(row=4,column=0,sticky='w')
btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
            pady=5,bg='Yellow',width=10)
btn1.grid(row=4,column=1,sticky='w')
btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exi,bd=8,
            pady=5,bg='Red',width=10)
btn2.grid(row=4,column=2,sticky='w')
mem1.mainloop() 
