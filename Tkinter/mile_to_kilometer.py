import tkinter
import tkinter.messagebox

def conversion():
    a=1.60934
    try:
        ans["text"]=a*int(box.get())
    except ValueError:
        new_wind=tkinter.messagebox.showerror(message="There is no valid input",title="Error")
    return

screen=tkinter.Tk()
screen.maxsize(width=500, height=100)
screen.title("Mile to Kilometer Converter")
km=0
element_1=tkinter.Label(text="Mile to Kilometer convertor", font=("Arial",15, "bold"))
element_1.grid(row=0,column=1)

box=tkinter.Entry(width=20)
box.grid(row=1,column=0)

convert=tkinter.Button(text="convert",font=("Arial",12),command=conversion)
convert.grid(row=1,column=1)

element_mile=tkinter.Label(text="Miles", font=("arial",12))
element_mile.grid()

ans=tkinter.Label(text=km,font=("Arial",12))
ans.grid(row=1,column=2)

element_km=tkinter.Label(text="kilometers",font=("Arial",12))
element_km.grid(row=2,column=2)

screen.mainloop()



