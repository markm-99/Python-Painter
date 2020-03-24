import tkinter
class PaintApp:

    """
    GUI PaintApp class for simple color app
    GUI PaintApp = simple coloring app

    Argument: (tkinter.Tk): root window object

    Attribute: canvas (tkinter.Canvas): the widget defining the area to be painted
                color(string): paint color chosen
    """


def main():
        # create gui main window

        root = tkinter.Tk()
        # instantiate pain app objec
        painting = PaintApp(root)
        # enter main event loop and wait for events

        root.mainloop()

    if __name__ == '__main__':
        main()

def __init__(self,parent):
    parent.title("CS 122 - Let's Paint!")
    color_frame = tkinter.Frame(parent)
    color_frame.grid()
    green_button = tkinter.Button(color_frame, text='GREEN', width=10,command=self.green)
    green_button.grid(column=0, row=0)

    red_button = tkinter.Button(color_frame, text='RED', width=10,
                                  command=self.red)

    blue_button = tkinter.Button(color_frame, text='BLUE', width=10,
                                command=self.blue)
    red_button.grid(column=1, row=0)

    blue_button.grid(column=2, row=0)


#     instantiate canvas widget with root as parent
    self.canvas = tkinter.Canvas(parent, width=300,height=300)
erase_button = tkinter.Button(parent,text='ERASER', width=30, command = self.erase)
erase_button.grid()


def green(self):
    self.color = "green"


def red(self):
    self.color = "red"


def blue(self):
    self.color = "blue"


    self.color = self.default_color
    self.erase()


    #     draw rectangle on canvas for background
    #     coordinates of upper left(x,y), and lower right(x,y)
    # canvas rectangle
    self.canvas.create_rectangle(0,0,300,300)
    # house rectangle
    self.canvas.create_rectangle(175,150,275,250)
#     triangle roof
    self.canvas.create_polygon(165,150,225,100,285,150, outline='black', fill='white')
    # flower
    self.canvas.create_oval(50,200,75,225)
    self.canvas.create_oval(50,175,75,200)
    self.canvas.create_oval(50,275,75,250)
    self.canvas.create_oval(25,187,50,212)
    self.canvas.create_oval(25,212,50,237)
    self.canvas.create_oval(75,187,100,212)
    self.canvas.create_oval(75,212,100,237)

    self.canvas.grid()