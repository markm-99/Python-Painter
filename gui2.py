import tkinter

class GenApp:
    """
    class to support a general GUI app
    """

def main():
    # root window instantiated
    root = tkinter.Tk()

    # instantiate the genapp object
    gen_app =  GenApp(root)

    # code to add widgets comes after this main event loop
    root.mainloop()

    def __init__(self, parent):
        parent.title('CS 122')

        # instantiate the button
        start_button = tkinter.Button(parent, text = 'START', width = 20,command = self.start )

       # create start button
        start_button.grid()

        self.stop_image = tkinter.PhotoImage(file = "stop.gif")
        # instantiate the button
        stop_button = tkinter.Button(parent, image=self.stop_image,command = self.stop )
        # create the stop button
        stop_button.grid()

        # needs to be updated from the start and stop methods
        # methods can access and make changes when called
        self.status = tkinter.Label(parent, text = 'Ready to start')

        # update within the grid
        self.status.grid()

    def start(self):
        """

        :param self:
        :return: None
        """
        self.status.configure(text='In progress', foreground='green')

    def stop(self):
        """

        :param self:
        :return:
        """
        self.status.configure(text='All done!', foreground='red')


def main():

    if __name__ == '__main__':
        main()


