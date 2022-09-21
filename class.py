from tkinter import messagebox, Menu, Label, Tk
from PIL import Image, ImageTk
import pynput
import threading

class CatWindow:
  flag_key_still_pressed = False;
  flag_image_change = False
  flag_on_function_change_img = False
  flag_on_function_on_window_change = False
  amount_keys_pressed_on_interval = 0
  amount_keys_pressed = 0
  
  
  def __init__(self):
    self.win = Tk()
    self.win.title('BongoCatPy!!')
    
    #Center window
    self.set_variables_from_config_file()
    self.win.geometry(f'{self.app_width}x{self.app_height}+{self.x}+{self.y}')
      
    #Menu
    menubar = Menu(self.win)
    
    #Menu file
    self.file = Menu(menubar, tearoff=0)
    self.file.add_command(label='Resize: ' + str(self.window_is_resizable), command=self.set_window_resizable)
    self.file.add_command(label='Always on Top: ' + str(self.window_always_on_top), command=self.set_window_on_top)
    self.file.add_command(label='Show total keys pressed: ' + str(self.flag_amount_keys_pressed), command=self.set_show_amount_keys)
    self.file.add_separator()
    self.file.add_command(label='Exit', command=self.on_closing)
    menubar.add_cascade(label='Options', menu=self.file)
    
    #Menu about
    about = Menu(menubar, tearoff=0)
    about.add_command(label='About', command=self.on_about)
    menubar.add_cascade(label='About', menu=about, command=self.on_about)

    self.background_image = ImageTk.PhotoImage(Image.open('./image/1.jpg'))
    self.label_img = Label(self.win, image=self.background_image)
    self.label_img.pack()
    if self.flag_amount_keys_pressed:
      self.label_amount_keys = Label(self.win, text=f'Teclas pressionadas: {self.amount_keys_pressed}')
      self.label_amount_keys.pack()

    self.win.config(menu=menubar)
    self.win.resizable(self.window_is_resizable, self.window_is_resizable)
    self.win.attributes('-topmost', self.window_always_on_top)
    
    self.win.protocol('WM_DELETE_WINDOW', self.on_closing)
    self.win.bind('<Configure>', self.on_window_change)
    self.win.update()
    self.key_listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
    self.key_listener.start()
    self.timer_to_reset_image = self.create_timer()
    
    self.win.mainloop()
    self.key_listener.join()
    
    
  #Funcoes da atualizacao da imagem
  def change_img(self, reset=False):
    self.flag_on_function_change_img = True
    if(reset):
      self.amount_keys_pressed_on_interval = 0
      file_name = '1'
    else:
      self.timer_to_reset_image.cancel()
      if self.amount_keys_pressed_on_interval > 20:
        if self.flag_image_change:
          file_name = '4'
        else:
          file_name = '5'
      else:
        self.amount_keys_pressed_on_interval += 1
        if self.flag_image_change:
          file_name = '2'
        else:
          file_name = '3'
      self.flag_image_change = not self.flag_image_change
    img2 = ImageTk.PhotoImage(Image.open(f'./image/{file_name}.jpg'))
    self.label_img.configure(image=img2)
    self.label_img.image = img2
    if self.flag_amount_keys_pressed:
      self.label_amount_keys.configure(text=f'Teclas pressionadas: {self.amount_keys_pressed}')
    self.flag_on_function_change_img = False


  #Funcoes para a janela
  def on_window_change(self, position):
    if not self.flag_on_function_on_window_change:
      self.save_config_file(position=position,
                            on_top=self.window_always_on_top,
                            resizable=self.window_is_resizable,
                            show_keys_pressed=self.flag_amount_keys_pressed)
  
  
  def set_variables_from_config_file(self):
    config_dict = self.read_config_file()
    if config_dict:
      self.app_width = config_dict['width']
      self.app_height = config_dict['height']
      self.x = config_dict['x']
      self.y = config_dict['y']
      self.window_always_on_top = (config_dict['on_top'] == 'True')
      self.window_is_resizable = (config_dict['resizable'] == 'True')
      self.flag_amount_keys_pressed = (config_dict['show_keys_pressed'] == 'True')
    else:
      self.window_is_resizable = True
      self.window_always_on_top = True
      self.flag_amount_keys_pressed = True
      self.app_width = 270
      self.app_height = 270
      self.x = int(self.win.winfo_screenwidth()/2 - self.app_width/2)
      self.y = int(self.win.winfo_screenheight()/2 - self.app_height/2)
      
  
  def read_config_file(self):
    config_dict = {}
    try:
      with open('config.conf', 'r') as file:
        for line in file:
          key, value = line.split()
          config_dict[key] = value
    except:
      print('file not found')
    finally:
      return config_dict


  def save_config_file(self, *, position=None, on_top=None, resizable=None, show_keys_pressed=None):
    self.flag_on_function_on_window_change = True
    config_dict = {}
    if position != None:
      config_dict['width'] = position.width
      config_dict['height'] = position.height
      config_dict['x'] = position.x
      config_dict['y'] = position.y
    if on_top != None:
      config_dict['on_top'] = on_top
    if resizable != None:
      config_dict['resizable'] = resizable
    if show_keys_pressed != None:
      config_dict['show_keys_pressed'] = show_keys_pressed
    
    with open('config.conf', 'w+') as file:
      for key, value in config_dict.items():
        file.write(f'{key} {value}\n')
    self.flag_on_function_on_window_change = False
    
  def on_about(self):
    messagebox.showinfo('Sobre nós', '\n'.join(
        ['Desenvolvido por:',
         'Jó Sales - github.com/josalesmj',
         'Amanda Girão - amandagirao.com']))
        
        
  def on_closing(self):
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        self.key_listener.stop()
        self.timer_to_reset_image.cancel()
        self.win.destroy()
    
    
  def set_window_resizable(self):
    self.window_is_resizable = not self.window_is_resizable
    self.win.resizable(self.window_is_resizable, self.window_is_resizable)
    self.file.entryconfigure(0, label='Resize: ' + str(self.window_is_resizable))
  
  
  def set_window_on_top(self):
    self.window_always_on_top = not self.window_always_on_top
    self.win.attributes('-topmost', self.window_always_on_top)
    self.file.entryconfigure(1, label='Always on Top: ' + str(self.window_always_on_top))
    
    
  def set_show_amount_keys(self):
    self.flag_amount_keys_pressed = not self.flag_amount_keys_pressed
    self.file.entryconfigure(2, label='Show total keys pressed: ' + str(self.flag_amount_keys_pressed))
    if self.flag_amount_keys_pressed:
      self.label_amount_keys = Label(self.win, text=f'Teclas pressionadas: {self.amount_keys_pressed}')
      self.label_amount_keys.pack()
    else:
      self.label_amount_keys.destroy()
    
    
  #Funcoes do listener do teclado
  def on_press(self, key):
    if not self.flag_key_still_pressed:
      self.amount_keys_pressed += 1
      if (pynput.keyboard.Key):
        self.timer_to_reset_image.cancel()
        if not self.flag_on_function_change_img:
          self.change_img()
        self.timer_to_reset_image = self.create_timer()
        self.timer_to_reset_image.start()
        self.flag_key_still_pressed = True


  def on_release(self, key):
    self.flag_key_still_pressed = False
  
    
  def create_timer(self):
    return threading.Timer(0.5, self.change_img, [True])
    
    
catWindow = threading.Thread(target=CatWindow())