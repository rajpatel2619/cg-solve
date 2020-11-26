from tkinter import *
import tkinter

def compute():
    sp=int(sell_price.get())
    pp=int(purchase_price.get())
    mp = sp-pp
    markup.set(mp)
    pm=((sp-pp)/pp)*100
    percentage_markup.set(pm)
    pmar = sp-pp
    profit_margin.set(pmar)

root = Tk()
root.title("Marketing Problem")

sell_price=tkinter.StringVar()
purchase_price=tkinter.StringVar()
markup=tkinter.StringVar()
percentage_markup=tkinter.StringVar()
profit_margin=tkinter.StringVar()

mainframe=Frame(bg="#ffffff")
mainframe.pack( pady=10, padx=20)

L1 = Label(mainframe, bg="#ffffff", text="Selling Price:")
L1.grid(row=0, column=0, pady=10)
ES = Entry(mainframe, bd =5, textvariable = sell_price)
ES.grid(row=0, column=1)

L1 = Label(mainframe, bg="#ffffff", text="Purchase Price:")
L1.grid(row=1, column=0, pady=10)
EP = Entry(mainframe, bd =5, textvariable = purchase_price)
EP.grid(row=1, column=1)

B = tkinter.Button(mainframe, text = "Compute Stuff", bg='#0058e8', fg='#ffffff', command = compute)
B.grid(row=2, column=0, columnspan=2, pady=10)

L1 = Label(mainframe, bg="#ffffff", text="Markup: ")
L1.grid(row=3, column=0, pady=10)
EM = Entry(mainframe, bd =5, textvariable = markup)
EM.grid(row=3, column=1)

L1 = Label(mainframe, bg="#ffffff", text="Percentage Markup:")
L1.grid(row=4, column=0, pady=10, padx=10)
EMP = Entry(mainframe, bd =5, textvariable = percentage_markup)
EMP.grid(row=4, column=1, padx=10)

L1 = Label(mainframe, bg="#ffffff", text="Profit Margin:")
L1.grid(row=5, column=0, pady=10)
EPM = Entry(mainframe, bd =5, textvariable = profit_margin)
EPM.grid(row=5, column=1)

root.mainloop()