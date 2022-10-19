from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

petasco = Tk()

petasco.title('KFC ONLINE FOOD ORDERING')
petasco.geometry('1300x700')
petasco.config(bg='#F0F8FF')
introlbl = Label(petasco, text='WELCOME TO PETASCO KFC', font=('algeria', 28, 'bold'), bg='blue', fg='gold', width=55)
introlbl.place(x=15, y=1)

# --------------------------------------------------- customer info label -----------------------------------------------------------
Label(petasco,
      text='================================= Customer Info =================================',
      font=('Arial', 15, 'bold'), bg='#F0F8FF').place(x=160, y=60)

customerlbl = Label(petasco, text='Customer Name:', font=('times', 13, 'bold'), bg='#F0F8FF')
customerlbl.place(x=15, y=90)

customerName_var = StringVar()
customer_entry = Entry(petasco, textvariable=customerName_var, font=('times', 13, 'bold'), bd=2)
customer_entry.focus()
customer_entry.place(x=145, y=90)

customerPhone = Label(petasco, text='Phone No:', font=('times', 13, 'bold'), bg='#F0F8FF')
customerPhone.place(x=350, y=90)
customerPhone_var = StringVar()
phone_entry = Entry(petasco, textvariable=customerPhone_var, font=('times', 13, 'bold'), bd=2)
phone_entry.place(x=430, y=90)

billNo_lbl = Label(petasco, text='Bill No:', font=('Arial', 13, 'bold'), bg='#F0F8FF')
billNo_lbl.place(x=630, y=90)
customerBill_var = StringVar()
bill_entry = Entry(petasco, textvariable=customerBill_var, font=('times', 13, 'bold'), bd=2)
bill_entry.place(x=690, y=90)

customerAddress = Label(petasco, text='Customer Address: ', font=('Arial', 13, 'bold'), bg='#F0F8FF')
customerAddress.place(x=890, y=90)
customerAddress_var = StringVar()
customerAddress_en = Entry(petasco, textvariable=customerAddress_var, font=('times', 13, 'bold'), bd=2)
customerAddress_en.place(x=1050, y=90)
# ----------------------------------------------Food  Menu ---------------------------------------------------------------------------


Fmenu_lbl = Label(petasco, text='============FOOD MENU============', font=('times', 14, 'bold'), bg='#F0F8FF')
Fmenu_lbl.place(y=120, x=15)
# ------------------------------ Items label -------------------------------
items = Label(petasco, text='ITEM', font=('times', 13, 'bold'), bg='#F0F8FF')
items.place(y=150, x=20)
# ====================================================================================
chicken_lbl = Label(petasco, text='Chicken', font=('times', 13, 'bold'), bg='#F0F8FF')
chicken_lbl.place(x=20, y=180)

imagechicken = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\chicken.jpg'))
chickenpic_lbl = Label(petasco, image=imagechicken)
chickenpic_lbl.place(x=110, y=180)

chicken_price = Label(text='$5.0', font=('times', 13, 'bold'), bg='#F0F8FF')
chicken_price.place(y=180, x=180)

chickenVar = IntVar()
chicken_qty = Entry(petasco, textvariable=chickenVar, font=('times', 13, 'bold'), bd=2, width=7)
chicken_qty.place(y=180, x=300)
# chicken = int(chicken_qty.get())


# =========================================================================================

# ====================================================================================

pizza_lbl = Label(petasco, text='Pizza', font=('times', 13, 'bold'), bg='#F0F8FF')
pizza_lbl.place(x=20, y=220)
image = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\Pizzaa.jpg'))
pizzapic_lbl = Label(petasco, image=image)
pizzapic_lbl.place(x=110, y=220, height=35)
pizzapic_lbl['compound'] = tk.RIGHT

pizza_price = Label(text='$10.0', font=('times', 13, 'bold'), bg='#F0F8FF')
pizza_price.place(y=220, x=180)

pizzaVar = IntVar()
pizza_qty = Entry(petasco, textvariable=pizzaVar, font=('times', 13, 'bold'), bd=2, width=7)
pizza_qty.place(y=220, x=300)

