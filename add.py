from tkinter import*
import tkinter.messagebox
import sqlite3
from tkinter import ttk
root=Tk()
#variable
ques=StringVar()
op1=StringVar()
op2=StringVar()
op3=StringVar()
op4=StringVar()
ans=StringVar()
#
ques.set('')
op1.set('')
op2.set('')
op3.set('')
op4.set('')
ans.set('')
#
root.configure(bg='yellow')
top=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
top.pack(side=TOP)
frame=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame.pack(side=TOP,anchor='nw')
frame1=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame1.pack(side=TOP,anchor='nw')
frame2=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame2.pack(side=TOP,anchor='nw')
frame3=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame3.pack(side=TOP,anchor='nw')
frame4=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame4.pack(side=TOP,anchor='nw')
frame5=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame5.pack(side=TOP,anchor='nw')
frame6=Frame(root,bg='Blue',bd=10,relief=RIDGE)
frame6.pack(side=TOP)

#Heading
head=Label(top,bg='Yellow',padx=5,pady=5,text='Add Questions',font=('arial 30 bold'))
head.grid(row=0,column=0)
#Question
question=Label(frame,bg='Yellow',padx=5,pady=5,text='Questions',font=('arial 16 bold'))
question.grid(row=0,column=0)
questiontxt=Entry(frame,textvar=ques,font=('arial 16 bold'),bd=5,width=70)
questiontxt.grid(row=0,column=1)
#Options
#Option_1
option1=Label(frame1,bg='Yellow',padx=5,pady=5,text='(A)',font=('arial 16 bold'))
option1.grid(row=0,column=0)
option1txt=Entry(frame1,textvar=op1,font=('arial 16 bold'),bd=5,width=30)
option1txt.grid(row=0,column=1)
#Option_2
option2=Label(frame2,bg='Yellow',padx=5,pady=5,text='(B)',font=('arial 16 bold'))
option2.grid(row=0,column=0)
option2txt=Entry(frame2,textvar=op2,font=('arial 16 bold'),bd=5,width=30)
option2txt.grid(row=0,column=1)
#Option_3
option3=Label(frame3,bg='Yellow',padx=5,pady=5,text='(C)',font=('arial 16 bold'))
option3.grid(row=0,column=0)
option3txt=Entry(frame3,textvar=op3,font=('arial 16 bold'),bd=5,width=30)
option3txt.grid(row=0,column=1)
#Option_4
option4=Label(frame4,bg='Yellow',padx=5,pady=5,text='(D)',font=('arial 16 bold'))
option4.grid(row=0,column=0)
option4txt=Entry(frame4,textvar=op4,font=('arial 16 bold'),bd=5,width=30)
option4txt.grid(row=0,column=1)

#Answer
option5=Label(frame5,bg='Yellow',padx=5,pady=5,text='Answer',font=('arial 16 bold'))
option5.grid(row=0,column=0)
option5txt= tkinter.ttk.Combobox(frame5,textvariable = ans,state='randomly',font=('arial 16 bold'))
option5txt.config(width=15)
option5txt.grid(row=0,column=1)
option5txt['value']=("-select-",'A','B','C','D')
option5txt.current(0)
def save():
    if ques.get!='' and op1.get!='' and op2.get()!='' and op3.get()!='' and op4.get!='' and ans.get()!='-select-':
        
        a=ques.get()
        b=op1.get()
        g=op2.get()
        d=op3.get()
        e=op4.get()
        f=ans.get()
        try:
            c=sqlite3.connect("QUIZ.db")
            cr=c.cursor()
            #cr.execute("create table quize(question TEXT,A TEXT,B TEXT,C TEXT,D TEXT,answer TEXT)")
            cr.execute("insert into quize values('%s','%s','%s','%s','%s','%s')"%(a,b,g,d,e,f))
            
            c.commit()
            cr.close()
            tkinter.messagebox.showinfo("program",'Question Saved.......')
        except:
            tkinter.messagebox.showinfo("program",'Question Not Saved.......')
    else:
        tkinter.messagebox.showinfo("program",'Check your input and try again.......')
def reset():
    ques.set('')
    op1.set('')
    op2.set('')
    op3.set('')
    op4.set('')
    ans.set('')
def exiti():
    root.destroy()
button=Button(frame6,padx=5,pady=5,text='Save',font=('arial 16 bold'),bd=10,width=8,bg='green',command=save)
button.grid(row=8,column=5)
button1=Button(frame6,padx=5,pady=5,text='Reset',font=('arial 16 bold'),bd=10,width=8,bg='orange',command=reset)
button1.grid(row=8,column=6)
button2=Button(frame6,padx=5,pady=5,text='Exit',font=('arial 16 bold'),bd=10,width=8,bg='red',command=exiti)
button2.grid(row=8,column=7)
root.mainloop()
