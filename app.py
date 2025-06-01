from word_replacing import *
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("AutoDocx")
        self.geometry("300x270")
        self.configure(bg='lightblue')
        self.resizable(False, False)
        
        self.label = tk.Label(self, text="Write Name, Address, ID code and Email", bg='lightblue', font=('Arial', 10, 'bold'))
        self.label.pack(pady=10)
        
        # Creating input fields for user data.
        self.name = tk.Entry(self)
        self.name.pack(pady=10)
        
        self.address = tk.Entry(self)
        self.address.pack(pady=10)
        
        self.id_code = tk.Entry(self)
        self.id_code.pack(pady=10)
        
        self.email = tk.Entry(self)
        self.email.pack(pady=10)
        
        self.button = tk.Button(self, text="Submit", command=self.replace)
        self.button.pack(pady=10)

    def replace(self):
        replacements = {
            "{name}": self.name.get(),
            "{address}": self.address.get(),
            "{id_code}": self.id_code.get(),
            "{email}": self.email.get(),
        }
        
        process_templates(replacements)
        self.label.config(text="Done! Check the 'ready' folder.", fg='green')