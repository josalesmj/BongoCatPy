from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import pynput
import threading

class CatWindow:
  flagBlock = False
  flag = False
  flagWindowResizable = True
  flagWindowAlwaysOnTop = False

  def __init__(self):

    self.win = Tk()
    self.win.geometry("450x400")
    self.win.title("Bongo Cat!")
    self.menubar = Menu(self.win)
    self.file = Menu(self.menubar, tearoff=0)
    self.file.add_command(
        label='Resize:' + str(self.flagWindowResizable), command=self.setWindowResizable)
    self.file.add_command(label='Always on Top:' +
                          str(self.flagWindowAlwaysOnTop), command=self.setWindowOnTop)
    self.file.add_separator()
    self.file.add_command(label='Exit', command=self.on_closing)

    self.menubar.add_cascade(label='File', menu=self.file)
    img1 = ImageTk.PhotoImage(Image.open("cat1.jpg"))

    self.label = Label(self.win, image=img1)
    self.label.pack()

    self.win.config(menu=self.menubar)
    self.win.resizable(self.flagWindowResizable, self.flagWindowResizable)
    self.win.attributes('-topmost', self.flagWindowAlwaysOnTop)
    self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.win.update()
    self.myListener = pynput.keyboard.Listener(
        on_press=self.on_press, on_release=self.on_release)
    self.myListener.start()
    self.myTimer = self.newTimer()
    self.win.mainloop()
    self.myListener.join()

  def on_closing(self):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.myListener.stop()
        self.myTimer.cancel()
        self.win.destroy()

  def newTimer(self):
    return threading.Timer(0.5, self.change_img, [True])

  def change_img(self, test=False):
    if(test):
      img2 = ImageTk.PhotoImage(Image.open("cat1.jpg"))
    else:
      if self.flag:
        img2 = ImageTk.PhotoImage(Image.open("cat1.jpg"))
        self.myTimer.cancel()
      else:
        img2 = ImageTk.PhotoImage(Image.open("cat2.jpg"))
    self.flag = not self.flag
    self.label.configure(image=img2)
    self.label.image = img2

  def on_press(self, key):
    if not self.flagBlock:
      if (pynput.keyboard.Key):
        self.myTimer.cancel()
        self.change_img()
        self.myTimer = self.newTimer()
        self.myTimer.start()
        self.flagBlock = True

  def on_release(self, key):
    self.flagBlock = False

  def setWindowResizable(self):
    self.flagWindowResizable = not self.flagWindowResizable
    self.win.resizable(self.flagWindowResizable, self.flagWindowResizable)
    self.file.entryconfigure(
        0, label='Resize:' + str(self.flagWindowResizable))

  def setWindowOnTop(self):
    self.flagWindowAlwaysOnTop = not self.flagWindowAlwaysOnTop
    self.win.attributes('-topmost', self.flagWindowAlwaysOnTop)
    self.file.entryconfigure(
        1, label='Always on Top:' + str(self.flagWindowAlwaysOnTop))

p1 = threading.Thread(target=CatWindow())