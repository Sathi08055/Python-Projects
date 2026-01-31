import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()

# Create a frame to hold the Text widget and the scrollbar
frame = tk.Frame(window)
frame.pack(fill="both")

# Create the Text widget
text_widget = tk.Text(frame, wrap="word", width=40, height=10)
text_widget.pack(side="left", fill="both")

# Create a ttk scrollbar and link it to the Text widget
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
scrollbar.pack(side="right",fill="y")

# Configure the Text widget to work with the scrollbar
text_widget.config(yscrollcommand=scrollbar.set)

# Add some text to the Text widget
text_widget.insert("1.0", "This is some 1234567890123456789012345678901234567890 text.\n" * 20)

# Start the Tkinter event loop
window.mainloop()
