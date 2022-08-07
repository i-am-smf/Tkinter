#importing modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#initialize main window 
root=Tk()
root.title("Loading screen")
root.geometry("600x400")

#creating class for loading screen
class loading:

    #initialize the class variables
    def __init__(self):
        self.loadingscreen=Tk()
        self.loadingscreen.geometry("500x70")
        self.loadingscreen.eval('tk::PlaceWindow . center')
        self.loadingscreen.configure(bg='grey')
        self.loadingscreen.withdraw()

        self.label1=Label(self.loadingscreen,text="Downloading",bg="grey")
        self.label1.place(anchor="center", relx = .5, rely = .2)

        self.my_progress=ttk.Progressbar(self.loadingscreen,orient=HORIZONTAL,length=480,mode="determinate")
        self.my_progress.place(anchor="center",relx=.5,rely=.5)

    #create function for update loading progress
    def download(self):
        self.loadingscreen.deiconify()

        #check progress bar values to close the window
        if self.my_progress["value"]==100.0:
            self.loadingscreen.destroy()
            loadscrmsgbx=messagebox.showinfo("Completed","Download Completed")

        else:
            self.label1.config(text=f"Downloading...{int(self.my_progress['value'])}%")
            self.my_progress["value"]+=10
            self.loadingscreen.after(500,self.download)

#create a temperory function to assign class and functions
def load():
    pass
    l=loading()
    l.download()

button1=Button(root,text="start download",font=("arial",24),bg="red",fg="white",command=load)
button1.pack(pady=20)

root.mainloop()
