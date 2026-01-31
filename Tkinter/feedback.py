import tkinter

def box_generator():
    boxes=[]
    for n in range(4):
        position_y=45*n+110
        box=tkinter.Entry(width=20)
        box.place(x=380,y=position_y)
        boxes.append(box)
    return boxes


def print_details():
    save=""
    for n in range(4):
        output=boxes[n].get()
        save=save+f"\n{output}"
    print(save)


screen=tkinter.Tk()
screen.minsize(width=600,height=600)
screen.title("Feedback form")


boxes=box_generator()


save=tkinter.Button(text="Save",font=("Arial",10),command=print_details)
save.place(x=300,y=550)


questions="What is your name\n\nWhat is your gender\n\nAgree to terms\n\nSelect intrest from list\n"
side=tkinter.Label(text=questions,font=(("Arial",15,"bold")))
side.place(x=50,y=100)


screen.mainloop()