# =========================================================================================
friesvar = DoubleVar()
fries_lbl = Label(petasco, text='Fries', font=('times', 13, 'bold'), bg='#F0F8FF')
fries_lbl.place(x=20, y=260)

imagefries = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\fries.jpg'))
friespic_lbl = Label(petasco, image=imagefries)
friespic_lbl.place(x=110, y=260)

fries_price = Label(text='$2.0', font=('times', 13, 'bold'), bg='#F0F8FF')
fries_price.place(y=260, x=180)

fries_qty = Entry(petasco, textvariable=friesvar, font=('times', 13, 'bold'), bd=2, width=7)
fries_qty.place(y=260, x=300)

# =========================================================================================

# ====================================================================================
ice_lbl = Label(petasco, text='Ice Cream', font=('times', 13, 'bold'), bg='#F0F8FF')
ice_lbl.place(x=20, y=300)

imageice = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\icecream.jpg'))
icepic_lbl = Label(petasco, image=imageice)
icepic_lbl.place(x=110, y=300)

ice_price = Label(text='$3.5', font=('times', 13, 'bold'), bg='#F0F8FF')
ice_price.place(y=300, x=180)
icevar = DoubleVar()
ice_qty = Entry(petasco, textvariable=icevar, font=('times', 13, 'bold'), bd=2, width=7)
ice_qty.place(y=300, x=300)

# ice_sum = 3 * int(ice_qty)
# =========================================================================================

# ====================================================================================
cheese_lbl = Label(petasco, text='Cheese', font=('times', 13, 'bold'), bg='#F0F8FF')
cheese_lbl.place(x=20, y=340)

imagecheese = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\cheese.jpg'))
cheesepic_lbl = Label(petasco, image=imagecheese)
cheesepic_lbl.place(x=110, y=340)

cheese_price = Label(text='$5.0', font=('times', 13, 'bold'), bg='#F0F8FF')
cheese_price.place(y=340, x=180)
cheesevar = DoubleVar()
cheese_qty = Entry(petasco, textvariable=cheesevar, font=('times', 13, 'bold'), bd=2, width=7)
cheese_qty.place(y=340, x=300)

# cheese_sum = 5 * int(cheese_qty)
# =========================================================================================

# ====================================================================================
sand_lbl = Label(petasco, text='Gob3', font=('times', 13, 'bold'), bg='#F0F8FF')
sand_lbl.place(x=20, y=380)

pic = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\gob33.jpg'))
pic_lbl = Label(petasco, image=pic)
pic_lbl.place(x=110, y=380)

sand_price = Label(text='$2.5', font=('times', 13, 'bold'), bg='#F0F8FF')
sand_price.place(y=380, x=180)
sandvar = DoubleVar()
sand_qty = Entry(petasco, textvariable=sandvar, font=('times', 13, 'bold'), bd=2, width=7)
sand_qty.place(y=380, x=300)

# sand_sum = 2.5 * int(sand_qty)
# =========================================================================================

# ====================================================================================
fufu_lbl = Label(petasco, text='Waakye', font=('times', 13, 'bold'), bg='#F0F8FF')
fufu_lbl.place(x=20, y=420)

imagewaakye = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\waakye.jpg'))
waakyepic_lbl = Label(petasco, image=imagewaakye)
waakyepic_lbl.place(x=110, y=420)

fufu_price = Label(text='$1.5', font=('times', 13, 'bold'), bg='#F0F8FF')
fufu_price.place(y=420, x=180)
futuvar = DoubleVar()
fufu_qty = Entry(petasco, textvariable=futuvar, font=('times', 13, 'bold'), bd=2, width=7)
fufu_qty.place(y=420, x=300)

# fufu_sum = 1 * int(fufu_qty)
# =========================================================================================


# ------------------------------ price label -------------------------------
price = Label(petasco, text='Price', font=('times', 13, 'bold'), bg='#F0F8FF')
price.place(y=150, x=180)

# ------------------------------ qauntity label -------------------------------
qty = Label(petasco, text='Qauntity', font=('times', 13, 'bold'), bg='#F0F8FF')
qty.place(y=150, x=300)

