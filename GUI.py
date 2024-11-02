import tkinter as tk
import PIL.Image
from PIL import ImageTk, Image
import threading


#
class Controller:
    def __init__(self, root, img_size=(300, 550), background_color='black'):
        # Window stuff
        self.root = root
        self.background_color = background_color
        self.root.title("Controller")
        self.root.configure(bg=background_color)
        root.attributes('-fullscreen', True)
        self.window_width = int(window.winfo_screenwidth() / 58)
        self.window_height = (self.window_width * 2)
        self.img_size = img_size
        # threading stuff
        self.t1 = threading.Thread(target=self.flash_top)
        self.t3 = threading.Thread(target=self.flash_bottom)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, bg='white')
        self.canvas.place(anchor='center', relx=0.5, rely=0.5)


        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        self.rect_width = 130
        self.rect_height = 130
        # Draw light rectangles (using canvas)
        self.up = self.canvas.create_rectangle(center_x - self.rect_width // 2,
                                               center_y - 150 - self.rect_height // 2,
                                               center_x + self.rect_width // 2,
                                               center_y - 150 + self.rect_height // 2,
                                               fill='black')

        self.down = self.canvas.create_rectangle(center_x - self.rect_width // 2,
                                                 center_y + 150 - self.rect_height // 2,
                                                 center_x + self.rect_width // 2,
                                                 center_y + 150 + self.rect_height // 2,
                                                 fill='black')

        self.is_on_top = False
        self.is_on_bottom = False
        self.threading()

    def run(self):
        self.root.mainloop()

    def threading(self):
        self.t1.start()
        self.t3.start()


    def flash_top(self):
        self.canvas.itemconfig(self.up, fill='white' if self.is_on_top else 'black')
        self.is_on_top = not self.is_on_top
        self.root.after(83, self.flash_top)

    def flash_bottom(self):
        self.canvas.itemconfig(self.down, fill='white' if self.is_on_bottom else 'black')
        self.is_on_bottom = not self.is_on_bottom
        self.root.after(66, self.flash_bottom)





# Initializes the Code
window = tk.Tk()
RC_Controller = Controller(window, background_color='white', img_size=(300, 525))
RC_Controller.run()
