from Tkinter import *

def changeMsg():
    label.configure(text="I will self destruct in 2 secs")
    label.after(2000, root.destroy)

root = Tk()
mainContainer = Frame(root)
label = Label(mainContainer, text="")
label.configure(text="msg will change in 3 secs")
label.pack(side=LEFT, ipadx=5, ipady=5)
mainContainer.pack()
label.after(3000, changeMsg)
root.title("Timed event")
root.mainloop()
