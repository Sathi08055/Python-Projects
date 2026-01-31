from tkinter import *
import requests

def get_quote():
    def data_return():
        url = "https://quotes15.p.rapidapi.com/quotes/random/?language_code=en"
        headers = {
            "x-rapidapi-host": "quotes15.p.rapidapi.com",
            "x-rapidapi-key": "73be45d676msh012c8e258cc48adp188179jsn852832fbfbb1"
        }
        response = requests.get(url, headers=headers)
        data=response.json()
        return data
    data=data_return()
    try:
        author=data["originator"]["name"]
        quote=data["content"]
    except KeyError:
            data_return()
            author=data["originator"]["name"]
            quote=data["content"]
            # Dynamically adjust font size based on length
    if len(quote) > 125:
        font_size = 15
    elif len(quote) > 50:
        font_size = 20
    elif len(quote) > 145:
        print("Overload")
        get_quote()
    else:
        font_size = 30

    canvas.itemconfig(quote_text,text=quote,font=("Arial",font_size,"bold"))
    new_canvas.itemconfig(author_quote, text=f"-{author}")
    return


window = Tk()
window.title("Random Quote Generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Random Quote Here, Press Kanye To Get more", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)
new_canvas=Canvas(width=300,height=50)
author_quote=new_canvas.create_text(150,25,text="Author",fill="black",font=("Arial",20,"italic"))
new_canvas.grid(row=1, column=0,sticky="ne")
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,borderwidth=0,)
kanye_button.grid(row=2, column=0,sticky="s")
window.mainloop()