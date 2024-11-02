import tkinter as tk
import PIL.Image
from PIL import ImageTk, Image
import threading


#
class Controller:
    def __init__(self, root, img_size=(300, 550), background_color='black'):
        self.root = root
        self.background_color = background_color
        self.root.title("Controller")
        self.root.configure(bg=background_color)
        root.attributes('-fullscreen', True)
        self.window_width = int(window.winfo_screenwidth() / 58)
        self.window_height = (self.window_width * 2)
        self.img_size = img_size
        # Start visualizing the code.
        self.t1 = threading.Thread(target=self.flash_top)
        # self.t2 = threading.Thread(target=self.flash_right)
        self.t3 = threading.Thread(target=self.flash_bottom)
        # self.t4 = threading.Thread(target=self.flash_left)
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

        # self.right = self.canvas.create_rectangle(center_x + 150 - self.rect_width // 2,
        #                                           center_y - self.rect_height // 2,
        #                                           center_x + 150 + self.rect_width // 2,
        #                                           center_y + self.rect_height // 2,
        #                                           fill='black')

        # self.left = self.canvas.create_rectangle(center_x - 150 - self.rect_width // 2,
        #                                          center_y - self.rect_height // 2,
        #                                          center_x - 150 + self.rect_width // 2,
        #                                          center_y + self.rect_height // 2,
        #                                          fill='black')

        self.is_on_top = False
        self.is_on_bottom = False
        self.is_on_right = False
        self.is_on_left = False
        self.during_break = False
        # Recursion settings
        self.threading()
        threading.Lock()


    def run(self):
        # starts running the actual code.
        self.root.mainloop()

    def threading(self):
        self.t1 = threading.Thread(target=self.take_a_break())
        self.t1.run()
        self.flash_top()
        self.flash_bottom()
        # self.flash_right()
        # self.flash_left()

    def flash_top(self):
        self.canvas.itemconfig(self.up, fill='white' if self.is_on_top else 'black')
        self.is_on_top = not self.is_on_top
        self.root.after(100, self.flash_top)

    def flash_right(self):
        self.canvas.itemconfig(self.right, fill='white' if self.is_on_right else 'black')
        self.is_on_right = not self.is_on_right
        self.root.after(200, self.flash_right)

    def flash_bottom(self):
        self.canvas.itemconfig(self.down, fill='white' if self.is_on_bottom else 'black')
        self.is_on_bottom = not self.is_on_bottom
        self.root.after(76, self.flash_bottom)

    def flash_left(self):
        self.canvas.itemconfig(self.left, fill='white' if self.is_on_left else 'black')

        self.is_on_left = not self.is_on_left
        if self.during_break:
            self.root.after(185, self.flash_left)




    def take_a_break(self):
        while True:
            self.root.after(60000)
            if self.during_break:
                self.during_break = False
            else:
                self.during_break = True




# Initializes the Code
window = tk.Tk()
RC_Controller = Controller(window, background_color='white', img_size=(300, 525))
RC_Controller.run()
