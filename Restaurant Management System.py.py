from  tkinter import*
from tkinter import messagebox
import random
import time
import datetime
import tkinter.messagebox
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN AAGF")
        self.root.geometry("1280x800+0+0")
        self.root.configure(background="gold")
        #variables
        self.uname=StringVar()
        self.pass_=StringVar()
        bg_lbl=Label(self.root).pack()
        title=Label(self.root,text="RESTAURANT LOGIN !!", font=("forte",40,"bold"),bg="dark red",fg="blue",bd=60,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1) 
        b=Frame(self.root,bg="dark red",bd=30,relief=GROOVE)
        b.place(x=510,y=280)
        lbluser=Label(b,text="Username :",compound=LEFT,font=("chiller",20,"bold" ),fg="purple")
        lbluser.grid(row=1,column=0,padx=50,pady=50)
        txtuser=Entry(b,bd=3,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1 ,padx=20)
        lblpass=Label(b,text="Password :",compound=LEFT,font=("chiller",20,"bold"),fg="purple")
        lblpass.grid(row=2,column=0,padx=10,pady=10)
        txtpass=Entry(b,bd=3,textvariable=self.pass_ ,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
        a=Button(b,text="||LOGIN||",width=15,command=login,font=("chiller",14,"bold"),bg="BLACK",fg="blue",relief=GROOVE,bd=20)
        a.grid(row=3,column=1,pady=10)
def  login( ):
    root= Tk()
    root.geometry( "1280x800+0+0" )
    root.title("MENU AAGF")
    root.configure(background="gold")
    # ----------------------total main Frame-----------------------------
    amritansh=Frame(root,width=15,height=100,bd=25,relief="raise")
    amritansh.pack(side=TOP)
    # ----------------------button connection-----------------------------
    abc=Frame(root,width=15,height=100,bd=12,relief="raise")
    abc.pack(side=BOTTOM)
    efg=Frame(abc,width=15,height=100,bd=12,relief="raise")
    efg.pack(side=LEFT)
    ijk=Frame(abc,width=15,height=100,bd=12,relief="raise")
    ijk.pack(side=RIGHT)
    #------------------------main left Frame-----------------------------
    gaurav=Frame(root,width=2000,height=650,bd=13,relief="raise")
    gaurav.pack(side=LEFT)
    #------------------------left left Frame-----------------------------
    azhar=Frame(gaurav,width=450,height=330,bd=13,relief="raise")
    azhar.pack(side=LEFT)
    #----------------------left left top Frame---------------------------
    f1=Frame(azhar,width=450,height=330,bd=13,relief="raise")
    f1.pack(side=TOP)
    #---------------------left left bottom Frame-------------------------
    f2=Frame(azhar,width=450,height=330,bd=13,relief="raise")
    f2.pack(side=BOTTOM)
    #------------------------left right Frame----------------------------
    f3=Frame(gaurav,width=450,height=330,bd=13,relief="raise")
    f3.pack(side=RIGHT)
    #----------------------left right top Frame--------------------------
    f1r=Frame(f3,width=450,height=330,bd=13,relief="raise")
    f1r.pack(side=TOP)
    #--------------------left right bottom Frame-------------------------
    f1s=Frame(f3,width=450,height=330,bd=13,relief="raise")
    f1s.pack(side=BOTTOM)
    #------------------------main right Frame----------------------------
    faisal=Frame(root,width=440,height=650,bd=13,relief="raise")
    faisal.pack(side=RIGHT)
    #------------------------right left Frame----------------------------
    f4=Frame(faisal,width=440,height=450,bd=13,relief="raise")
    f4.pack(side=LEFT)
    #----------------------right left top Frame--------------------------
    f1e=Frame(f4,width=450,height=330,bd=13,relief="raise")
    f1e.pack(side=TOP)
    #---------------------right left bottom Frame------------------------
    f1f=Frame(f4,width=450,height=330,bd=13,relief="raise")
    f1f.pack(side=BOTTOM)
    #------------------------right right Frame---------------------------
    f5=Frame(faisal,width=440,height=3000,bd=13,relief="raise")
    f5.pack(side=RIGHT)
    #----------------------right right top Frame-------------------------
    f1g=Frame(f5,width=450,height=330,bd=13,relief="raise")
    f1g.pack(side=TOP)
    #---------------------right right bottom Frame-----------------------
    f1h=Frame(f5,width=450,height=9000,bd=13,relief="raise")
    f1h.pack(side=BOTTOM)
    #--------------------------frame colours---------------------------
    amritansh.configure(background='dark red')
    gaurav.configure(background='green')
    faisal.configure(background='green')
    azhar.configure(background='dark red')
    f3.configure(background='dark red')
    f4.configure(background='dark red')
    f5.configure(background='dark red')
    f1.configure(background='green')
    f2.configure(background='purple')
    f1r.configure(background='green')
    f1s.configure(background='purple')
    f1e.configure(background='green')
    f1f.configure(background='purple')
    f1g.configure(background='green')
    f1h.configure(background='purple')
    abc.configure(background='dark red')
    efg.configure(background='dark red')
    ijk.configure(background='dark red')
    #-----------------------------main header name-------------------------------
    lblinfo=Label(amritansh, font=('forte',45,'bold'), text="....Menu....",bd=10)
    lblinfo.grid(row=0,column=0)
    #==========================left Foods Side Heading===========================
    FOODS=Label(f1, text="      ...FOODS...      ",font=('Bernard MT Condensed', 24, 'bold'),bd=10)
    FOODS.grid(row=0,column=0)
    #=========================left Foods Side Heading 2==========================
    PRICES1=Label(f1r, text="   ...PRICES...   ",font=('Bernard MT Condensed', 24, 'bold'),bd=10)
    PRICES1.grid(row=0,column=0)
    #==========================Right Foods Side Heading=========================
    BEVERAGES=Label(f1e, text="  ...BEVERAGES...  ",font=('Bernard MT Condensed', 24, 'bold'),bd=10)
    BEVERAGES.grid(row=0,column=0)
    #=========================Right Foods Side Heading 2=========================
    PRICES2=Label(f1g, text="   ...PRICES...   ",font=('Bernard MT Condensed', 24, 'bold'),bd=10)
    PRICES2.grid(row=0,column=0)
    #=============================left Foods Side===============================
    Burger =Label(f2, text=" Burger.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=0,column=0)
    Pizza =Label(f2, text=" Pizza.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=2,column=0)
    Sandwich =Label(f2, text=" Sandwich.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=4,column=0)
    Pasta =Label(f2, text=" Pasta.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=6,column=0)
    Fries =Label(f2, text=" Fries.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=8,column=0)
    Nachos =Label(f2, text=" Nachos.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=10,column=0)
    Soup =Label(f2, text=" Soup.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=12,column=0)
    Salad =Label(f2, text=" Salad.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=14,column=0)
    #=============================left Foods Side===============================
    Burger =Label(f1s, text=" Rs.70 ",font=('chiller', 19, 'bold'),bd=10).grid(row=0,column=0)
    Pizza =Label(f1s, text=" Rs.200 ",font=('chiller', 19, 'bold'),bd=10).grid(row=2,column=0)
    Sandwich =Label(f1s, text=" Rs.150 ",font=('chiller', 19, 'bold'),bd=10).grid(row=4,column=0)
    Pasta =Label(f1s, text=" Rs.100 ",font=('chiller', 19, 'bold'),bd=10).grid(row=6,column=0)
    Fries =Label(f1s, text=" Rs.60 ",font=('chiller', 19, 'bold'),bd=10).grid(row=8,column=0)
    Nachos =Label(f1s, text=" Rs.50 ",font=('chiller', 19, 'bold'),bd=10).grid(row=10,column=0)
    Soup =Label(f1s, text=" Rs.40 ",font=('chiller', 19, 'bold'),bd=10).grid(row=12,column=0)
    Salad =Label(f1s, text=" Rs.20 ",font=('chiller', 19, 'bold'),bd=10).grid(row=14,column=0)
    #=============================Right Foods Side=============================
    Coffee =Label(f1f, text=" Coffee.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=0,column=0) 
    Tea =Label(f1f, text=" Tea.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=2,column=0)
    Mojito =Label(f1f, text=" Mojito.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=4,column=0)
    Shake =Label(f1f, text=" Shake.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=6,column=0)
    Lemonade =Label(f1f, text=" Lemonade.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=8,column=0)
    Coke =Label(f1f, text=" Coke.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=10,column=0)
    Soda =Label(f1f, text=" Soda.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=12,column=0)
    Juice =Label(f1f, text=" Juice.. ",font=('chiller', 19, 'bold'),bd=10).grid(row=14,column=0)
    #=============================Right Foods Side=============================
    Coffee =Label(f1h, text=" Rs.50 ",font=('chiller', 19, 'bold'),bd=10).grid(row=0,column=0) 
    Tea =Label(f1h, text=" Rs.45 ",font=('chiller', 19, 'bold'),bd=10).grid(row=2,column=0)
    Mojito =Label(f1h, text=" Rs.55 ",font=('chiller', 19, 'bold'),bd=10).grid(row=4,column=0)
    Shake =Label(f1h, text=" Rs.60 ",font=('chiller', 19, 'bold'),bd=10).grid(row=6,column=0)
    Lemonade =Label(f1h, text=" Rs.25 ",font=('chiller', 19, 'bold'),bd=10).grid(row=8,column=0)
    Coke =Label(f1h, text=" Rs.30 ",font=('chiller', 19, 'bold'),bd=10).grid(row=10,column=0)
    Soda =Label(f1h, text=" Rs.20 ",font=('chiller', 19, 'bold'),bd=10).grid(row=12,column=0)
    Juice =Label(f1h, text=" Rs.35 ",font=('chiller', 19, 'bold'),bd=10).grid(row=14,column=0)
    #==========================left Foods Side Heading===========================
    def qbill():
        root= Tk()
        root.geometry( "1280x800+0+0" )
        root.title("BILL AAGF")
        root.configure(background="gold")
        #----------------------total main Frame------------------------------------------
        Tops=Frame(root,width=15,height=100,bd=14,relief="raise")
        Tops.pack(side=TOP)
        #--------------------------main left Frame--------------------------------------
        f1=Frame(root,width=900,height=650,bd=8,relief="raise")
        f1.pack(side=LEFT)
        #------------------------------left top Frame----------------------------------
        f1a=Frame(f1,width=900,height=330,bd=10,relief="raise")
        f1a.pack(side=TOP)
        #-------------------------------left  top left Frame-----------------------------
        f1aa=Frame(f1a,width=450,height=330,bd=25,relief="raise")
        f1aa.pack(side=LEFT)
        #--------------------------------- left top right Frame--------------------------
        f1ab=Frame(f1a,width=450,height=330,bd=25,relief="raise")
        f1ab.pack(side=RIGHT)
        #-------------------------------------left bottom Frame---------------------------
        f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
        f2a.pack(side=BOTTOM)
        #---------------------------- left bottom left Frame---------------------------
        f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
        f2aa.pack(side=LEFT)
        #------------------------left bottom right Frame------------------------------
        f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
        f2ab.pack(side=RIGHT)
        #-----------------------------main  right Frame-----------------------------------
        f2=Frame(root,width=3000,height=650,bd=8,relief="raise")
        f2.pack(side=RIGHT)
        #-------------------------right top Frame-------------------------------------
        ft2=Frame(f2,width=3000,height=450,bd=16,relief="raise")
        ft2.pack(side=TOP)
        #------------------------right bottom Frame------------------------------
        fb2=Frame(f2,width=3000,height=15,bd=16,relief="raise")
        fb2.pack(side=BOTTOM)
        #------------------------frame colours----------------------------
        Tops.configure(background='dark red')
        f1.configure(background='dark red')
        f2.configure(background='dark red')
        f1a.configure(background='dark red')
        f2a.configure(background='dark red')
        f1aa.configure(background='green')
        ft2.configure(background='green')
        f1ab.configure(background='green')
        fb2.configure(background='green')
        #--------------------------------main header name----------------------------------
        lblinfo=Label(Tops, font=('forte',50,'bold'), text="...Bill Management...",bd=25)
        lblinfo.grid(row=0,column=0)
        #-------------------------------main header name ends-----------------------------
        #------------------------------------exit function----------------------------------
        def qExit():
            qExit = tkinter.messagebox.askyesno("Quit System","Do you want to exit?")
    
            if(qExit > 0):
                root.destroy()
                return
        #----------------------------------reset function---------------------
        def qReset():
            PaidTax.set(" ")
            SubTotal.set(" ")
            TotalCost.set(" ")
            CostOfBeverages.set(" ")
            CostOfFoods.set(" ")
            ServiceCharge.set(" ")
            txtReceipt.delete("1.0",END)
            E_Burger.set("0")
            E_Pizza.set("0")
            E_Sandwich.set("0")
            E_Pasta.set("0")
            E_Fries.set("0")
            E_Nachos.set("0")
            E_Soup.set("0")
            E_Salad.set("0")
            E_Coffee.set("0")
            E_Tea.set("0")
            E_Mojito.set("0")
            E_Shake.set("0")
            E_Lemonade.set("0")
            E_Coke.set("0")
            E_Soda.set("0")
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)    
            txtBurger.configure(state="disabled")
            txtPizza.configure(state="disabled")
            txtSandwich.configure(state="disabled")
            txtPasta.configure(state="disabled")
            txtFries.configure(state="disabled")
            txtNachos.configure(state="disabled")
            txtSoup.configure(state="disabled")
            txtSalad.configure(state="disabled")
            txtCoffee.configure(state="disabled")
            txtTea.configure(state="disabled")
            txtMojito.configure(state="disabled")
            txtShake.configure(state="disabled")
            txtLemonade.configure(state="disabled")
            txtCoke.configure(state="disabled")
            txtSoda.configure(state="disabled")
            txtJuice.configure(state="disabled")
        #=================Check Function=====================
        def chkButton():
            if(var1.get()==1):
                txtBurger.configure(state="normal")
            elif(var1.get()==0):
                txtBurger.configure(state="disabled")
                E_Burger.set("0")
            if(var2.get()==1):
                txtPizza.configure(state="normal")
            elif(var2.get()==0):
                txtPizza.configure(state="disabled")
                E_Pizza.set("0")
            if(var3.get()==1):
                txtSandwich.configure(state="normal")
            elif(var3.get()==0):
                txtSandwich.configure(state="disabled")
                E_Sandwich.set("0")
            if(var4.get()==1):
                txtPasta.configure(state="normal")
            elif(var4.get()==0):
                txtPasta.configure(state="disabled")
                E_Pasta.set("0")
            if(var5.get()==1):
                txtFries.configure(state="normal")
            elif(var5.get()==0):
                txtFries.configure(state="disabled")
                E_Fries.set("0")
            if(var6.get()==1):
                txtNachos.configure(state="normal")
            elif(var6.get()==0):
                txtNachos.configure(state="disabled")
                E_Nachos.set("0")
            if(var7.get()==1):
                txtSoup.configure(state="normal")
            elif(var7.get()==0):
                txtSoup.configure(state="disabled")
                E_Soup.set("0")
            if(var8.get()==1):
                txtSalad.configure(state="normal")
            elif(var8.get()==0):
                txtSalad.configure(state="disabled")
                E_Salad.set("0")
            if(var9.get()==1):
                txtCoffee.configure(state="normal")
            elif(var9.get()==0):
                txtCoffee.configure(state="disabled")
                E_Coffee.set("0")
            if(var10.get()==1):
                txtTea.configure(state="normal")
            elif(var10.get()==0):
                txtTea.configure(state="disabled")
                E_Tea.set("0")
            if(var11.get()==1):
                txtMojito.configure(state="normal")
            elif(var11.get()==0):
                txtMojito.configure(state="disabled")
                E_Mojito.set("0")
            if(var12.get()==1):
                txtShake.configure(state="normal")
            elif(var12.get()==0):
                txtShake.configure(state="disabled")
                E_Shake.set("0")
            if(var13.get()==1):
                txtLemonade.configure(state="normal")
            elif(var13.get()==0):
                txtLemonade.configure(state="disabled")
                E_Lemonade.set("0")
            if(var14.get()==1):
                txtCoke.configure(state="normal")
            elif(var14.get()==0):
                txtCoke.configure(state="disabled")
                E_Coke.set("0")
            if(var15.get()==1):
                txtSoda.configure(state="normal")
            elif(var15.get()==0):
                txtSoda.configure(state="disabled")
                E_Soda.set("0")
            if(var16.get()==1):
                txtJuice.configure(state="normal")
            elif(var16.get()==0):
                txtJuice.configure(state="disabled")
                E_Juice.set("0")
        #----------------------Calculate Function-------------------------
        def CostOfItem():
            Item1 = float(E_Burger.get())
            Item2 = float(E_Pizza.get())
            Item3 = float(E_Sandwich.get())
            Item4 = float(E_Pasta.get())
            Item5 = float(E_Fries.get())
            Item6 = float(E_Nachos.get())
            Item7 = float(E_Soup.get())
            Item8 = float(E_Salad.get())
            Item9 = float(E_Coffee.get())
            Item10 = float(E_Tea.get())
            Item11 = float(E_Mojito.get())
            Item12 = float(E_Shake.get())
            Item13 = float(E_Lemonade.get())
            Item14 = float(E_Coke.get())
            Item15 = float(E_Soda.get())
            Item16 = float(E_Juice.get())
            PriceOfFoods = (Item1 * 70) + (Item2 * 200) + (Item3 * 150) + (Item4 * 100) + (Item5 * 60) + (Item6 * 50) + (Item7 * 40) + (Item8 * 20)
            PriceOfBeverages = (Item9 * 50) + (Item10 * 45) + (Item11 * 55) + (Item12 * 60) + (Item13 * 25) + (Item14 * 30) + (Item15 * 20) + (Item16 * 35)
            BeveragesPrice = "Rs."+ str('%.2f'%(PriceOfBeverages))
            FoodsPrice = "Rs."+ str('%.2f'%(PriceOfFoods))
            CostOfBeverages.set(BeveragesPrice)
            CostOfFoods.set(FoodsPrice)
            SC = "Rs."+ str('%.2f'%(1.59))
            ServiceCharge.set(SC)
        #--------------------------------mention calculation of tax-----------------------------------------
            subTotal= "Rs."+ str('%.2f'%(PriceOfBeverages + PriceOfFoods + 1.59))
            SubTotal.set(subTotal)
            Tax = "Rs."+ str('%.2f'%((PriceOfBeverages + PriceOfFoods + 1.59)*0.15))
            PaidTax.set(Tax);
            TT = ((PriceOfBeverages + PriceOfFoods + 1.59)*0.15)
            TC = "Rs."+ str('%.2f'%(PriceOfBeverages + PriceOfFoods + 1.59+1.59+TT))
            TotalCost.set(TC)
        def receipt():
            txtReceipt.delete("1.0",END)
            x = random.randint(100898,6812789)
            randomRef = str(x)
            Receipt_Ref.set("Bill"+randomRef)
            txtReceipt.insert(END, 'Burger\t\t\t' + str(E_Burger.get()) + "\n")
            txtReceipt.insert(END, 'Pizza\t\t\t' + str(E_Pizza.get()) + "\n")
            txtReceipt.insert(END, 'Sandwich\t\t\t' + str(E_Sandwich.get()) + "\n")
            txtReceipt.insert(END, 'Pasta\t\t\t' + str(E_Pasta.get()) + "\n")
            txtReceipt.insert(END, 'Fries\t\t\t' + str(E_Fries.get()) + "\n")
            txtReceipt.insert(END, 'Nachos\t\t\t' + str(E_Nachos.get()) + "\n")
            txtReceipt.insert(END, 'Soup\t\t\t' + str(E_Soup.get()) + "\n")
            txtReceipt.insert(END, 'Salad\t\t\t' + str(E_Salad.get()) + "\n")
            txtReceipt.insert(END, 'Coffee\t\t\t' + str(E_Coffee.get()) + "\n")
            txtReceipt.insert(END, 'Tea\t\t\t' + str(E_Tea.get()) + "\n")
            txtReceipt.insert(END, 'Mojito\t\t\t' + str(E_Mojito.get()) + "\n")
            txtReceipt.insert(END, 'Shake\t\t\t' + str(E_Shake.get()) + "\n")
            txtReceipt.insert(END, 'Lemonade\t\t\t' + str(E_Lemonade.get()) + "\n")
            txtReceipt.insert(END, 'Coke\t\t\t' + str(E_Coke.get()) + "\n")
            txtReceipt.insert(END, 'Soda\t\t\t' + str(E_Soda.get()) + "\n")
            txtReceipt.insert(END, 'Juice\t\t\t' + str(E_Juice.get()) + "\n")
            txtReceipt.insert(END, 'Cost Of Foods\t\t\t' + str(CostOfFoods.get()) + "\n")
            txtReceipt.insert(END, 'Cost Of Beverges\t\t\t' + str(CostOfBeverages.get()) + "\n")
            txtReceipt.insert(END, 'Tax Paid:\t\t\t' + str(PaidTax.get()) + "\n")
            txtReceipt.insert(END, 'Service Charge\t\t\t' + str(ServiceCharge.get()) + "\n")
            txtReceipt.insert(END, 'Total Cost\t\t\t' + str(TotalCost.get()) + "\n")
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m%y"))
        Receipt = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()
        CostOfBeverages = StringVar()
        CostOfFoods = StringVar()
        ServiceCharge = StringVar()
        Receipt_Ref = StringVar()
        #============================Food Input==============================
        E_Burger = IntVar()
        E_Pizza = IntVar()
        E_Sandwich = IntVar()
        E_Pasta = IntVar()
        E_Fries = IntVar()
        E_Nachos = IntVar()
        E_Soup = IntVar()
        E_Salad = IntVar()
        E_Burger.set("0")
        E_Pizza.set("0")
        E_Sandwich.set("0")
        E_Pasta.set("0")
        E_Fries.set("0")
        E_Nachos.set("0")
        E_Soup.set("0")
        E_Salad.set("0")
        #===================Beverges Input======================
        E_Coffee = StringVar()
        E_Tea = StringVar()
        E_Mojito = StringVar()
        E_Shake = StringVar()
        E_Lemonade = StringVar()
        E_Coke = StringVar()
        E_Soda = StringVar()
        E_Juice = StringVar()
        E_Coffee.set("0")
        E_Tea.set("0")
        E_Mojito.set("0")
        E_Shake.set("0")
        E_Lemonade.set("0")
        E_Coke.set("0")
        E_Soda.set("0")
        E_Juice.set("0")
        #=================================left Foods Side================================
        Burger = Checkbutton(f1aa, text="Burger\t", variable=var1, onvalue=1,
                       offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=0, sticky=W)
        Pizza = Checkbutton(f1aa, text="Pizza\t", variable=var2, onvalue=1,
                     offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=1, sticky=W)
        Sandwich = Checkbutton(f1aa,text="Sandwch\t",variable=var3,onvalue=1,
                            offvalue=0,font=('chiller',19,'bold'),command=chkButton).grid(row=2,sticky=W)
        Pasta = Checkbutton(f1aa, text="Pasta\t", variable=var4, onvalue=1,
                      offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=3, sticky=W)
        Fries = Checkbutton(f1aa, text="Fries\t", variable=var5, onvalue=1,
                     offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=4, sticky=W)
        Nachos = Checkbutton(f1aa, text="Nachos\t", variable=var6, onvalue=1,
                         offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=5, sticky=W)
        Soup = Checkbutton(f1aa, text="Soup\t", variable=var7, onvalue=1,
                     offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=6, sticky=W)
        Salad = Checkbutton(f1aa, text="Salad\t", variable=var8, onvalue=1,
                     offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=7, sticky=W)
        #=================================left Foods Enter Side============================
        txtBurger = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Burger, justify='left', state='disabled')
        txtBurger.grid(row=0, column=1)
        txtPizza = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Pizza ,justify='left', state='disabled')
        txtPizza.grid(row=1, column=1)
        txtSandwich = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Sandwich ,justify='left', state='disabled')
        txtSandwich.grid(row=2, column=1)
        txtPasta = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Pasta , justify='left', state='disabled')
        txtPasta.grid(row=3, column=1)
        txtFries = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Fries, justify='left', state='disabled')
        txtFries.grid(row=4, column=1)
        txtNachos = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Nachos , justify='left', state='disabled')
        txtNachos.grid(row=5, column=1)
        txtSoup = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Soup , justify='left', state='disabled')
        txtSoup.grid(row=6, column=1)
        txtSalad = Entry(f1aa, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Salad , justify='left', state='disabled')
        txtSalad.grid(row=7, column=1)
        #=================================Right Foods Side================================
        Coffee = Checkbutton(f1ab, text="Coffee\t", variable=var9, onvalue=1,
                       offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=0, sticky=W)
        Tea = Checkbutton(f1ab, text="Tea\t", variable=var10, onvalue=1,
                   offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=1, sticky=W)
        Mojito = Checkbutton(f1ab, text="Mojito\t", variable=var11, onvalue=1,
                      offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=2, sticky=W)
        Shake = Checkbutton(f1ab, text="Shake\t", variable=var12, onvalue=1,
                       offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=3, sticky=W)
        Lemonade = Checkbutton(f1ab, text="Lemonde\t", variable=var13, onvalue=1,
                             offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=4, sticky=W)
        Coke = Checkbutton(f1ab, text="Nachos\t", variable=var14, onvalue=1,
                     offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=5, sticky=W)
        Soda = Checkbutton(f1ab, text="Soda\t", variable=var15, onvalue=1,
                     offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=6, sticky=W)
        Juice = Checkbutton(f1ab, text="Juice\t", variable=var16, onvalue=1,
                     offvalue=0,font=('chiller', 19, 'bold'), command=chkButton).grid(row=7, sticky=W)
        #============================Right Foods Enter Side============================
        txtCoffee = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Coffee, justify='left', state='disabled')
        txtCoffee.grid(row=0, column=1)
        txtTea = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Tea ,justify='left', state='disabled')
        txtTea.grid(row=1, column=1)
        txtMojito = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Mojito ,justify='left', state='disabled')
        txtMojito.grid(row=2, column=1)
        txtShake = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Shake , justify='left', state='disabled')
        txtShake.grid(row=3, column=1)
        txtLemonade = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Lemonade, justify='left', state='disabled')
        txtLemonade.grid(row=4, column=1)
        txtCoke = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Coke , justify='left', state='disabled')
        txtCoke.grid(row=5, column=1)
        txtSoda = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Soda , justify='left', state='disabled')
        txtSoda.grid(row=6, column=1)
        txtJuice = Entry(f1ab, font=('forte', 15, 'bold'), bd=8, width=22,textvariable=E_Juice , justify='left', state='disabled')
        txtJuice.grid(row=7, column=1)
        #=======================for receipt frame===========================
        lblReceipt = Label(ft2, font=('Harlow Solid Italic', 20, 'bold'), text="Restaurant Receipt",bd=2).grid(row=0, column=0, sticky=W)
        txtReceipt = Text(ft2, font=('bell mt', 13, 'bold'), bd=8, width=21)
        txtReceipt.grid(row=2, column=0)
        #==========================cost of Item Information==================
        lblCostOfFoods=Label(f2aa, font=('Comic Sans MS', 13, 'bold'), text="Enter the Amount Per Cost Of Foods:", bd=8)
        lblCostOfFoods.grid(row=0, column=0, sticky=W)
        txtCostOfFoods=Entry(f2aa, font=('Comic Sans MS', 13, 'bold'), bd=6, width=22, justify='left', textvariable=CostOfFoods) 
        txtCostOfFoods.grid(row=0, column=1, sticky=W)
        lblCostOfBeverages=Label(f2aa, font=('Comic Sans MS', 13, 'bold'), text="Enter the Amount Per Cost Of Beverages:", bd=8)
        lblCostOfBeverages.grid(row=1, column=0, sticky=W)
        txtCostOfBeverages=Entry(f2aa,font=('Comic Sans MS',13,'bold'),bd=7,width=22,justify='left', textvariable=CostOfBeverages) 
        txtCostOfBeverages.grid(row=1, column=1, sticky=W)
        lblCostOfserviceCharge=Label(f2aa, font=('Comic Sans MS', 13, 'bold'), text="Service charge:", bd=8)
        lblCostOfserviceCharge.grid(row=2, column=0, sticky=W)
        txtCostOfserviceCharge=Entry(f2aa,font=('Comic Sans MS',13,'bold'), bd=6,width=22,justify='left',textvariable=ServiceCharge) 
        txtCostOfserviceCharge.grid(row=2, column=1, sticky=W)
        #===========================Payment Information===================
        lblCostOfTax = Label(f2ab, font=('Comic Sans MS', 13, 'bold'), text="Enter Tax Percentage:", bd=8)
        lblCostOfTax.grid(row=0, column=0, sticky=W)
        txtCostOfTax = Entry(f2ab, font=('Comic Sans MS', 13, 'bold'), bd=6, width=22, justify='left', textvariable=PaidTax) 
        txtCostOfTax.grid(row=0, column=1, sticky=W)
        lblCostOfSubTotal = Label(f2ab, font=('Comic Sans MS', 13, 'bold'), text="Sub Total:", bd=8)
        lblCostOfSubTotal.grid(row=1, column=0, sticky=W)
        txtCostOfSubTotal = Entry(f2ab, font=('Comic Sans MS', 13, 'bold'), bd=7, width=22, justify='left', textvariable=SubTotal) 
        txtCostOfSubTotal.grid(row=1, column=1, sticky=W)
        lblCostOfTotal = Label(f2ab, font=('Comic Sans MS', 13, 'bold'), text="Total:", bd=5)
        lblCostOfTotal.grid(row=2, column=0, sticky=W)
        txtCostOfTotal = Entry(f2ab, font=('Comic Sans MS', 13, 'bold'), bd=6, width=22, justify='left', textvariable=TotalCost) 
        txtCostOfTotal.grid(row=2, column=1, sticky=W)
        #==================== Bottom Total payment right corner down frame=======
        btnTotal = Button(fb2,padx=0,pady=5,bd=8,fg="blue",font=('forte',10,'bold'),width=14,text="TOTAL",command=CostOfItem)
        btnTotal.grid(row=0, column=0)
        btnReceipt = Button(fb2,padx=0,pady=5,bd=8,fg="blue",font=('forte',10,'bold'),width=14,text="RECEIPT",command=receipt)
        btnReceipt.grid(row=0, column=1)
        btnReset = Button(fb2,padx=0,pady=5,bd=8,fg="blue",font=('forte',10,'bold'),width=14,text="RESET",command=qReset)
        btnReset.grid(row=1, column=0)
        btnExit = Button(fb2, padx=0, pady=5, bd=8, fg="blue", font=('forte',10,'bold'),width=14,text="EXIT",command=qExit)
        btnExit.grid(row=1, column=1)
    BILL=Button(ijk,padx=2,pady=13,bd=3,fg="blue",font=('Comic Sans MS',14,'bold'),width=15,text="|| BILLING ||",command=qbill)        
    BILL.grid(row=0, column=0)
    def qtable():
        root= Tk()
        root.geometry( "1280x800+0+0" )
        root.title("TABLE AAGF")
        root.configure(background="gold")
        #----------------------total main Frame-----------------------------------------
        Tops=Frame(root,width=15,height=100,bd=25,relief="raise")
        Tops.pack(side=TOP)
        #--------------------------main left Frame--------------------------------------
        f1=Frame(root,width=300,height=1000,bd=13,relief="raise")
        f1.pack(side=LEFT)
        #--------------------------left left Frame--------------------------------------
        f2=Frame(f1,width=300,height=1000,bd=13,relief="raise")
        f2.pack(side=LEFT)
        #--------------------------left left top Frame----------------------------------
        f3=Frame(f2,width=300,height=1000,bd=13,relief="raise")
        f3.pack(side=TOP)
        #--------------------------left left bottom Frame-----------------------------
        f4=Frame(f2,width=300,height=9000,bd=13,relief="raise")
        f4.pack(side=BOTTOM)
        #-----------------------------left right Frame--------------------------
        f5=Frame(f1,width=300,height=1000,bd=13,relief="raise")
        f5.pack(side=RIGHT)
        #-------------------------------left right top Frame---------------------------
        f6=Frame(f5,width=300,height=1000,bd=13,relief="raise")
        f6.pack(side=TOP)
        #--------------------------left right bottom Frame---------------------------
        f7=Frame(f5,width=300,height=9000,bd=13,relief="raise")
        f7.pack(side=BOTTOM)
        #--------------------------main right Frame--------------------------------------
        f8=Frame(root,width=300,height=1000,bd=13,relief="raise")
        f8.pack(side=RIGHT)
        #--------------------------right left Frame--------------------------------------
        f9=Frame(f8,width=300,height=1000,bd=13,relief="raise")
        f9.pack(side=LEFT)
        #------------------------------right left top Frame----------------------------------
        f10=Frame(f9,width=300,height=1000,bd=13,relief="raise")
        f10.pack(side=TOP)
        #-------------------------------right left bottom Frame-----------------------------
        f11=Frame(f9,width=300,height=9000,bd=13,relief="raise")
        f11.pack(side=BOTTOM)
        #---------------------------------right right Frame--------------------------
        f12=Frame(f8,width=300,height=1000,bd=13,relief="raise")
        f12.pack(side=RIGHT)
        #------------------------------------right right top Frame---------------------------
        f13=Frame(f12,width=300,height=1000,bd=13,relief="raise")
        f13.pack(side=TOP)
        #----------------------------right right bottom Frame---------------------------
        f14=Frame(f12,width=300,height=9000,bd=13,relief="raise")
        f14.pack(side=BOTTOM)
        #---------------------------------frame colours----------------------------------
        Tops.configure(background='dark red')
        f1.configure(background='dark red')
        f2.configure(background='dark red')
        f3.configure(background='dark green')
        f4.configure(background='blue')
        f5.configure(background='dark red')
        f6.configure(background='dark green')
        f7.configure(background='blue')
        f8.configure(background='dark red')
        f9.configure(background='dark red')
        f10.configure(background='dark green')
        f11.configure(background='blue')
        f12.configure(background='dark red')
        f13.configure(background='dark green')
        f14.configure(background='blue')
        #--------------------------------main header name----------------------------------
        lblinfo=Label(Tops, font=('forte',75,'bold'), text="...Tables...",bd=25).grid(row=0,column=0)
        #-------------------------------main header name ends-----------------------------
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()
        var19 = IntVar()
        var20 = IntVar()
        var21 = IntVar()
        var22 = IntVar()
        var23 = IntVar()
        var24 = IntVar()
        #=================================left Foods Side================================
        a=Checkbutton(f4,text="TABLE 01\t",variable=var1,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=0,sticky=W)
        b=Checkbutton(f4,text="TABLE 02\t",variable=var2,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=1,sticky=W)
        c=Checkbutton(f4,text="TABLE 03\t",variable=var3,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=2,sticky=W)
        d=Checkbutton(f4,text="TABLE 04\t",variable=var4,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=3,sticky=W)
        e=Checkbutton(f4,text="TABLE 05\t",variable=var5,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=4,sticky=W)
        f=Checkbutton(f4,text="TABLE 06\t",variable=var6,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=5,sticky=W)
        #=================================left Foods Side================================
        g=Checkbutton(f7,text="TABLE 07\t",variable=var7,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=0,sticky=W)
        h=Checkbutton(f7,text="TABLE 08\t",variable=var8,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=1,sticky=W)
        i=Checkbutton(f7,text="TABLE 09\t",variable=var9,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=2,sticky=W)
        j=Checkbutton(f7,text="TABLE 10\t",variable=var10,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=3,sticky=W)
        k=Checkbutton(f7,text="TABLE 11\t",variable=var11,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=4,sticky=W)
        l=Checkbutton(f7,text="TABLE 12\t",variable=var12,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=5,sticky=W)
        #=================================Right Foods Side================================
        m=Checkbutton(f11,text="TABLE 13\t",variable=var13,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=0,sticky=W)
        n=Checkbutton(f11,text="TABLE 14\t",variable=var14,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=1,sticky=W)
        o=Checkbutton(f11,text="TABLE 15\t",variable=var15,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=2,sticky=W)
        p=Checkbutton(f11,text="TABLE 16\t",variable=var16,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=3,sticky=W)
        q=Checkbutton(f11,text="TABLE 17\t",variable=var17,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=4,sticky=W)
        r=Checkbutton(f11,text="TABLE 18\t",variable=var18,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=5,sticky=W)
        #=================================Right Foods Side================================
        s=Checkbutton(f14,text="TABLE 19\t",variable=var19,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=0,sticky=W)
        t=Checkbutton(f14,text="TABLE 20\t",variable=var20,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=1,sticky=W)
        u=Checkbutton(f14,text="TABLE 21\t",variable=var21,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=2,sticky=W)
        v=Checkbutton(f14,text="TABLE 22\t",variable=var22,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=3,sticky=W)
        w=Checkbutton(f14,text="TABLE 23\t",variable=var23,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=4,sticky=W)
        x=Checkbutton(f14,text="TABLE 24\t",variable=var24,onvalue=1,offvalue=0,font=('chiller',25,'bold')).grid(row=5,sticky=W)
        #==========================left Foods Side Heading===========================
        abcd=Label(f3, text="..2 PEOPLES..",font=('Bernard MT Condensed', 32, 'bold'),bd=10).grid(row=0,column=0)
        #=========================left Foods Side Heading 2==========================
        efgh=Label(f6, text="..4 PEOPLES..",font=('Bernard MT Condensed', 32, 'bold'),bd=10).grid(row=0,column=0)
        #==========================Right Foods Side Heading==========================
        ijkl=Label(f10, text="..6 PEOPLES..",font=('Bernard MT Condensed', 32, 'bold'),bd=10).grid(row=0,column=0)
        #=========================Right Foods Side Heading 2=========================
        mnop=Label(f13, text="..8 PEOPLES..",font=('Bernard MT Condensed', 32, 'bold'),bd=10).grid(row=0,column=0)
    TABLE=Button(efg, padx=2,pady=13, bd=3, fg="blue", font=('Comic Sans MS', 14, 'bold'), width=15, text="|| TABLES ||",command=qtable).grid(row=0, column=0) 
root=Tk()
object= Login_system(root)
root.mainloop()
        
    
