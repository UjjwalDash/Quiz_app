import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
import tkinter.messagebox
from tkinter import ttk
def loginPage(logdata):
    sup.destroy()
    global login
    login=Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#101357")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="yellow")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="USER LOGIN",fg="black",bg="yellow")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="USER NAME:",fg='black',bg='yellow')
    ulabel.place(relx=0.12,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.35,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="PASSWORD:",fg='black',bg='yellow')
    plabel.place(relx=0.13,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = password, show='*')
    pas.config(width=42)
    pas.place(relx=0.35,rely=0.5)

    def check():
        try:
            cnx=sqlite3.connect('QUIZ.db')
            Cursor=cnx.cursor()
            Query=("SELECT USERNAME,PASSWORD FROM userSignUp")
            Cursor.execute(Query)
            for (user,passworde) in Cursor:
                a=user
                b=passworde
                if a == user_name.get() and b == password.get():
                    menu()
                    break
                else:
                    error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='yellow')
                    error.place(relx=0.37,rely=0.7)
            cnx.commit()
                #Cursor.close()
        except:
            tkinter.messagebox.showinfo('program','Check Your input and try again...')
    def bac():
        login.destroy()
        start()
    
    #LOGIN BUTTON
    log = Button(login_frame,text='LOGIN',fg='black',bg='yellow',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    log1 = Button(login_frame,text='<<Back',fg='black',bg='yellow',padx=5,pady=5,width=5,command=bac)
    log1.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log1.place(relx=0.1,rely=0.6)
    
     
    login.mainloop()

      
def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#101357")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="yellow")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="QUIZ APP SIGNUP",fg="black",bg="yellow")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="FULL NAME:",fg='black',bg='yellow')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.35,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="USERNAME:",fg='black',bg='yellow')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.35,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="PASSWORD:",fg='black',bg='yellow')
    plabel.place(relx=0.21,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='blue',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.35,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="COUNTRY:",fg='black',bg='yellow')
    clabel.place(relx=0.215,rely=0.7)
    c = tkinter.ttk.Combobox(sup_frame,textvariable = country,state='randomly')
    c.config(width=42)
    c.place(relx=0.35,rely=0.7)
    c['value']=("-select-",'India','China','Nepal','Bhutan','Bangladash','Sri Lanka','Austrilia','Others')
    c.current(0)
    def addUserToDataBase():
        if fname.get()!='' and uname.get()!='' and passW.get()!='' and country.get()!='-select-':
            fullname = fname.get()
            username = uname.get()
            password = passW.get()
            countryd = country.get()
            
            conn = sqlite3.connect('QUIZ.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES ('%s','%s','%s','%s')"%(fullname,username,password,countryd)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
         #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            create.close()
            tkinter.messagebox.showinfo('program','You are sign in...')

        else:
            tkinter.messagebox.showinfo('program','Check Your input and try again...')

#---------------------------------------------------------------------------------
    
    def lod():
        sup.destroy()
        login=Tk()
        
        user_name = StringVar()
        password = StringVar()
        
        login_canvas = Canvas(login,width=720,height=440,bg="#101357")
        login_canvas.pack()

        login_frame = Frame(login_canvas,bg="yellow")
        login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

        heading = Label(login_frame,text="ADMIN LOGIN",fg="black",bg="yellow")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2,rely=0.1)

        #USER NAME
        ulabel = Label(login_frame,text="USER NAME:",fg='black',bg='yellow')
        ulabel.place(relx=0.12,rely=0.4)
        uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
        uname.config(width=42)
        uname.place(relx=0.35,rely=0.4)

        #PASSWORD
        plabel = Label(login_frame,text="PASSWORD:",fg='black',bg='yellow')
        plabel.place(relx=0.13,rely=0.5)
        pas = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = password, show='*')
        pas.config(width=42)
        pas.place(relx=0.35,rely=0.5)
        def check():
            try:
                cnx=sqlite3.connect('QUIZ.db')
                Cursor=cnx.cursor()
                Query=("SELECT USERNAME,PASSWORD FROM adminSignUp")
                Cursor.execute(Query)
                for (user,passworde) in Cursor:
                    a=user
                    b=passworde
                    if a == user_name.get() and b == password.get():
                        menu1()
                        break
                    else:
                        error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='yellow')
                        error.place(relx=0.37,rely=0.7)
                cnx.commit()
                #Cursor.close()
            except:
                tkinter.messagebox.showinfo('program','Check Your input and try again...')
        def bec():
            login.destroy()
            start()
        log  = Button(login_frame,text='LOGIN',fg='black',bg='yellow',padx=5,pady=5,width=5,command=check)
        log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
        log.place(relx=0.4,rely=0.6)
        log1  = Button(login_frame,text='<<Back',fg='black',bg='yellow',padx=5,pady=5,width=5,command=bec)
        log1.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
        log1.place(relx=0.1,rely=0.6)
    
        def menu1():
            login.destroy()
            menu11= Tk()
            #menu11.maxsize(500,500)
            #menu11.minsize(500,500)
            #menu11.configure(bg='Powder Blue')
            #-----------------
            menu_canvas = Canvas(menu11,width=720,height=440,bg="#101357")
            menu_canvas.pack()

            menu112 = Frame(menu_canvas,bg="red")
            menu112.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

            wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="#101357") 
            wel.config(font=('Broadway 22'))
            wel.place(relx=0.1,rely=0.02)
            #----------------
            
            
            level = Label(menu112,text='Lets start the game !!',bg="red",font="calibri 18")
            level.place(relx=0.25,rely=0.3)
            
            
            var = IntVar()
            easyR = Radiobutton(menu112,text='Click here To Begin The Game...',bg="red",font="calibri 16",value=1,variable = var)
            easyR.place(relx=0.25,rely=0.4)
            easyR1 = Radiobutton(menu112,text='Click here To Add Question...',bg="red",font="calibri 16",value=2,variable = var)
            easyR1.place(relx=0.25,rely=0.5)
            easyR2 = Radiobutton(menu112,text='Add New Admin...',bg="red",font="calibri 16",value=3,variable = var)
            easyR2.place(relx=0.25,rely=0.6)
            easyR2 = Radiobutton(menu112,text='Delete Question...',bg="red",font="calibri 16",value=4,variable = var)
            easyR2.place(relx=0.25,rely=0.7)
           
            
            def navigate():
                
                x = var.get()
                if x == 1:
                    menu11.destroy()
                    easy()
                    start()
                if x == 2:
                    menu11.destroy()
                    add()
                    start()
                if x == 3:
                    menu11.destroy()
                    AdminsignUpPage()
                    start()
                if x == 4:
                    menu11.destroy()
                    delete()
                    start()
                else:
                    pass
            def bac():
                menu11.destroy()
                start()
            letsgo = Button(menu112,text="Let's Go..!! ",bg="white",font="calibri 12",command=navigate)
            letsgo.place(relx=0.25,rely=0.8)
            letsgo1 = Button(menu112,text="<<Back",bg="white",font="calibri 12",command=bac)
            letsgo1.place(relx=0.1,rely=0.8)
            menu11.mainloop()
        
