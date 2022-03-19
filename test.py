from tkinter import*
from PIL import Image, ImageTk
import pynput

flag = False
def change_img():
  global flag
  if flag:
    img2=ImageTk.PhotoImage(Image.open("cat1.jpg"))
  else:
    img2=ImageTk.PhotoImage(Image.open("cat2.jpg"))
  flag = not flag
  label.configure(image=img2)
  label.image=img2

def press(key):
  if (pynput.keyboard.Key):
    change_img()

def teste():
  print("hello")

#test = pynput.keyboard.Listener(on_press=press)
#test.start()
#test.join()

win= Tk()

win.geometry("450x400")
win.title("Bongo Cat!")

# Creating Menubar
menubar = Menu(win)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)

file.add_command(label ='New File', command = teste)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = win.destroy)
menubar.add_cascade(label ='File', menu = file)
img1= ImageTk.PhotoImage(Image.open("cat1.jpg"))

label= Label(win,image= img1)
label.pack()
# display Menu
win.config(menu = menubar)
win.attributes('-topmost', True)
win.resizable(False, False)
win.update()

with pynput.keyboard.Listener(on_press=press) as listener:
  win.mainloop()
  listener.join()
