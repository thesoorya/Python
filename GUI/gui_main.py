from tkinter import *

# window - the container contains all widgets
# widgets - GUI elements

window = Tk()
window.geometry('400x400') #height and width of the window

# icon = PhotoImage(file='file.name')
# window.iconphoto(icon) #used to change the logo of the window

window.config(background='black')

window.mainloop() #place window on computer and listen for events