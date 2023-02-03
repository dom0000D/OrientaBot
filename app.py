from tkinter import *
#from chat import bot_name
"""""
# Create object
splash = Tk()
splash.title("OrientaBot")
# Adjust size
splash.geometry("600x600")
splash.eval('tk::PlaceWindow . center')

# Set Label
img = PhotoImage(file= "../../Desktop/TESI/Icona bianca.png")
splash_label = Label(splash, font=18, image=img)
splash_label.pack()


# main window function


def main():
    # destroy splash window
    splash.destroy()

    # Execute tkinter
    root = Tk()

    # Adjust size
    root.geometry("400x400")


# Set Interval
splash.after(4000, main)

# Execute tkinter
mainloop()
"""""
BG_COLOR = "#17202A"
class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self.setup_main_window()

    def run(self):
        self.window.mainloop()

    def setup_main_window(self):
        self.window.title("OrientaBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=500, height=550, bg = BG_COLOR)
        self.window.eval('tk::PlaceWindow . center')

if __name__ == "__main__":
    app = ChatApplication()
    app.run()