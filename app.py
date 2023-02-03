from tkinter import *
#from chat import bot_name

# Create object
splashScreen = Tk()
splashScreen.title("OrientaBot")
# Adjust size
splashScreen.configure(width=500, height=550)
splashScreen.eval('tk::PlaceWindow . center') #center splash screen

# Set Label
logo = PhotoImage(file="../../Desktop/TESI/Icona bianca.png") #load logo
splash_label = Label(splashScreen, font=18, image=logo)
splashScreen.resizable(width=False, height=False)

splash_label.pack()

# main window function
def main():
    # destroy splashScreen window
    splashScreen.destroy()
# Time of splash screen
splashScreen.after(2500, main)
# Execute tkinter
mainloop()

BG_COLOR = "#063970" #color background
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