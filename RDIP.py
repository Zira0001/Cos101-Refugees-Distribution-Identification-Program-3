 for d, k in zip(d, k):

        if code in m:
            root = tkinter.Tk()
            l1 = ttk.Label(text='already entered', style="BW.TLabel", font='bobo 100', background="red")
            l1.pack()
            root.maxsize(1000, 300)
            root.minsize(1000, 300)
            root.mainloop()

            break

        if code in d:
            root = tkinter.Tk()
            l1 = ttk.Label(text=k, style="BW.TLabel", font='bobo 70', background="green")
            l1.pack()

            root.maxsize(1000, 100)
            root.minsize(1000, 100)
            root.mainloop()
            break

    for k, d in zip(k, d):
        if code in m:
            root = tkinter.Tk()
            l1 = ttk.Label(text='already entered', style="BW.TLabel", font='bobo 70', background="red")
            l1.pack()
            root.maxsize(1000, 100)
            root.minsize(1000, 100)
            root.mainloop()

            break
        if code not in d:
            root = tkinter.Tk()
            l1 = ttk.Label(text='Not in existence', style="BW.TLabel", font='bobo 100', background="red")
            l1.pack()
            root.maxsize(1000, 200)
            root.minsize(1000, 200)
            root.mainloop()
            break
    m.append(code)


while True:
    chocks()