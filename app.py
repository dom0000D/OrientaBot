from tkinter import *
from chat import bot_name, get_response

# Create object
splashScreen = Tk()
splashScreen.title("OrientaBot")
# Adjust size
splashScreen.configure(width=500, height=550)
splashScreen.eval('tk::PlaceWindow . center') #center splash screen

# Set Label
logo = PhotoImage(file="../../Desktop/TESI/logo.png") #load logo
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

TEXT_COLOR = "#EAECEE"
FONT_BOLD = "Helvetica 16 bold"
BG_GRAY = "#ABB2B9"
FONT = "Helvetica 14"
class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self.setup_main_window()

    def run(self):
        self.window.mainloop()

    def setup_main_window(self):
        self.window.title("OrientaBot")
        self.window.resizable(width=False, height=False)
        self.window.configure (bg = "#000000")
        self.window.attributes('-fullscreen', True)
        self.window.eval('tk::PlaceWindow . center')

        #head Label
        head_label = Label(self.window, bg="#000000", fg= TEXT_COLOR, text= "[∵┌]└[ ∵ ]┘[┐∵]┘ ᴏʀɪᴇɴᴛᴀʙᴏᴛ [∵┌]└[ ∵ ]┘[┐∵]┘", font="Helvetica 25", pady=20)
        head_label.place(relwidth=1)

        #text widget
        self.text_widget = Text(self.window, width=40, height=2, bg="#f7ecda", font="Helvetica 18", padx=10,pady=10)  # 40 caratteri a liena
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="trek", state=DISABLED)

        #foto del bot a destra
        self.photo = PhotoImage(file="../../Desktop/TESI/c.png")
        self.canvas = Canvas(self.window, bg="#f7ecda", highlightthickness=0, height=self.photo.height(),width=self.photo.width())
        self.canvas.place(relx=0.96, rely=0.65, anchor="ne")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=2) #relx 2 cosí é invisibile poiché fuori campo
        scrollbar.configure(command=self.text_widget.yview)

        #bottom label
        bottom_label = Label(self.window, bg="#f4e4ca", height=80)
        bottom_label.place(relwidth=1, rely=0.870)

        #message box
        self.msg_entry = Entry(bottom_label,bg="#cec3ad", fg= "#000000", font= "Helvetica 18")
        self.msg_entry.place(relwidth=0.74, relheight= 0.06, rely=0.020, relx= 0.011)
        self.msg_entry.focus() #quando starta l'app il cursore è già attivo
        self.msg_entry.bind("<Return>",self._on_enter_press)

        #send button
        button_image = PhotoImage(file="../../Desktop/TESI/v.png")
        send_button = Button(bottom_label, bg="#ffc107", fg="#000000", relief="solid",width=10, height=2, command=lambda: self._on_enter_press(None))
        send_button.config(image=button_image, compound="center")
        send_button.image = button_image
        send_button.place(relx=0.77, rely=0.020, relheight=0.06, relwidth=0.22)

    def _on_enter_press(self,event):
        msg = self.msg_entry.get()
        self._insert_msg(msg, "Tu")
    def _insert_msg(self,msg,sender):
        if not msg:
            return
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state= NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        self.text_widget.configure(state= NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()