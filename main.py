from tkinter import *

root = Tk()
root.title("Chatbot")

BG_GRAY="#FF5F1F"
BG_COLOR = "#F88158"
TEXT_COLOR="#033E3E"
TITLE_COLOR="#FF5F1F"

FONT="Helvetica 14"
FONT_BOLD="Helvetica 13 bold"

def send():
    send = "You ->"+uInput.get()
    txt.insert(END,"\n"+send)

    user=uInput.get().lower()

    if(user=="hello"):
        txt.insert(END,"\n"+"Bot -> Hi there, how can I help?")

    elif(user=="hi" or user == "hii" or user =="hiii"):
        txt.insert(END,"\n"+"Bot -> Hi there, what can I do for you")

    elif(user=="how are you"):
        txt.insert(END,"\n"+"Bot -> fine! and you")

    elif(user=="fine" or user=="i am good" or user=="i am doing good"):
        txt.insert(END,"\n"+"Bot -> Great how can i help you.")

    elif(user=="thanks" or user=="thank you" or user=="now its my time"):
        txt.insert(END,"\n"+"Bot -> My Pleasure")

    elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
        txt.insert(END, "\n" + "Bot -> We have coffee and tea")

    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert(
            END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")

    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")


        uInput.delete(0,END)

label1=Label(root,bg=TITLE_COLOR,fg=TEXT_COLOR,text="Welcome",font=FONT_BOLD,pady=10,width=20,height=1).grid(row=0)
txt = Text(root,bg=BG_COLOR,fg=TEXT_COLOR,font=FONT,width=60)
txt.grid(row=1,column=0,columnspan=2)

scrollbar=Scrollbar(txt)
scrollbar.place(relheight=1,relx=0.974)

uInput=Entry(root,bg="#AAF0D1",fg=TEXT_COLOR,font=FONT,width=55)
uInput.grid(row=2,column=0)

send=Button(root,text="Send",font=FONT_BOLD, bg=BG_GRAY,command=send).grid(row=2,column=1)

root.mainloop()


