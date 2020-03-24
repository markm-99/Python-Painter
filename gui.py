
import tkinter

# gui app main window
def main():
    # default top level window
    root = tkinter.Tk()
    # rename title window

    root.title('CS 122')
    hello = tkinter.Label(root, text = "Hello World!")
    hello.pack()

    # code that waits for the user
    root.mainloop()

if __name__ == '__main__':
    main()

