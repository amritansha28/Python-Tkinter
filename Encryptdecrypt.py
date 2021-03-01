import onetimepad
from tkinter import *
root=Tk()
root.title("CRYPTOGRAPHY")
root.geometry("1100x230")
def eM():
    pt=e1.get()
    ct=onetimepad.encrypt(pt,'random')
    e2.insert(0,ct)
def dM():
    ct1=e3.get()
    pt1=onetimepad.decrypt(ct1,'random')
    e4.insert(0,pt1)
label1=Label(root,text='Plain text:',bd=20,font=('Forte', 19, 'bold')).grid(row=50,column=1)
label2=Label(root,text='Encrypted text:',bd=20,font=('Forte', 19, 'bold')).grid(row=61,column=1)
label3=Label(root,text='Cipher text:',bd=20,font=('Forte', 19, 'bold')).grid(row=50,column=10)
label4=Label(root,text='Decrypted text:',bd=20,font=('Forte', 19, 'bold')).grid(row=61,column=10)
e1=Entry(root,bd=20,font=('Forte',19,'bold'))
e1.grid(row=50,column=2)
e2=Entry(root,bd=20,font=('Forte',19,'bold'))
e2.grid(row=61,column=2)
e3=Entry(root,bd=20,font=('Forte',19,'bold'))
e3.grid(row=50,column=11)
e4=Entry(root,bd=20,font=('Forte',19,'bold'))
e4.grid(row=61,column=11)
ent=Button(root,text="Encrypt",bg="red",fg="white",command=eM,bd=20,font=('Forte',19,'bold')).grid(row=63,column=2)
b2=Button(root,text="Decrypt",bg="green",fg="white",command=dM,bd=20,font=('Forte',19,'bold')).grid(row=63,column=11)
root.mainloop()