# ---------------------------------- Drinks Menu -------------------------------------------
Fmenu_lbl = Label(petasco, text='============DRINKS MENU============', font=('times', 14, 'bold'), bg='#F0F8FF')
Fmenu_lbl.place(y=120, x=450)

# ------------------------------ Items label -------------------------------
items = Label(petasco, text='ITEM', font=('times', 13, 'bold'), bg='#F0F8FF')
items.place(y=150, x=450)

# ------------------------------ price label -------------------------------
price = Label(petasco, text='Price', font=('times', 13, 'bold'), bg='#F0F8FF')
price.place(y=150, x=620)

# ------------------------------ qauntity label -------------------------------
qty = Label(petasco, text='Qauntity', font=('times', 13, 'bold'), bg='#F0F8FF')
qty.place(y=150, x=750)

# ====================================================================================
coke_lbl = Label(petasco, text='Coke', font=('times', 13, 'bold'), bg='#F0F8FF')
coke_lbl.place(x=450, y=190)

imagecoke = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\coke.jpg'))
cokepic_lbl = Label(petasco, image=imagecoke)
cokepic_lbl.place(x=570, y=190)

coke_price = Label(text='Ghs 10', font=('times', 13, 'bold'), bg='#F0F8FF')
coke_price.place(y=190, x=620)
cokevar = IntVar()
coke_qty = Entry(petasco, textvariable=cokevar, font=('times', 13, 'bold'), bd=2, width=7)
coke_qty.place(y=190, x=750)
coke = 10 * cokevar.get()
# =========================================================================================

# ========================================================================================
pepsi_lbl = Label(petasco, text='Pepsi', font=('times', 13, 'bold'), bg='#F0F8FF')
pepsi_lbl.place(x=450, y=230)

imagepepsi = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\pepsi1.jpg'))
pepsipic_lbl = Label(petasco, image=imagepepsi)
pepsipic_lbl.place(x=570, y=230)

pepsi_price = Label(text='Ghs 10', font=('times', 13, 'bold'), bg='#F0F8FF')
pepsi_price.place(y=230, x=620)
pepsivar = IntVar()
pepsi_qty = Entry(petasco, textvariable=pepsivar, font=('times', 13, 'bold'), bd=2, width=7)
pepsi_qty.place(y=230, x=750)
pepsi = 10 * pepsivar.get()
# =========================================================================================

# ========================================================================================
cola_lbl = Label(petasco, text='Coka Cola', font=('times', 13, 'bold'), bg='#F0F8FF')
cola_lbl.place(x=450, y=270)

imagecola = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\cola1.jpg'))
colapic_lbl = Label(petasco, image=imagecola)
colapic_lbl.place(x=570, y=265)

cola_price = Label(text='Ghs 15', font=('times', 13, 'bold'), bg='#F0F8FF')
cola_price.place(y=270, x=620)
colavar = IntVar()
cola_qty = Entry(petasco, textvariable=colavar, font=('times', 13, 'bold'), bd=2, width=7)
cola_qty.place(y=270, x=750)
cola = 15 * colavar.get()
# =========================================================================================

# ========================================================================================
dew_lbl = Label(petasco, text='Dew', font=('times', 13, 'bold'), bg='#F0F8FF')
dew_lbl.place(x=450, y=300)

imagedew = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\dew1.jpg'))
dewpic_lbl = Label(petasco, image=imagedew)
dewpic_lbl.place(x=570, y=300)

dew_price = Label(text='Ghs 25', font=('times', 13, 'bold'), bg='#F0F8FF')
dew_price.place(y=300, x=620)
dewvar = IntVar()
dew_qty = Entry(petasco, textvariable=dewvar, font=('times', 13, 'bold'), bd=2, width=7)
dew_qty.place(y=300, x=750)
dew = 25 * dewvar.get()
# =========================================================================================

# =========================================================================================
cocktail_lbl = Label(petasco, text='Cocktail', font=('times', 13, 'bold'), bg='#F0F8FF')
cocktail_lbl.place(x=450, y=340)

