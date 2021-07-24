# Quiz_app
It is a quiz application.
Basically their are two login
1.user login:- The user can only be allowed to give the quiz
2.Admin login:-The Admin have the asses of all the things such as adding questions,deleting questions,adding admins,and playing quiz
the defult admin username and password is ```xyz ``` and ```1234``` respectively.
All the data such as username passwords questions are save in ```quiz.db```

what inside ```quiz.db```
Their are mainly 4 tables
1.adminSinghUp:-in this table all username and passwords of admins are saved.
2.quize:-in this all the question answer and options are saved.
3.user:-in this all the user datails are saved
4.userSignUp:- in this all user sign up information are saved

How it's work?
I had use ```Tkinter``` module of python to develop its whole gui.
In this project i had use the ```sqlite3```  database which is defult database in python
basically all the qustions that are saved in the database are displayed in the screen randomly for this 
i had use ```random``` module of python.
After few minutes the program will automatically close and score will be shown on your screen.
