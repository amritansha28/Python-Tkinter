from tkinter import *
from PIL import Image, ImageTk
from functools import partial
def vL(u,p):
    if u.get()=="amrit" and p.get()=="abc123":
        a=Tk()
        a.geometry( "1280x800" )
        a.title("Hi man")
        a.configure(background="gold")
    else:
        a=Tk()
        a.geometry( "710x108" )
        a.title("Invalid Credentials")
        a.configure(background="gold")
        M=Label(a,text="Invalid Username or Password!!",font=("Cooper Black",30),bg="grey",fg="orange",bd=30,relief=GROOVE).grid(row=0,column=0)
a=Tk()  
a.geometry('713x297')  
a.title('||LOGIN||')
a.configure(background="red")
uLabel=Label(a,text="Username:",font=("Comic Sans MS",20),bg="grey",fg="gold",bd=30,relief=GROOVE).grid(row=0,column=0)
u=StringVar()
uEntry=Entry(a,textvariable=u,font=("Comic Sans MS",20)).grid(row=0,column=2)  
pLabel=Label(a,text="Password: ",font=("Comic Sans MS",20),bg="grey",fg="gold",bd=30,relief=GROOVE).grid(row=1,column=0)  
p=StringVar()
pEntry=Entry(a,textvariable=p,show='*',font=("Comic Sans MS",20)).grid(row=1,column=2)  
vL=partial(vL,u,p)
loginButton=Button(a,text="Login",command=vL,font=("Cooper Black",25),width=7,bg="black",fg="blue",relief=GROOVE,bd=15).grid(row=3,column=1) 
a.mainloop()
