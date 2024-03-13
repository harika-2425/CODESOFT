import tkinter
class MyGui:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame1=tkinter.Frame(self.main_window)
        self.top_frame2=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        self.prompt_label1 = tkinter.Label(self.top_frame1,text='Num1:')

        self.kilo_entry1 = tkinter.Entry(self.top_frame1,width=10)

        self.prompt_label1.pack(side='left')

        self.kilo_entry1.pack(side='left')
        self.prompt_label2=tkinter.Label(self.top_frame2,text="Num2:")
        self.kilo_entry2=tkinter.Entry(self.top_frame2,width=10)
        self.prompt_label2.pack(side='left')
        self.kilo_entry2.pack(side='right')
       
        self.descr_label = tkinter.Label(self.bottom_frame,text='Result:')
        self.value = tkinter.StringVar()
        self.result_label=tkinter.Label(self.bottom_frame,textvariable=self.value)
        self.descr_label.pack(side='left')
        self.result_label.pack(side='left')
        self.add_button=tkinter.Button(self.mid_frame,text='add',command=self.adding)
        self.sub_button=tkinter.Button(self.mid_frame,text='sub',command=self.subtracting)
        self.mul_button=tkinter.Button(self.mid_frame,text='mul',command=self.multiplying)
        self.div_button=tkinter.Button(self.mid_frame,text='div',command=self.dividing)
        self.quit_button = tkinter.Button(self.mid_frame,text='Quit',command=self.main_window.destroy)
        self.add_button.pack(side='left')
        self.sub_button.pack(side='left')
        self.mul_button.pack(side='left')
        self.div_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame1.pack()
        self.top_frame2.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def adding(self):
        number1=float(self.kilo_entry1.get())
        number2=float(self.kilo_entry2.get())
        sum1=number1+number2
        self.value.set(sum1)
    def subtracting(self):
        number1=float(self.kilo_entry1.get())
        number2=float(self.kilo_entry2.get())
        sub=number1-number2
        self.value.set(sub)
    def multiplying(self):
        number1=float(self.kilo_entry1.get())
        number2=float(self.kilo_entry2.get())
        mul=number1*number2
        self.value.set(mul)
    def dividing(self):
        number1=float(self.kilo_entry1.get())
        number2=float(self.kilo_entry2.get())
        div=number1/number2
        self.value.set(div)
mygui=MyGui()
