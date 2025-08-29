from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x300")
        self.master.title('Age Guessing Game')
        self.StartPage()

    
    def StartPage(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.page1 = Frame(self.master)
        self.page1.pack()

        self.title_text = ttk.Label(self.page1, text = 'This app can guess your age with just one question.\n', font = ('Helvetica', 18))
        self.title_text.pack()

        self.subtext = ttk.Label(self.page1, text = 'Press the next button to play.\n')
        self.subtext.pack()

        self.next_button = ttk.Button(self.page1, text = "Next", command = self.GamePage)
        self.next_button.pack()
    
    def GamePage(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.page2 = Frame(self.master)
        self.page2.pack()

        self.title_text = ttk.Label(self.page2, text = 'How old are you?\n', font = ('Helvetica', 18))
        self.title_text.pack()
        
        self.age_entry = Entry(self.page2, width = 30, font = ('Helvetica', 12))
        self.age_entry.config(bg = 'white', fg = 'black')
        self.age_entry.pack()
        self.age_entry.focus_set()

        guess_age_button = ttk.Button(self.page2, text = 'Guess Age', command = self.get_entry_text)
        guess_age_button.pack()

    def get_entry_text(self):
        age = self.age_entry.get()
        self.FinalPage(age)        

    def FinalPage(self, age):
        for i in self.master.winfo_children():
            i.destroy()

        self.page3 = Frame(self.master)
        self.page3.pack()

        if age.isdigit():
            result_text = f"You are {age} years old."
        else:
            result_text = "Invalid entry, try again."

        self.title_text = ttk.Label(self.page3, text = result_text, font = ('Helvetica', 18))
        self.title_text.pack()

        play_again_button = ttk.Button(self.page3, text = 'Play Again?', command = self.GamePage)
        play_again_button.pack(pady = 20)

if __name__ == "__main__":
    root = Tk()
    app_instance = App(root)
    root.mainloop()
