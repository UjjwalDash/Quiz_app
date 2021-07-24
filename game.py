from tkinter import *
import sqlite3
import random
import time
import tkinter.messagebox

global root
root=Tk()
L=[]
L1=[]
L2=[]
L3=[]
ans1=IntVar()
ans2=IntVar()
ans3=IntVar()
ans4=IntVar()
#
ans1.set(0)
ans2.set(0)
ans3.set(0)
ans4.set(0)
score=StringVar()
score.set('')
#check button
varA=IntVar()
varB=IntVar()
varC=IntVar()
varD=IntVar()
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
varA.set(0)
varB.set(0)
varC.set(0)
varD.set(0)
#
root.configure(bg='yellow')
top=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
top.pack(side=TOP)
frame=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame.pack(side=TOP)
frame1=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame1.pack(side=TOP)
frame2=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame2.pack(side=TOP)
frame3=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame3.pack(side=TOP)
frame4=Frame(root,bg='Yellow',bd=10,relief=RIDGE)
frame4.pack(side=TOP)
frame6=Frame(root,bg='Blue',bd=10,relief=RIDGE)
frame6.pack(side=TOP)
frame7=Frame(root,bg='Blue',bd=10,relief=RIDGE)
frame7.pack(side=RIGHT)


def countDown():
    check = 0
    for k in range(90, 0, -1):
        
        if k == 1:
            check=-1
        timer.configure(text=k)
        frame7.update()
        time.sleep(1)
        
    timer.configure(text="Times up!")
    if check==-1:
        return (-1)
    else:
        return 0
S=[]
def reset():
    confirm()
    ques.set('')
    op1.set('')
    op2.set('')
    op3.set('')
    op4.set('')
    varA.set(0)
    varB.set(0)
    varC.set(0)
    varD.set(0)
    def clk():
        crr=sqlite3.connect("QUIZ.db")
        c=crr.cursor()
        c.execute('select* from quize')
        l=c.fetchall()
        d={}
        L=[]
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4],row[5]
            L.append(row[0])
        try:    
            s=random.randint(0,len(L))
            check()
            b=d[L[s]]   
            A=b[0]
            B=b[1]
            C=b[2]
            D=b[3]
            answer=b[4]
            ques.set(L[s])
            op1.set(A)
            op2.set(B)
            op3.set(C)
            op4.set(D)
            ans.set(answer)
            S.append(s)
            #
        except:
           return None
    def check():
        for i in S:
            if i==S:
                s=random.randint(0,len(L))
            else:
                continue
    #check()
    clk()

def A ( ):
    if (varA.get() == 1):
        option1txt.configure(state = NORMAL)
        option1txt.configure(bg='green')
        option1txt.configure(state = DISABLED)
        option1txt.focus ( )
        varB.set(0)
        varC.set(0)
        varD.set(0)
        
        
    elif (varA.get() == 0):
        option1txt.configure(state = DISABLED)
def B ( ):
    if (varB.get() == 1):
        option2txt.configure(state = NORMAL)
        option2txt.configure(bg='green')
        option2txt.configure(state = DISABLED)
        option2txt.focus ( )
        varA.set(0)
        varC.set(0)
        varD.set(0)
        
    elif (varB.get() == 0):
        option2txt.configure(state = DISABLED)
def C ( ):
    if (varC.get() == 1):
        option3txt.configure(state = NORMAL)
        option3txt.configure(bg='green')
        option3txt.configure(state = DISABLED,bg='green')
        option3txt.focus ( )
        varB.set(0)
        varA.set(0)
        varD.set(0)
        
    elif (varC.get() == 0):
        option2txt.configure(state = DISABLED)
def D ( ):
    if (varD.get() == 1):
        option4txt.configure(state = NORMAL)
        option4txt.configure(bg='green')
        option4txt.configure(state = DISABLED)
        option4txt.focus ( )
        varB.set(0)
        varC.set(0)
        varA.set(0)
        
    elif (varD.get() == 0):
        option4txt.configure(state = DISABLED)

