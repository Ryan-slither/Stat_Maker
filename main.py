import tkinter
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def make_app():
    window = tkinter.Tk()
    app = app.Window(window)
    window.title("Stat Maker")
    window.geometry("500x620")
    window.mainloop()

if __name__ == "__main__":
    make_app()