cock_image = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Forex\cock.jpg'))
cock_pic_lbl = Label(petasco, image=cock_image)
cock_pic_lbl.place(x=565, y=340)
cock_price = Label(text='Ghs 20', font=('times', 13, 'bold'), bg='#F0F8FF').place(y=340, x=620)
cockvar = IntVar()
cock_qty = Entry(petasco, textvariable=cockvar, font=('times', 13, 'bold'), bd=2, width=7).place(y=340, x=750)
cock = 20 * cockvar.get()
# =========================================================================================

# =========================================================================================
orange_lbl = Label(petasco, text='Organge Juice', font=('times', 13, 'bold'), bg='#F0F8FF').place(x=450, y=380)

image_organge = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Forex\ORANGE.png'))
organe_piclbl = Label(petasco, image=image_organge)
organe_piclbl.place(y=380, x=565)
organge_price = Label(petasco, text='Ghs 15', font=("times", 13, 'bold'), bg="#F0F8FF").place(y=380, x=620)
orangevar = IntVar()
orange_qty = Entry(petasco, textvariable=orangevar, font=('times', 13, 'bold'), bd=2, width=7).place(y=380, x=750)
orange = 15 * orangevar.get()
# =========================================================================================

# =========================================================================================
beet_lbl = Label(petasco, text='Beet Juice', font=('times', 13, 'bold'), bg='#F0F8FF').place(x=450, y=420)
beet_image = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Forex\beet.png'))
beet_pic_lbl = Label(petasco, image=beet_image)
beet_pic_lbl.place(y=420, x=565)
beet_price = Label(petasco, text='Ghs 12', font=('times', 13, 'bold'), bg='#F0F8FF').place(y=420, x=620)
beetvar = IntVar()
beet_Qty = Entry(petasco, textvariable=beetvar, font=('times', 13, 'bold'), bd=2, width=7).place(y=420, x=750)
beet = 12 * beetvar.get()
# =========================================================================================

# =================================== payment ============================================

payment = Entry(petasco, font=('times', 15, 'bold'), bd=2, width=35, bg='blue')
payment.place(x=450, y=570, height=6)

payment_lbl = Label(petasco, text='Make Payment', font=('times', 15, 'bold'), bg='#F0F8FF')
payment_lbl.place(x=565, y=560)

mtn_info = Label(petasco, text='Enter Your MoMo Number and Allow Cashout', font=('times', 8, 'bold'), fg='blue',
                 bg='#F0F8FF')
mtn_info.place(x=400, y=590)
# ==================================== Check box =======================================
checkbtnvar = IntVar()
mtn_checkbtn = Checkbutton(petasco, variable=checkbtnvar, onvalue=1, offvalue=0, bg='#F0F8FF').place(x=370, y=612)
Mtn_Method = Label(petasco, text='MTN', font=('times', 15, 'bold'), bg='#F0F8FF')
Mtn_Method.place(x=400, y=608)
momo_var = IntVar()
Momo_no = Entry(petasco, textvariable=momo_var, font=('times', 13, 'bold'), bd=2)
Momo_no.place(x=450, y=610)

voda_info = Label(petasco, text='Till No Below', font=('times', 8, 'bold'), fg='blue', bg='#F0F8FF')
voda_info.place(x=710, y=590)

Voda_Method = Label(petasco, text='VodaCash 48862', font=('times', 15, 'bold'), bg='#F0F8FF')
Voda_Method.place(x=710, y=608)

Checkbutton(petasco, variable=checkbtnvar, onvalue=0, offvalue=1, bg='#F0F8FF').place(x=680, y=612)

checkbtn = checkbtnvar.get()  # this assigns the value to the connected checkbox


# ======================================== Drinks Total ===================================

def drinkmenu():
    global drinkTotal
    drinkTotal = ((cokevar.get() * 10) + (pepsivar.get() * 10) + (colavar.get() * 15) + (dewvar.get() * 25) + (
            cockvar.get() * 20) + (orangevar.get() * 15) + (beetvar.get() * 12)) / 10
    drklbl.config(text='Total $ ' + str(drinkTotal))


drink_total = DoubleVar()
drinktotal = Button(petasco, text='Total', command=drinkmenu, font=('times', 15, 'bold'), bd=5, width=10)
drinktotal.place(x=480, y=480)

