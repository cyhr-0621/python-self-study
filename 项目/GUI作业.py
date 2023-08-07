import tkinter as tk
top=tk.Tk()

top.title('python GUI')

lab1=tk.Label(top,bg='white',width=20,height=2,text='请选择课程',fg='Red',bd=6,relief='ridge',font=('隶书',20))
lab1.grid(row=0,column=1)

var1 =tk.IntVar()
var2 =tk.IntVar()

def psel():
    if(var1.get()==1) and (var2.get()==0):
        lab1.config(text='选择离散')

    elif(var1.get()==1) and (var2.get()==1):
        lab1.config(text='选择离散和高数')

    elif(var1.get()==0) and (var2.get()==0):
        lab1.config(text='都不选择')
    else:
        lab1.config(text='选择高数')

c1=tk.Checkbutton(top,text='离散',width=4,height=2,bd=2,relief='ridge',variable=var1,
                  onvalue=1,
                  offvalue=0,
                  command= psel,
                  font=('Verdana',14,'bold'))
c1.grid(row=2,column=1)
c2 =tk.Checkbutton(top,text='高数',width=4,height=2,bd=2,relief='ridge',variable=var2,
                   onvalue=1,
                   offvalue=0,
                   command= psel,
                   font=('Verdana',14,'bold'))
c2.grid(row=3,column=1)
top.mainloop()

