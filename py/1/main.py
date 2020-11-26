from tkinter import *




class CurrencyConverter:

    
   
    def __init__(self):
        window=Tk()
        window.title("Marketing problem")
        window.configure()

        sellingPrice = Label(window,font="Arial 10",fg="dark blue",text="selling price").grid(row=1,column=1,sticky=W)
        Label(window,font="Arial 10",fg="dark blue",text="Purchase price").grid(row=2,column=1,sticky=W)
        Label(window,font="Arial 10",fg="dark blue",text="Markup").grid(row=4,column=1,sticky=W)
        Label(window,font="Arial 10",fg="dark blue",text="Percentage Markup").grid(row=5,column=1,sticky=W)
        Label(window,font="Arial 10",fg="dark blue",text="Profit Margin").grid(row=6,column=1,sticky=W)

        Entry(window,justify=RIGHT).grid(row=1,column=2)
        Entry(window,justify=RIGHT).grid(row=2,column=2)


        MyButton=Button(window,height=1,width=20,text="Compute Stuff",font="Arial 10",bg="light blue",fg="black").grid(row=3,column=2)
        
        Entry(window,state="disabled",justify=RIGHT).grid(row=4,column=2)
        Entry(window,state="disabled",justify=RIGHT).grid(row=5,column=2)
        Entry(window,state="disabled",justify=RIGHT).grid(row=6,column=2)

        window.mainloop()
        

CurrencyConverter()