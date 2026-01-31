import tkinter
window= tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)
my_label= tkinter.Label(text="Dont touch me!", font=("Arial",30,"bold")) #creating a text object
my_label.pack() #allign into the window
def butt_clicked():
    my_label["text"]=inp.get()
    print(inp.get())
    return
butt=tkinter.Button(text="Click Me",command=butt_clicked)
butt.pack()
inp= tkinter.Entry()
inp.pack()
window.mainloop()