drklbl = Label(petasco, font=('times', 15, 'bold'), bg='#F0F8FF')
drklbl.place(x=650, y=480)
drinkmenu()

# ---------------------------------- Invoice  -------------------------------------------
Fmenu_lbl = Label(petasco, text='============INVOICE============', font=('times', 14, 'bold'), bg='#F0F8FF')
Fmenu_lbl.place(y=120, x=890)

bar = Scrollbar(petasco, orient='vertical')
bar.pack(side=RIGHT, fill='y')

invoice_txtarea = Text(petasco, font=('times', 13, 'bold'), bd=2, width=40, yscrollcommand=bar.set)
invoice_txtarea.place(y=150, x=890, height=470)


# --------------------------------------------------- Total Button ----------------------------------------
def Total():
    global total
    total = (chickenVar.get() * 5) + (pizzaVar.get() * 10) + (friesvar.get() * 2) + (icevar.get() * 3.5) + (
            cheesevar.get() * 5) + (sandvar.get() * 2.5) + (futuvar.get() * 1.5)
    totaloutput.config(text='Total $' + str(total))
    return total


food_total = DoubleVar()
btn = Button(petasco, text='Total', command=Total, font=('times', 15, 'bold'), bd=5, width=10)
btn.place(x=50, y=480)

totaloutput = Label(petasco, font=('times', 15, 'bold'), bg='#F0F8FF')
totaloutput.place(x=230, y=490)
Total()


def gross():
    global grossTotal
    grossTotal = float(total) + float(drinkTotal)
    grosslbl.config(text='Your Bill Is: $ ' + str(grossTotal), bg='#F0F8FF')


gross_total = DoubleVar()
grossbtn = Button(petasco, text='Gross Total', command=gross, font=('times', 15, 'bold'), bd=5, width=10)
grossbtn.place(x=50, y=580)

grosslbl = Label(petasco, font=('times', 15, 'bold'), bg='#F0F8FF')
grosslbl.place(x=230, y=580)


def confirmPayment():
    if checkbtnvar.get() == 1:
        if Momo_no.get() == '0':
            messagebox.showerror('Payment Info', 'Please Enter Your MTN Number!')
    elif checkbtnvar.get() == 0:
        messagebox.askquestion('Payment Info', 'Have you made payment to the Till Number?')
    else:
        messagebox.showwarning('Payment Info', 'Please Select a Payment')


# ================================================ Invoice Print Out =========================================================