def confirm():
    
    if varA.get()==1:
        try:
            q=ques.get()
            cnx=sqlite3.connect('QUIZ.db')
            Cursor=cnx.cursor()
            query=("SELECT * FROM quize WHERE question='%s'"%q)
            Cursor.execute(query)
            for(question,A,B,C,D,answer) in Cursor:
                s=answer
                if s=='A':
                    ans1.set(1)
                    ans2.set(0)
                    ans3.set(0)
                    ans4.set(0)
                else:
                    ans1.set(0)
                    return None
            
            cnx.commit()
            Cursor.close()
        except:
            return None
    elif varB.get()==1:
        try:
            q=ques.get()
            cnx=sqlite3.connect('QUIZ.db')
            Cursor=cnx.cursor()
            query=("SELECT * FROM quize WHERE question='%s'"%q)
            Cursor.execute(query)
            for(question,A,B,C,D,answer) in Cursor:
                s=answer
                if s=='B':
                    ans2.set(1)
                    ans1.set(0)
                    ans3.set(0)
                    ans4.set(0)
                else:
                    ans2.set(0)
                    return None
            
            cnx.commit()
            Cursor.close()
        except:
            return None
    elif varC.get()==1:
        try:
            q=ques.get()
            cnx=sqlite3.connect('QUIZ.db')
            Cursor=cnx.cursor()
            query=("SELECT * FROM quize WHERE question='%s'"%q)
            Cursor.execute(query)
            for(question,A,B,C,D,answer) in Cursor:
                s=answer
                if s=='C':
                    ans3.set(1)
                    ans2.set(0)
                    ans1.set(0)
                    ans4.set(0)
                else:
                    ans3.set(0)
                    return None
            
            cnx.commit()
            Cursor.close()
        except:
            return None
    elif varD.get()==1:
        try:
            q=ques.get()
            cnx=sqlite3.connect('QUIZ.db')
            Cursor=cnx.cursor()
            query=("SELECT * FROM quize WHERE question='%s'"%q)
            Cursor.execute(query)
            for(question,A,B,C,D,answer) in Cursor:
                s=answer
                if s=='D':
                    ans4.set(1)
                    ans2.set(0)
                    ans3.set(0)
                    ans1.set(0)
                else:
                    ans4.set(0)
                    return None
            
            cnx.commit()
            Cursor.close()
        except:
            return None
    L.append(ans1.get())
    L1.append(ans2.get())
    L2.append(ans3.get())
    L3.append(ans4.get())
        
def exiti():
    confirm()
    a1=0
    b=0
    c=0
    d=0
    for i in L:
        a12=int(i)
        a1=a1+a12
    for j in L1:
        b1=int(j)
        b=b+b1
    for k in L2:
        c1=int(k)
        c=c+c1
    for l in L3:
        d1=int(l)
        d=d+d1
    a=a1+b+c+d
    tkinter.messagebox.showinfo('program',"Your Score is '%s'"%a)
    root.destroy()
    
#Heading
head=Label(top,bg='Yellow',padx=5,pady=5,text='Quiz',font=('arial 30 bold'))
head.grid(row=0,column=0)
#Question
question=Label(frame,bg='Yellow',padx=5,pady=5,text='Questions',font=('arial 16 bold'))
question.grid(row=0,column=0)
questiontxt=Entry(frame,textvar=ques,font=('arial 16 bold'),bd=5,width=70,state=DISABLED)
questiontxt.grid(row=0,column=1)
#Options
#Option_1
option1=Checkbutton(frame1,bg='Yellow',padx=5,pady=5,text='(A)',font=('arial 16 bold'),variable=varA,command=A)
option1.grid(row=0,column=0)
option1txt=Entry(frame1,textvar=op1,font=('arial 16 bold'),bd=5,width=30,state=DISABLED)
option1txt.grid(row=0,column=1)
#Option_2
option2=Checkbutton(frame2,bg='Yellow',padx=5,pady=5,text='(B)',font=('arial 16 bold'),variable=varB,command=B)
option2.grid(row=0,column=0)
option2txt=Entry(frame2,textvar=op2,font=('arial 16 bold'),bd=5,width=30,state=DISABLED)
option2txt.grid(row=0,column=1)
#Option_3
option3=Checkbutton(frame3,bg='Yellow',padx=5,pady=5,text='(C)',font=('arial 16 bold'),variable=varC,command=C)
option3.grid(row=0,column=0)
option3txt=Entry(frame3,textvar=op3,font=('arial 16 bold'),bd=5,width=30,state=DISABLED)
option3txt.grid(row=0,column=1)
#Option_4
option4=Checkbutton(frame4,bg='Yellow',padx=5,pady=5,text='(D)',font=('arial 16 bold'),variable=varD,command=D)
option4.grid(row=0,column=0)
option4txt=Entry(frame4,textvar=op4,font=('arial 16 bold'),bd=5,width=30,state=DISABLED)
option4txt.grid(row=0,column=1)
##
button1=Button(frame6,padx=5,pady=5,text='Next',font=('arial 16 bold'),bd=10,width=8,bg='orange',command=reset)
button1.grid(row=8,column=6)
button2=Button(frame6,padx=5,pady=5,text='Exit',font=('arial 16 bold'),bd=10,width=8,bg='red',command=exiti)
button2.grid(row=8,column=7)
timer = Label(root)
timer.place(relx=0.8,rely=0.82,anchor=CENTER)
reset()
y = countDown()
if y == -1:
    exiti()
root.mainloop()
