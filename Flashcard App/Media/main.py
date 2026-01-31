import pandas as pd
import tkinter as tk
import random 
from PIL import Image, ImageTk
from tkinter import ttk

data=pd.read_csv(r"data\dict.csv")
back_clr="#91C2AF"
# Window:
window=tk.Tk()
window.title("Flashcard")
bg_clr="#b1ddc6"
window.config(bg=bg_clr)
window.geometry("790x690")
window.resizable(0,0)
# functions
def parse( data= data):
    tot=42051
    id=random.randint(0,tot-1)
    content=[data.loc[id]["word"].title(),data.loc[id]["definition"]]
    return content
content=parse()


#UI


## UI Elements:

### Images:

resized_img=Image.open(r"images\right.png")
right_img=ImageTk.PhotoImage(resized_img)
resized_img=Image.open(r"images\wrong.png")
wrong_img=ImageTk.PhotoImage(resized_img)

back_img=tk.PhotoImage(file=r"images\card_back.png")


# Classes:

class Front():
    def __init__(self,vocab=None, meaning=None):
        if (vocab==None) or (meaning==None):
             self.content=parse()
             vocab=self.content[0]
             meaning=self.content[1]
        for widget in window.winfo_children():
            widget.destroy()
        self.vocab=vocab
        self.meaning=meaning
        self.card=tk.Canvas(width=800, height=526,bg=bg_clr,bd=0,highlightthickness=0)
        self.front_img=tk.PhotoImage(file=r"images\card_front.png")
        self.card.create_image(400,263,image=self.front_img)
        self.card.pack()
        self.card.create_text(400,125,text="What is the meaning of ",font=("Bahnschrift",25,"bold"))
        self.vocabulary=self.card.create_text(400,250,text=self.vocab,font=("Bahnschrift",25,"bold"),fill="blue")
        self.count_lab=self.card.create_text(50,50,text=str(3),font=("Arial",24,"bold"),fill="red")
        window.after(1000,self.countdown,3)
        
    def countdown(self,count):
            count=count-1
            self.card.itemconfig(self.count_lab,text=str(count))
            if (count>0):
                window.after(1000,self.countdown,count)
            else:
                Back(meaning=self.meaning,vocab=self.vocab)
            return

class Back():
    def __init__(self,meaning,vocab):
        for widget in window.winfo_children():
               widget.destroy()
        self.mean=meaning
        self.card = tk.Canvas(window, width=800, height=526,bg=bg_clr,bd=0,highlightthickness=0)
        # Use the back image that was loaded earlier
        self.card.create_image(400,263, image=back_img)
        self.card.place(x=0,y=0)
        self.vocab=vocab
        vocab_label=tk.Label(bg=back_clr,text=vocab,font=("Bahnschrift",22,"bold"),fg="blue")
        vocab_label.place(x=400,y=50,anchor="center")
        frame=tk.Frame(window,width=750,height=360,highlightthickness=0,bd=0,bg=back_clr)
        frame.pack_propagate(0)
        frame.place(x=15,y=100)
        self.mean_lab=tk.Text(frame, wrap= "word",bg="white",highlightthickness=0,bd=0,padx=10, fg="black",font=("Bahnschrift",18),spacing2=10)
        self.scrollbar = tk.Scrollbar(frame, command=self.mean_lab.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y",padx=0)
        self.mean_lab.config(yscrollcommand=self.scrollbar.set)
        self.mean_lab.pack(fill="both")
        self.mean_lab.insert("end",meaning)
        self.mean_lab.config(state="disabled")
        self.wrong_butt=tk.Button(image=wrong_img, command=self.again,bd=0,highlightthickness=0)
        self.right_butt=tk.Button(image=right_img, command=self.next,bd=0,highlightthickness=0)
        self.wrong_butt.place(x=100,y=600,anchor="center")
        self.right_butt.place(x=690,y=600,anchor="center")
    def next(self):
         Front()
    def again(self):
         Front(vocab=self.vocab, meaning=self.mean)

Front()

#-------------------->This
window.mainloop()