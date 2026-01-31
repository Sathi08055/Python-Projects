import tkinter,pyperclip, json
import random
import tkinter.messagebox

class pass_vault:
    def __init__(self,username,website,password):
        self.username=username
        self.website=website
        self.password=password
        pass
    def __str__(self):
        a= f"Username or Website-{self.username}\nWebsite-{self.website}\nPassword-{self.password}\n"
        return a
    def cred_list(self):
        cred_list=[self.username,self.website,self.password]
        return cred_list
    def save_format(self):
        b=f'\n"{self.username}","{self.website}","{self.password}"'
        return b
    def json_save(self):
        json_save={
            self.website:{
                "password":self.password,
                "username":self.username,}}
        return json_save

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!@#$%^&*()_-+=<>?/")
    password=(random.choices(letters,k=4)+(random.choices(numbers,k=4)))+(random.choices(symbols,k=4))
    random.shuffle(password)
    pass_inp.delete(0,tkinter.END)
    pass_inp.insert(0,("".join(password)))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def update():
    pass_word=pass_inp.get()
    web_site=web_inp.get()
    user_name=user_inp.get()
    new_det=pass_vault(password=pass_word,username=user_name,website=web_site)
    conf=tkinter.messagebox.askyesno(title="Confirmation box",message="Do you want to save this password?")
    if conf:
        try:
            with open ("passwords.json","r") as file:
                pass_data=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass_data = {}
        finally:
            pass_data.update(new_det.json_save())
            with open ("passwords.json","w") as file:
                json.dump(pass_data,file,indent=4)
        tkinter.messagebox.showinfo(title="Saved info",message="Succesful")
        pyperclip.copy(new_det.password)
    web_inp.delete(0,tkinter.END)
    user_inp.delete(0,tkinter.END)
    pass_inp.delete(0,tkinter.END)
    return

# ---------------------------- UI SETUP ------------------------------- #
padding = {"padx": 20, "pady": 20}
FONT=("Arial Rounded MT Bold",12)
window=tkinter.Tk()
#window.geometry("600x600")
#window.resizable(0,0)
window.title("Password Manager")
logo=tkinter.PhotoImage(file="logo.png")
logo_canvas=tkinter.Canvas(width=200,height=200)
logo_canvas.create_image(100,100, image= logo)
logo_canvas.grid(row=0, column=0,pady=20,columnspan=3)
web_lab=tkinter.Label(text="   Website:",font=FONT)
web_inp=tkinter.Entry(width=35)
web_lab.grid(row=1, column=0, **padding, sticky="e" )
web_inp.grid(row=1,column=1,columnspan=2,**padding,sticky="w")
user_lab=tkinter.Label(text=" Username or email:",font=FONT)
user_lab.grid(row=2,column=0,**padding,sticky="e")
user_inp=tkinter.Entry(width=35)
user_inp.grid(row=2, column=1,**padding,sticky="w")
pass_lab=tkinter.Label(text="Password:",font=FONT) #password label

pass_inp=tkinter.Entry(width=30) #-----------------------------------------Password Entry Box
pass_lab.grid(row=3, column=0,**padding,sticky="e")
pass_inp.grid(row=3,column=1,columnspan=2,**padding,sticky="w")
gen_button=tkinter.Button(text="Generate",font=FONT) #-------------------------------Password Gen Button
gen_button.grid(row=3,column=2,sticky="w",**padding)
gen_button.config(command=pass_gen)

save_button=tkinter.Button(text="Save",font=FONT)
save_button.grid(row=4,column=0,**padding,columnspan=3)
save_button.config(command=update)

window.mainloop()