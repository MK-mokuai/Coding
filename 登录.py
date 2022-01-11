from tkinter import *
root = Tk()
root.title('Login System.Made by NKH.Liu@2022.1.8')
root.geometry('620x400')

Logsta = StringVar()
ssta = StringVar()
qcheck = StringVar()
q_check = StringVar()

q_check.set('Quit')
q_tem= 0
time_loginfail = 0

Aetem = StringVar()
Petem = StringVar()

RightAc = StringVar()
RightPa = StringVar()
blank_entry = StringVar()

RightAc = 'mk'
RightPa = 'mokuai'
blank_entry = ''

def login():
    global Ae,Pe,RightAc,RightPa,AE,PE,time_loginfail
    Aetem = Ae.get()
    Petem = Pe.get()
    if Aetem == RightAc and Petem == RightPa:
        Logsta.set('Welcome Back.mk@tkinter.py')
        root.destroy()
        Aw = Tk()
        Aw.title(Aetem)
        Aw.geometry('700x700')
        API = Label(Aw,text='Welcome Back').place(x=324,y=320)
    else:
        Logsta.set('Wrong Account or Password.')
        time_loginfail = time_loginfail + 1
        if time_loginfail == 5:
            Logsta.set('You have already tried for 5 times.')
            Ae.set('You dirty hacker.')
            Pe.set('You dirty hacker.')
        if time_loginfail == 10:
            Logsta.set('I will shut down if you keep trying.')
        if time_loginfail == 11:
            root.destroy()
def Su():
    global Ae,Pe,RightAc,RightPa,AE,PE
    if Ae.get() == blank_entry or Pe.get() == blank_entry:
        ssta.set('Account or Password cannot be blank.')
    else:
        ssta.set('            Successfully Rigistered.')
def Quit():
    global q_tem
    if q_tem == 0:
        q_tem = 1
        qcheck.set('Really wanna quit?')
        q_check.set('Yes')
    else:
        root.destroy()
blank = Label(root,text='           ').place(x=0,y=0)
A = Label(root,text='Account:',font=('Arial',10)).place(x=130,y=70)

Ae = StringVar()
AE = Entry(root,textvariable=Ae,bd=3,highlightcolor='blue',justify='center',width='25').place(x=255,y=70)

P = Label(root,text='Password:',font=('Arial',10)).place(x=125,y=120)
Pe = StringVar()
PE = Entry(root,textvariable=Pe,bd=3,highlightcolor='blue',justify='center',width='25').place(x=255,y=120)

Log = Button(root,text='Login',command=lambda:login(),width='7').place(x=133,y=200)

LOGSTA = Label(root,textvariable=Logsta,fg='red').place(x=200,y=250)

S = Button(root,text='Sign Up:',command=lambda:Su()).place(x=266,y=200)

SSTA = Label(root,textvariable=ssta,fg='green').place(x=170,y=270)

Q = Button(root,textvariable=q_check,command=lambda:Quit(),width='7').place(x=399,y=200)

QSTA = Label(root,textvariable=qcheck,fg='purple').place(x=240,y=290)

root.mainloop()