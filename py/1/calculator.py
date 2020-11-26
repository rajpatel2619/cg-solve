from tkinter import *
import tkinter
root = Tk()

# setting window title 
root.title("Marketing Problem")

class CurrencyConverter:
    selling_price=tkinter.StringVar()
    purchase_price=tkinter.StringVar()
    markup=tkinter.StringVar()
    percentage_markup=tkinter.StringVar()
    profit_margin=tkinter.StringVar()

#  function for calculating the markup, percantage markup and profit
    def compute(self):
        selling_price=int(self.selling_price.get())
        purchase_price=int(self.purchase_price.get())
        # // markup calculation
        markup = "{:.2f}".format(selling_price-purchase_price)
        self.markup.set(markup)
        # // percantage markup calculation
        percentage_markup="{:.2f}".format(((selling_price-purchase_price)/purchase_price)*100)
        self.percentage_markup.set(percentage_markup)
        # // profit margin calculation
        profit_margin = "{:.2f}".format(selling_price-purchase_price)
        self.profit_margin.set(profit_margin)
        
    def __init__(self, master):
        mainframe=Frame(bg="#ffffff")
        mainframe.pack( pady=10, padx=20)

        L1 = Label(mainframe, bg="#ffffff",fg="dark blue", text="Selling Price:")
        L1.grid(row=0, column=0, pady=10)
        ES = Entry(mainframe, bd =5, textvariable = self.selling_price)
        ES.grid(row=0, column=1)

        L1 = Label(mainframe, bg="#ffffff",fg="dark blue", text="Purchase Price:")
        L1.grid(row=1, column=0, pady=10)
        EP = Entry(mainframe, bd =5, textvariable = self.purchase_price)
        EP.grid(row=1, column=1)

        B = tkinter.Button(mainframe, text = "Compute Stuff", bg='#0058e8', fg='#ffffff', command = self.compute)
        B.grid(row=2, column=0, columnspan=2, pady=10)

        L1 = Label(mainframe, bg="#ffffff",fg="dark blue", text="Markup: ")
        L1.grid(row=3, column=0, pady=10)
        EM = Entry(mainframe, state="disabled", bd =5, textvariable = self.markup)
        EM.grid(row=3, column=1)

        L1 = Label(mainframe,  bg="#ffffff",fg="dark blue", text="Percentage Markup:")
        L1.grid(row=4, column=0, pady=10, padx=10)
        EMP = Entry(mainframe, state="disabled", bd =5, textvariable = self.percentage_markup)
        EMP.grid(row=4, column=1, padx=10)

        L1 = Label(mainframe, bg="#ffffff",fg="dark blue", text="Profit Margin:")
        L1.grid(row=5, column=0, pady=10)
        EPM = Entry(mainframe, state="disabled", bd =5, textvariable = self.profit_margin)
        EPM.grid(row=5, column=1)

CurrencyConverter(root)
root.mainloop()