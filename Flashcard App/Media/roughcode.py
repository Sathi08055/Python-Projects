import pandas as pd
import tkinter as tk
import random
from PIL import Image, ImageTk

# Constants
BG_COLOR = "#b1ddc6"
BACK_COLOR = "#91C2AF"
WINDOW_WIDTH = 790
WINDOW_HEIGHT = 690
CARD_WIDTH = 800
CARD_HEIGHT = 526
FONT_TITLE = ("Bahnschrift", 25, "bold")
FONT_TEXT = ("Bahnschrift", 18)
FONT_COUNT = ("Arial", 24, "bold")
TOTAL_WORDS = 42051

# Load data
data = pd.read_csv(r"data\dict.csv")

# Placeholder for images
right_img = None
wrong_img = None
front_img = None
back_img = None

# Functions
def parse(data=data):
    id = random.randint(0, TOTAL_WORDS - 1)
    return [data.loc[id]["word"].title(), data.loc[id]["definition"]]

# Classes
class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard")
        self.root.config(bg=BG_COLOR)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(0, 0)
        global right_img, wrong_img, front_img, back_img
        right_img = ImageTk.PhotoImage(Image.open(r"images\right.png"))
        wrong_img = ImageTk.PhotoImage(Image.open(r"images\wrong.png"))
        front_img = tk.PhotoImage(file=r"images\card_front.png")
        back_img = tk.PhotoImage(file=r"images\card_back.png")
        self.content = parse()
        self.front_view()

    def front_view(self, vocab=None, meaning=None):
        self.clear_window()
        if vocab is None or meaning is None:
            self.content = parse()
            vocab, meaning = self.content

        self.vocab = vocab
        self.meaning = meaning

        self.card = tk.Canvas(self.root, width=CARD_WIDTH, height=CARD_HEIGHT, bg=BG_COLOR, bd=0, highlightthickness=0)
        self.card.create_image(CARD_WIDTH // 2, CARD_HEIGHT // 2, image=front_img)
        self.card.create_text(CARD_WIDTH // 2, 125, text="What is the meaning of", font=FONT_TITLE)
        self.card.create_text(CARD_WIDTH // 2, 250, text=self.vocab, font=FONT_TITLE, fill="blue")
        self.count_label = self.card.create_text(50, 50, text="3", font=FONT_COUNT, fill="red")
        self.card.pack()
        self.countdown(3)

    def back_view(self):
        self.clear_window()

        self.card = tk.Canvas(self.root, width=CARD_WIDTH, height=CARD_HEIGHT, bg=BG_COLOR, bd=0, highlightthickness=0)
        self.card.create_image(CARD_WIDTH // 2, CARD_HEIGHT // 2, image=back_img)
        self.card.pack()

        vocab_label = tk.Label(self.root, bg=BACK_COLOR, text=self.vocab, font=("Bahnschrift", 22, "bold"), fg="blue")
        vocab_label.place(x=CARD_WIDTH // 2, y=50, anchor="center")

        frame = tk.Frame(self.root, width=750, height=360, bg=BACK_COLOR)
        frame.pack_propagate(0)
        frame.place(x=15, y=100)

        text_box = tk.Text(frame, wrap="word", bg="white", font=FONT_TEXT, spacing2=10, padx=10)
        text_box.insert("end", self.meaning)
        text_box.config(state="disabled")
        text_box.pack(fill="both")

        scrollbar = tk.Scrollbar(frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        text_box.config(yscrollcommand=scrollbar.set)

        tk.Button(self.root, image=wrong_img, command=self.again, bd=0, highlightthickness=0).place(x=100, y=600, anchor="center")
        tk.Button(self.root, image=right_img, command=self.next_card, bd=0, highlightthickness=0).place(x=690, y=600, anchor="center")

    def countdown(self, count):
        if count > 0:
            self.card.itemconfig(self.count_label, text=str(count))
            self.root.after(1000, self.countdown, count - 1)
        else:
            self.back_view()

    def next_card(self):
        self.front_view()

    def again(self):
        self.front_view(vocab=self.vocab, meaning=self.meaning)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main
if __name__ == "__main__":
    window = tk.Tk()
    app = FlashcardApp(window)
    window.mainloop()