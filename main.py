import data
import app
import tkinter
import multiprocessing
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

window = tkinter.Tk()
app = app.Window(window)
window.title("Stat Maker")
window.geometry("600x600")

def make_stat():
    data.change_in_data(data.gdp, "2020", "2021")
    app.make_scatter(data.gdp["change_2020-2021"], data.population["PPOPCHG_2021"], x_name="Change in GDP (millions of current dollars)", y_name="Change in Population", title="Change in GDP vs. Change in Population (20-21)")

def make_app():
    window.mainloop()

if __name__ == "__main__":
    #p1 = multiprocessing.Process(name='p1', target=make_stat)
    p2 = multiprocessing.Process(name='p2', target=make_app)
    #p1.start()
    p2.start()