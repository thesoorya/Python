from tkinter import *

# window - the container contains all widgets
# widgets - GUI elements

window = Tk()
window.geometry('200x200') #height and width of the window

# icon = PhotoImage(file='logo.jpg')
# window.iconphoto(icon) #used to change the logo of the window

window.title('GUI Project')

# window.config(background='black')

########## LABLE

lable = Label(text='Hello Python',
              font=('Arial',20, 'bold'),
              padx=20,
              pady=10,
              fg='red',
              bg='black',
              bd='10',
              relief='raised'
              )
lable.pack()

window.mainloop() #place window on computer and listen for events