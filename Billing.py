from tkinter import *
import random
import tkinter.messagebox as tmsg
import os
class Bill_App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1400x800")
        self.root.title("Billing Software")
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE,
                      font="comicsansms 20 bold", pady=2, bg="lime").pack(fill=X)

        # =========== Variables================
        #===== Cosmetics======
        self.soap_var = IntVar()
        self.cream_var = IntVar()
        self.face_var = IntVar()
        self.spary_var = IntVar()
        #===== Grocery =============
        self.rice_var = IntVar()
        self.daal_var = IntVar()
        self.sugar_var = IntVar()
        self.tea_var = IntVar()
        #===== Cold Drinnks=====
        self.maza_var = IntVar()
        self.cola_var = IntVar()
        self.sprite_var = IntVar()
        self.froot_var = IntVar()
        #===== Total=========
        self.total_cos_var = StringVar()
        self.total_gos_var = StringVar()
        self.total_drink_var = StringVar()
        #======== Tax=========
        self.costax_var = StringVar()
        self.grostax_var = StringVar()
        self.drinktax_var = StringVar()
        #============ Customer===========
        self.name_var = StringVar()
        self.phon_var = StringVar()
        self.billno_var = StringVar()
        x = random.randint(100,999)
        self.billno_var.set(str(x))
        self.search_bill = StringVar()
        f1 = LabelFrame(self.root, text="Customer Details",
                        font="comicsansms 15 bold",fg='red', bg='skyblue', bd=8, relief=SUNKEN)
        f1.place(x=0, y=80, relwidth=1)

        cust_name = Label(f1, text="Customer Name",bg='skyblue', font="comicsansms 18 bold").grid(
            row=0, column=0, padx=20, pady=5)
        cust_entry = Entry(f1, width=12,textvariable=self.name_var, font="arial 18 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=12, pady=5)

        cust_name = Label(f1, text="Phone",bg='skyblue', font="comicsansms 18 bold").grid(
            row=0, column=2, padx=20, pady=5)
        cust_entry = Entry(f1, width=12,textvariable=self.phon_var, font="arial 18 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=12, pady=5)

        bill = Label(f1, text="Bill No",bg='skyblue', font="comicsansms 18 bold").grid(
            row=0, column=4, padx=20, pady=5)
        bill = Entry(f1, width=12, textvariable=self.billno_var,font="arial 18 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=5, padx=12, pady=5)

        search = Entry(f1, width=12, textvariable=self.search_bill,font="arial 18 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=6, padx=12, pady=5)
        Button(f1, text='Search',bg='skyblue', font="comicsansms 18 bold", bd=7,
               relief=GROOVE,command=self.find_bill).grid(row=0, column=7, padx=12, pady=5)

        # =============== Cosmetic=======================
        f2 = LabelFrame(self.root, text="Cosmetics",
                        font="comicsansms 15 bold", fg='red',bg='skyblue', bd=8, relief=SUNKEN)
        f2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(f2, text="Bath Soap", bg='skyblue',font="comicsansms 16 bold").grid(
            row=0, column=0, padx=20, pady=3, sticky='w')
        bath_entry = Entry(f2, width=8, textvariable=self.soap_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=0, column=1, padx=12, pady=5)

        face_cream_lbl = Label(f2, text="Face Cream",bg='skyblue', font="comicsansms 16 bold").grid(
            row=1, column=0, padx=20, pady=3, sticky='w')
        face_cream_entry = Entry(f2, width=8,textvariable=self.cream_var, font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=1, column=1, padx=12, pady=5)

        face_w_lbl = Label(f2, text="Face Wash", bg='skyblue',font="comicsansms 16 bold").grid(
            row=2, column=0, padx=20, pady=3, sticky='w')
        face_wentry = Entry(f2, width=8, textvariable=self.face_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=2, column=1, padx=12, pady=5)

        hair_s_lbl = Label(f2, text="Hair Spray",bg='skyblue', font="comicsansms 16 bold").grid(
            row=3, column=0, padx=20, pady=3, sticky='w')
        hair_s_entry = Entry(f2, width=8, textvariable=self.spary_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=3, column=1, padx=12, pady=5)

        f3 = LabelFrame(self.root, text="Grocery",
                        font="comicsansms 15 bold", fg='red',bg='skyblue', bd=8, relief=SUNKEN)
        f3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(f3, text="Rice", bg='skyblue',font="comicsansms 16 bold").grid(
            row=0, column=0, padx=20, pady=3, sticky='w')
        rice_entry = Entry(f3, width=8, textvariable=self.rice_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=0, column=1, padx=12, pady=5)

        daal_cream_lbl = Label(f3, text="Daal", bg='skyblue',font="comicsansms 16 bold").grid(
            row=1, column=0, padx=20, pady=3, sticky='w')
        daal_cream_entry = Entry(f3, width=8, textvariable=self.daal_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=1, column=1, padx=12, pady=5)

        sugar_lbl = Label(f3, text="Sugar", bg='skyblue',font="comicsansms 16 bold").grid(
            row=2, column=0, padx=20, pady=3, sticky='w')
        sugar_wentry = Entry(f3, width=8, textvariable=self.sugar_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=2, column=1, padx=12, pady=5)

        tea_lbl = Label(f3, text="Tea",bg='skyblue', font="comicsansms 16 bold").grid(
            row=3, column=0, padx=20, pady=3, sticky='w')
        tea_entry = Entry(f3, width=8,textvariable=self.tea_var, font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=3, column=1, padx=12, pady=5)

        f4 = LabelFrame(self.root, text="Cold Drinks",
                        font="comicsansms 15 bold", fg='red',bg='skyblue', bd=8, relief=SUNKEN)
        f4.place(x=670, y=180, width=325, height=380)

        maza_lbl = Label(f4, text="Maza", bg='skyblue',font="comicsansms 16 bold").grid(
            row=0, column=0, padx=20, pady=3, sticky='w')
        maza_entry = Entry(f4, width=8,textvariable=self.maza_var, font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=0, column=1, padx=12, pady=5)

        coc_cream_lbl = Label(f4, text="Coca Cola", bg='skyblue',font="comicsansms 16 bold").grid(
            row=1, column=0, padx=20, pady=3, sticky='w')
        coc_cream_entry = Entry(f4, width=8, textvariable=self.cola_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=1, column=1, padx=12, pady=5)

        sprite_lbl = Label(f4, text="Sprite", bg='skyblue',font="comicsansms 16 bold").grid(
            row=2, column=0, padx=20, pady=3, sticky='w')
        sprite_wentry = Entry(f4, width=8, textvariable=self.sprite_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=2, column=1, padx=12, pady=5)

        frooti_lbl = Label(f4, text="Frooti", bg='skyblue',font="comicsansms 16 bold").grid(
            row=3, column=0, padx=20, pady=3, sticky='w')
        frooti_entry = Entry(f4, width=8, textvariable=self.froot_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=3, column=1, padx=12, pady=5)

        # =====Bill area====
        f5 = Frame(self.root, bd=8, relief=SUNKEN)
        f5.place(x=1000, y=180, width=385, height=380)
        bill_title = Label(
            f5, text="Bill Area", bg='skyblue',font="arial 17 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5, font="ChalkboardSE 10 bold",
                             yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        f6 = LabelFrame(self.root, text="Bill Menue",
                        font="comicsansms 15 bold", fg='red',bg='skyblue', bd=8, relief=SUNKEN)
        f6.place(x=0, y=560, relwidth=1, height=180)
        total_cosmetic_lbl = Label(f6, text="Total Cosmetics Price", bg='skyblue',font="comicsansms 16 bold").grid(
            row=0, column=0, padx=20, pady=3, sticky='w')
        total_cosmetic_entry = Entry(f6, width=12,textvariable=self.total_cos_var, font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=0, column=1, padx=12, pady=3)

        total_grocery_lbl = Label(f6, text="Total Grocery Price", bg='skyblue',font="comicsansms 16 bold").grid(
            row=1, column=0, padx=20, pady=3, sticky='w')
        coc_cream_entry = Entry(f6, width=12, textvariable=self.total_gos_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=1, column=1, padx=12, pady=3)

        total_drinks_lbl = Label(f6, text="Total Cold Drinks Price",bg='skyblue', font="comicsansms 16 bold").grid(
            row=2, column=0, padx=20, pady=3, sticky='w')
        total_drinks_wentry = Entry(f6, width=12, textvariable=self.total_drink_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=2, column=1, padx=12, pady=3)

        # ====== Tax======
        cosmetic_tax_lbl = Label(f6, text="Cosmetics Tax",bg='skyblue', font="comicsansms 16 bold").grid(
            row=0, column=2, padx=20, pady=3)
        cosmetic_tax_entry = Entry(f6, width=12, textvariable=self.costax_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=0, column=3, padx=12, pady=3)

        grocery_tax_lbl = Label(f6, text="Grocery Tax",bg='skyblue', font="comicsansms 16 bold").grid(
            row=1, column=2, padx=20, pady=3)
        grocery_tax_entry = Entry(f6, width=12, textvariable=self.grostax_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=1, column=3, padx=12, pady=3)

        drinks_tax_lbl = Label(f6, text="Cold Drinks Tax", bg='skyblue',font="comicsansms 16 bold").grid(
            row=2, column=2, padx=20, pady=3)
        drinks_tax_entry = Entry(f6, width=12, textvariable=self.drinktax_var,font="arial 13 bold", bd=5, relief=SUNKEN).grid(
            row=2, column=3, padx=12, pady=3)

        Button(f6, text="Total", font="comicsansms 18 bold", bd=7,
               relief=GROOVE,command=self.Total).grid(row=0, column=4, padx=10)
        Button(f6, text="Genereate Bill", font="comicsansms 18 bold", bd=7,
               relief=GROOVE,command=self.Bill).grid(row=0, column=5, padx=10)
        Button(f6, text="Clear", font="comicsansms 18 bold", bd=7,
               relief=GROOVE,command=self.clear).grid(row=0, column=6, padx=10)
        Button(f6, text="Exit", font="comicsansms 18 bold", bd=7,
               relief=GROOVE, command=exit).grid(row=0, column=7, padx=10)
        self.Welcome()
    def Welcome(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t*** Welcome Webcode Retail ***")
        self.textarea.insert(END,f"\nBill Number :{self.billno_var.get()}")
        self.textarea.insert(END,f"\nCustomer Name :{self.name_var.get()} ")
        self.textarea.insert(END,f"\nPhone :{self.phon_var.get()}")
        self.textarea.insert(END,"\n===========================================")
        self.textarea.insert(END,"\tProducts \t\t\tQTY \t\tPrice")
        self.textarea.insert(END,"\n===========================================")


    def Total(self):
        self.Welcome()
        # For Cosmetics
        self.soap_price = self.soap_var.get()*40
        self.cream_price = self.cream_var.get()*100
        self.face_price = self.face_var.get()*200
        self.spray_price = self.spary_var.get()*50
        self.total_cosmetic_price = float(
                                        (self.soap_price)+
                                        (self.cream_price)+
                                        (self.face_price)+
                                        (self.spray_price)
                                    )
        self.total_cos_var.set("Rs: "+str(self.total_cosmetic_price))
        self.c_tax = self.total_cosmetic_price*0.05
        self.costax_var.set("Rs: "+str(self.c_tax))
        # For Grocery
        self.rice_price = self.rice_var.get()*140
        self.daal_price = self.daal_var.get()*120
        self.sugar_price = self.sugar_var.get()*180
        self.tea_price = self.tea_var.get()*50        
        self.total_grocery_price = float(
                                        (self.rice_price)+
                                        (self.daal_price)+
                                        (self.sugar_price)+
                                        (self.tea_price)
                                    )
        self.total_gos_var.set("Rs: "+str(self.total_grocery_price))
        self.g_tax = self.total_grocery_price*0.1
        self.grostax_var.set("Rs: "+str(self.g_tax))
        # For cold drinks
        self.maza_price = self.maza_var.get()*50
        self.cola_price = self.cola_var.get()*40
        self.sprite_price = self.sprite_var.get()*40
        self.froot_price = self.froot_var.get()*10
        self.total_drinks_price = float(
                                        (self.maza_price)+
                                        (self.cola_price)+
                                        (self.sprite_price)+
                                        (self.froot_price)
                                    )
        self.total_drink_var.set("Rs: "+str(self.total_drinks_price))
        self.d_tax = self.total_drinks_price*0.1
        self.drinktax_var.set("Rs: "+str(self.d_tax))

        self.total_bill = (self.total_cosmetic_price+self.total_grocery_price+self.total_drinks_price)+(self.c_tax+self.g_tax+self.d_tax)
    def Bill(self):
        if self.name_var.get()=="" or self.phon_var.get()=="":
            tmsg.showinfo(message="Please Enter Customer Details First")
        else:
            # Cosmetics
            if self.soap_var.get()!=0:
                self.textarea.insert(END,f"\nSoap \t\t\t{self.soap_var.get()} \t\t{self.soap_price}")
            if self.cream_var.get()!=0:
                self.textarea.insert(END,f"\nFace Wash \t\t\t{self.cream_var.get()} \t\t{self.cream_price}")
            if self.face_var.get()!=0:
                self.textarea.insert(END,f"\nCream \t\t\t{self.face_var.get()} \t\t{self.face_price}")
            if self.spary_var.get()!=0:
                self.textarea.insert(END,f"\nSpray \t\t\t{self.spary_var.get()} \t\t{self.spray_price}")
            # Grocery
            if self.rice_var.get()!=0:
                self.textarea.insert(END,f"\nRice \t\t\t{self.rice_var.get()} \t\t{self.rice_price}")
            if self.daal_var.get()!=0:
                self.textarea.insert(END,f"\nDaal \t\t\t{self.daal_var.get()} \t\t{self.daal_price}")
            if self.sugar_var.get()!=0:
                self.textarea.insert(END,f"\nSugar \t\t\t{self.sugar_var.get()} \t\t{self.sugar_price}")
            if self.tea_var.get()!=0:
                self.textarea.insert(END,f"\nTea \t\t\t{self.tea_var.get()} \t\t{self.tea_price}")
            # Cold Drinks
            if self.cola_var.get()!=0:
                self.textarea.insert(END,f"\nCoca Cola \t\t\t{self.cola_var.get()} \t\t{self.cola_price}")
            if self.sprite_var.get()!=0:
                self.textarea.insert(END,f"\nSprite \t\t\t{self.sprite_var.get()} \t\t{self.sprite_price}")
            if self.maza_var.get()!=0:
                self.textarea.insert(END,f"\nMaza \t\t\t{self.maza_var.get()} \t\t{self.maza_price}")
            if self.froot_var.get()!=0:
                self.textarea.insert(END,f"\nFrootie \t\t\t{self.froot_var.get()} \t\t{self.froot_price}")

            self.textarea.insert(END,"\n---------------------------------------------------------------------------------------")
            if self.costax_var.get()!='0.0':
                self.textarea.insert(END,f"\nCosmetic Tax : \t\t\t \t\t{self.costax_var.get()}")
            if self.costax_var.get()!='0.0':
                self.textarea.insert(END,f"\nGrocery Tax : \t\t\t \t\t{self.grostax_var.get()}")
            if self.costax_var.get()!='0.0':
                self.textarea.insert(END,f"\nCold Drinks Tax : \t\t\t \t\t{self.drinktax_var.get()}")
            self.textarea.insert(END,"\n---------------------------------------------------------------------------------------")
            self.textarea.insert(END,f"\nTotal : {self.total_bill}")

            self.save_data()
    def clear(self):
        self.textarea.delete('1.0',END)
        self.Welcome()
    def save_data(self):
        op = tmsg.askyesno(title="save",message="Do You want to Save??")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1 = open(self.billno_var.get()+".txt",'w')
            f1.write(self.bill_data)
            f1.close()
        else:
            return
    def find_bill(self):
        found = False
        for i in os.listdir('F:\Tkinter'):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(i,'r')
                self.textarea.delete('1.0',END)
                for data in f1:
                    self.textarea.insert(END,data)
                f1.close()
                found = True
        if found == False:
            tmsg.showerror("error",message=f"There is no records matches to this bill no- {self.search_bill.get()}")
            
if __name__ == '__main__':
    root = Tk()
    b = Bill_App(root)
    root.mainloop()
    