def receipt():
    invoice_txtarea.delete(1.0, END)

    if gross_total.get() == 0:
        messagebox.showerror('Error', 'Please Make an Order to get a Receipt')
    else:

        # ==================================== customer info ============================
        invoice_txtarea.insert(END, "===========Customer Details============\n")
        invoice_txtarea.insert(END, 'Customer Name: 'f'{customerName_var.get()}\n')
        invoice_txtarea.insert(END, 'Phone Number: 'f'{customerPhone_var.get()}\n')
        invoice_txtarea.insert(END, 'Bill Number: 'f'{customerBill_var.get()}\n')
        invoice_txtarea.insert(END, 'Customer Address: 'f'{customerAddress_var.get()}\n\n')

        # ==================================== order info ==============================
        invoice_txtarea.insert(END, '=========== Food Order Details =========\n')
        invoice_txtarea.insert(END, 'Item\t\tPrice\tQty\tTotal\n')
        invoice_txtarea.insert(END, 'Chicken\t\t $5.0 \t 'f'{chickenVar.get()}\t  $ 'f'{chickenVar.get() * 5}\n')
        invoice_txtarea.insert(END, 'Pizza\t\t $10.0 \t 'f'{pizzaVar.get()}\t  $ 'f'{pizzaVar.get() * 10}\n')
        invoice_txtarea.insert(END, 'Fries\t\t $2.0 \t 'f'{friesvar.get()}\t  $ 'f'{friesvar.get() * 2}\n')
        invoice_txtarea.insert(END, 'Ice Cream\t\t $5.0 \t 'f'{icevar.get()}\t  $ 'f'{icevar.get() * 5}\n')
        invoice_txtarea.insert(END, 'Cheese\t\t $5.0 \t 'f'{cheesevar.get()}\t  $ 'f'{cheesevar.get() * 5}\n')
        invoice_txtarea.insert(END, 'Gob3\t\t $2.5 \t 'f'{sandvar.get()}\t  $ 'f'{sandvar.get() * 2.5}\n')
        invoice_txtarea.insert(END, 'Waakye\t\t $1.5 \t 'f'{futuvar.get()}\t  $ 'f'{futuvar.get() * 1.5}\n\n')
        # ================================ Total =========================================
        invoice_txtarea.insert(END, '=====Total:\t\t  'f'{total}\t\t  ======\n\n')

        invoice_txtarea.insert(END, '========== Drinks Order Details =========\n\n')
        invoice_txtarea.insert(END, 'Item\t\tPrice\tQty\tTotal\n')
        invoice_txtarea.insert(END, 'Coke\t\t Ghs10 \t 'f'{cokevar.get()}\t  Ghs 'f'{cokevar.get() * 10}\n')
        invoice_txtarea.insert(END, 'Pepsi\t\t Ghs10 \t 'f'{pepsivar.get()}\t  Ghs 'f'{pepsivar.get() * 10}\n')
        invoice_txtarea.insert(END, 'Coka Cola\t\t Ghs15 \t 'f'{colavar.get()}\t  Ghs 'f'{colavar.get() * 15}\n')
        invoice_txtarea.insert(END, 'Dew\t\t Ghs25 \t 'f'{dewvar.get()}\t  Ghs 'f'{dewvar.get() * 25}\n')
        invoice_txtarea.insert(END, 'Cocktail\t\t Ghs20 \t 'f'{cockvar.get()}\t  Ghs 'f'{cockvar.get() * 20}\n')
        invoice_txtarea.insert(END, 'Orange Juice\t\t Ghs15 \t 'f'{orangevar.get()}\t  Ghs 'f'{orangevar.get() * 15}\n')
        invoice_txtarea.insert(END, 'Beet Juice\t\t Ghs12 \t 'f'{beetvar.get()}\t  Ghs 'f'{beetvar.get() * 12}\n\n')
        # ============================================ Total =============================
        invoice_txtarea.insert(END, '=====Total:\t\t  'f'{drinkTotal}\t\t  ======\n\n')
        invoice_txtarea.insert(END,
                               '------------------------------------------------------------\nGross Total:\t\t  'f'{grossTotal}\t\t  \n------------------------------------------------------------\n\n')

        # ====================================== payment =================================
        invoice_txtarea.insert(END, '============ Payment Details ===========\n\n')
        if checkbtnvar.get() == 0:
            invoice_txtarea.insert(END, 'Payment Method : Voda Cash')
        elif checkbtnvar.get() == 1:
            if Momo_no.get() == '0':
                messagebox.showerror('Payment Info', 'Please Enter Your MTN Number!')
            else:
                invoice_txtarea.insert(END, f'Payment Method : MTN {Momo_no.get()}')
        else:
            messagebox.showinfo('Payment Info', 'Please select your mode of Payment')
    # ================================ Disabled Text Area =============================
    invoice_txtarea.config(state='disabled')


payment_info = Label(petasco,
                     text='Payment Info:===================================================================================',
                     font='12', fg='red', bg='#F0F8FF')
payment_info.place(x=20, y=540)
confirmQ = Label(petasco, text='Made Payment?', font=('Arial', 12, 'bold'), fg='red', bg='#F0F8FF')
confirmQ.place(x=495, y=640)
confirmbtn = Button(petasco, text='Confirm', font=('times', 15, 'bold'), bd=5, width=7, bg='red',
                    command=confirmPayment)
confirmbtn.place(x=640, y=640, height=35)

print_btn = Button(petasco, command=receipt, text='Print', font=('times', 15, 'bold'), bd=5, width=7)
print_btn.place(x=920, y=628)

save_btn = Button(petasco, text='Save', font=('times', 15, 'bold'), bd=5, width=7)
save_btn.place(x=1100, y=628)

bar.config(command=invoice_txtarea.yview)
petasco.resizable(False, False)
petasco.mainloop()
