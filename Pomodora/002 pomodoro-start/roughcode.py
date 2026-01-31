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
segment = ["Work", "Short Break", "Long Break"]
timing = [WORK_MIN * 60, SHORT_BREAK_MIN * 60, LONG_BREAK_MIN * 60]
default_time = timing.copy()

# ---------------------------- TIMER RESET ------------------------------- # 
now = "25:00"

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.maxsize(width=600, height=600)
window.minsize(width=600, height=600)
window.config(bg=YELLOW)
window.title("Pomodoro")

# Tomato image setup
image_canvas = tkinter.Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")  # Ensure you have 'tomato.png' in the correct directory
image_canvas.create_image(110, 112, image=tomato)
image_canvas.place(x=200, y=185)

# Timer label setup
tim = tkinter.Label(text=now, font=(FONT_NAME, 20))
tim.place(x=270, y=300)

# Label to show current segment
i = 0
label_1 = tkinter.Label(text=f"{segment[i]}", font=(FONT_NAME, 25), bg=YELLOW)
label_1.pack(pady=30)

# Timer function
timer_id = None  # Variable to store the ID of the scheduled timer

def timer():
    global timing, i, timer_id
    timing[i] -= 1
    nows = int(timing[i])
    a = nows // 60
    b = nows % 60
    if nows < 0:
        next_segment()  # Go to the next segment when the current one finishes
    else:
        if 0 <= nows < 60:
            time = f"{nows:02}"
        else:
            time = f"{a:02}:{b:02}"
        tim["text"] = time
        
        # Cancel the previous timer if there is one and schedule the next one
        if timer_id:
            window.after_cancel(timer_id)  # Cancel the previous scheduled timer
        timer_id = window.after(1000, timer)  # Schedule the next timer call

# Function to switch to the next segment
def next_segment():
    global i, timing, default_time
    i += 1
    if i > 2:  # If we have passed the last segment, restart from "Work"
        i = 0
        timing = default_time.copy()  # Reset to the default time for each segment
    label_1["text"] = segment[i]
    timer()  # Restart the timer for the next segment

# Reset function to reset the timer
def reset_timer():
    global i, timing, default_time, timer_id
    i = 0  # Reset to the "Work" segment
    timing = default_time.copy()  # Reset to the default timings
    label_1["text"] = segment[i]  # Update the segment label
    tim["text"] = f"{WORK_MIN:02}:00"  # Reset the timer display to "25:00"
    
    # Cancel the previous timer and restart it
    if timer_id:
        window.after_cancel(timer_id)
    timer()  # Start the timer again

# Buttons setup
butt = tkinter.Button(text="Reset", font=(FONT_NAME, 15), highlightthickness=0, bd=0,
                      activebackground="#BE5985", activeforeground="#FDFAF6", command=reset_timer)
butt.place(x=120, y=420)

butt_2 = tkinter.Button(text="Next", font=(FONT_NAME, 15), highlightthickness=0, bd=0,
                        activebackground="#BE5985", activeforeground="#FDFAF6", command=next_segment)
butt_2.place(x=420, y=420)

# Start the timer
timer_id = window.after(1000, timer)  # Start the initial timer

window.mainloop()
