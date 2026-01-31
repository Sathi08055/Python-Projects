import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
segment=["Work","Short Brake","Long Brake"]
timing=[WORK_MIN*60, SHORT_BREAK_MIN*60, LONG_BREAK_MIN*60]
default_time=timing.copy()
# ---------------------------- TIMER RESET ------------------------------- # 
now="25:00"
# ---------------------------- STATIC ELEMENTS ------------------------------- #
timer_id= None
window=tkinter.Tk()
window.maxsize(width=600, height=600)
window.minsize(width=600, height=600)
window.config(bg=YELLOW)
window.title("Pomodoro")
image_canvas=tkinter.Canvas(width=220,height=224,bg=YELLOW,highlightthickness=0)
tomato=tkinter.PhotoImage(file="tomato.png")
image_canvas.create_image(110,112,image=tomato)
image_canvas.place(x=200,y=185)
tim=tkinter.Label(text=now,font=(FONT_NAME,20))
tim.place(x=270,y=300)

## Timer Functions:
def timer():
    global timing, i, timer_id
    timing[i]-=1
    nows= int(timing[i])
    a= nows//60
    b=nows%60
    if(nows <0):
        next_segment()
    else:
        if (0<=nows < 60):
            time=f"{nows:02}"
        else:
            time=f"{a:02}:{b:02}"
        tim["text"]= time
        if timer_id:
            window.after_cancel(timer_id)
        timer_id=window.after(1000, timer)


def next_segment():
    global i, timing,default_time
    i+=1
    if i>2:
        i=0
        timing=default_time.copy()
    timer()
    label_1["text"]=segment[i]

def reset_timer():
    global i, timing, default_time
    i=0
    timing= default_time.copy()
    label_1["text"]=segment[i]
    timer()

### Updating Elements in our code
i=0
label_1=tkinter.Label(text=f"{segment[i]}",font=(FONT_NAME,25),bg=YELLOW)
label_1.pack(pady=30)

butt=tkinter.Button(text="Reset",font=(FONT_NAME,15),highlightthickness=0,bd=0,activebackground="#BE5985",activeforeground="#FDFAF6",command=reset_timer)
butt.place(x=120,y=420)

butt_2=tkinter.Button(text="Next",font=(FONT_NAME,15),highlightthickness=0,bd=0,activebackground="#BE5985",activeforeground="#FDFAF6",command=next_segment)
butt_2.place(x=420,y=420)

window.after(1000,timer)

window.mainloop()