#-------------------------------------------------------------------------------
        
                
             
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #SIGNUP LOGIN BUTTON
    sp = Button(sup_frame,text='SIGN UP',padx=5,pady=5,width=5,command = addUserToDataBase)
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='LOGIN ',padx=5,pady=5,width=5,command = gotoLogin,bg="pink")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.1,rely=0.9)


    Alog= Button(sup_frame,text='ADMIN LOGIN',padx=5,pady=5,width=5,command =lod,bg="coral")
    Alog.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    Alog.place(relx=0.7,rely=0.9)


    



    sup.mainloop()
def AdminsignUpPage():
    #root.destroy()
    global sup
    sup = Tk()

    fname1 = StringVar()
    uname1 = StringVar()
    passW = StringVar()
    country = StringVar()

    

    sup_canvas = Canvas(sup,width=720,height=440,bg="#101357")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="yellow")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text=" Admin SIGNUP",fg="black",bg="yellow")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="FULL NAME:",fg='black',bg='yellow')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname1)
    fname.config(width=42)
    fname.place(relx=0.35,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="USERNAME:",fg='black',bg='yellow')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname1)
    user.config(width=42)
    user.place(relx=0.35,rely=0.5)


    #password
    plabel = Label(sup_frame,text="PASSWORD:",fg='black',bg='yellow')
    plabel.place(relx=0.21,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='blue',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.35,rely=0.6)



    #country
    clabel = Label(sup_frame,text="COUNTRY:",fg='black',bg='yellow')
    clabel.place(relx=0.215,rely=0.7)
    c = tkinter.ttk.Combobox(sup_frame,textvariable = country,state='randomly')
    c.config(width=42)
    c.place(relx=0.35,rely=0.7)
    c['value']=("-select-",'India','China','Nepal','Bhutan','Bangladash','Sri Lanka','Austrilia','Others')
    c.current(0)
    
    #function
    def addUserToDataBase1():
        if fname1.get()!='' and uname1.get()!='' and passW.get()!='' and country.get()!='':
            fullname = fname1.get()
            username = uname1.get()
            password = passW.get()
            countryd = country.get()

            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS adminSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO adminSignUp VALUES ('%s','%s','%s','%s')"%(fullname,username,password,countryd)) 
            conn.commit()
            create.execute('SELECT * FROM adminSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            create.close()
            #loginPage(z)
            
        else:
            return None
    # sign up
    sp = Button(sup_frame,text='SIGN UP',padx=5,pady=5,width=5,command = addUserToDataBase1)
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.35,rely=0.8)
def menu():
    login.destroy()
    global menu 
    menu = Tk()


    menu_canvas = Canvas(menu,width=720,height=440,bg="#101357")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="red")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)


    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    
    level = Label(menu_frame,text='Lets start the game !!',bg="red",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='ARE YOU SURE YOU WANT TO PLAY',bg="red",font="calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
   
    
    def navigate():
        
        x = var.get()
        if x == 1:
            menu.destroy()
            easy()
            start()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go..!! ",bg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def add():
    import add
def easy():
    import game
def delete():
    import dele
    



def start():
    global root 

    root=Tk()
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    #img = PhotoImage(file="output-onlinepngtools.png")
    #canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text= "LET'S START THE QUIZ" , command = signUpPage) 
    button.configure(width = 109 ,height=3,bg="orange", activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)
    root.mainloop()

    
    
if __name__=='__main__':
    start()
