from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    box_hr.config(text=hr)
    box_min.config(text=min)
    box_sec.config(text=sec)
    box_am.config(text=am)
    box_date.config(text=date)
    box_month.config(text=month)
    box_year.config(text=year)
    box_day.config(text=day)

    #for continue change
    box_hr.after(200,date_time)

clock=Tk()

clock.title('Digital Clock')
clock.geometry('500x300')
clock.config(bg='#ccc')

#time
box_hr=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg="#000",fg="#fff")
box_hr.place(x=20,y=10,height=100,width=100)
box_min=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg="#000",fg="#fff")
box_min.place(x=140,y=10,height=100,width=100)
box_sec=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg="#000",fg="#fff")
box_sec.place(x=260,y=10,height=100,width=100)
box_am=Label(clock,text="00",font=('Time New Roman',45,"bold"),bg="#000",fg="#fff")
box_am.place(x=380,y=10,height=100,width=100)

#timetext
box_hrtxt=Label(clock,text="Hour",font=('Cameric',10,"bold"),bg="#36454f",fg="#fff")
box_hrtxt.place(x=35,y=115,height=20,width=70)
box_mintxt=Label(clock,text="Min",font=('Cameric',10,"bold"),bg="#36454f",fg="#fff")
box_mintxt.place(x=155,y=115,height=20,width=70)
box_sectxt=Label(clock,text="Sec",font=('Cameric',10,"bold"),bg="#36454f",fg="#fff")
box_sectxt.place(x=275,y=115,height=20,width=70)
box_amtxt=Label(clock,text="AM/PM",font=('Cameric',10,"bold"),bg="#36454f",fg="#fff")
box_amtxt.place(x=395,y=115,height=20,width=70)

#date
box_date=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg="#000",fg="#fff")
box_date.place(x=20,y=165,height=100,width=100)
box_month=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg="#000",fg="#fff")
box_month.place(x=140,y=165,height=100,width=100)
box_year=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg="#000",fg="#fff")
box_year.place(x=260,y=165,height=100,width=100)
box_day=Label(clock,text="00",font=('Time New Roman',35,"bold"),bg="#000",fg="#fff")
box_day.place(x=380,y=165,height=100,width=100)

#datetext
box_datwtxt=Label(clock,text="Date",font=('Arial',10,"bold"),bg="#36454f",fg="#fff")
box_datwtxt.place(x=35,y=270,height=20,width=70)
box_monthtxt=Label(clock,text="Month",font=('Arial',10,"bold"),bg="#36454f",fg="#fff")
box_monthtxt.place(x=155,y=270,height=20,width=70)
box_yeartxt=Label(clock,text="Year",font=('Arial',10,"bold"),bg="#36454f",fg="#fff")
box_yeartxt.place(x=275,y=270,height=20,width=70)
box_daytxt=Label(clock,text="Day",font=('Arial',10,"bold"),bg="#36454f",fg="#fff")
box_daytxt.place(x=395,y=270,height=20,width=70)

date_time()

clock.mainloop()