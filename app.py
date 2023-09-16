import tkinter
from tkinter import font as tkfont
from tkinter import ttk
import data
import matplotlib.pyplot as plt
import pandas as pd
import typing
import numpy as np

data_dict = {"GDP": data.gdp, "Population": data.population, "Crime": data.crime}

class Window:
    def __init__(self, tkwindow):
        self.root = tkwindow
        self.current_frame = None
        self.title_font = tkfont.Font(family="Helvetica", size=36, weight="bold")
        self.button_font = tkfont.Font(family="Helvetica", size=24, weight="normal")
        self.make_button_font = tkfont.Font(family="Helvetica", size=12, weight="normal")
        self.make_start()
    
    def make_start(self):
        self.start_frame = tkinter.Frame(self.root)

        self.start_label = tkinter.Label(self.start_frame, text="Stat Maker", justify="center", font=self.title_font)
        self.start_label.grid(row=0, column=0)

        self.bar_button = tkinter.Button(self.start_frame, text="Bar Graph", justify="center", font=self.button_font, command=self.make_bar_page)
        self.bar_button.grid(row=1, column=0)

        if self.current_frame:
            self.current_frame.grid_forget()
            self.current_frame.destroy()

        self.current_frame = self.start_frame
        self.fit_frame()

    def make_bar_page(self):
        self.bar_frame = tkinter.Frame(self.root)

        self.bar_label = tkinter.Label(self.bar_frame, text="Bar Settings", font=self.title_font)
        self.bar_label.grid(row=0, column=0, columnspan=2)

        self.bar_data_drop_label = tkinter.Label(self.bar_frame, text="Dataset:", font=self.make_button_font)
        self.bar_data_drop_label.grid(row=1, column=0)

        self.bar_data_drop = ttk.Combobox(self.bar_frame, values=list(data_dict.keys()))
        self.bar_data_drop.grid(row=1, column=1)

        self.bar_column_drop_label = tkinter.Label(self.bar_frame, text="Data Column:", font=self.make_button_font)
        self.bar_column_drop_label.grid(row=2, column=0)

        self.bar_column_drop = ttk.Combobox(self.bar_frame, values=[])
        self.bar_column_drop.grid(row=2, column=1)

        self.bar_data_drop.bind("<<ComboboxSelected>>", lambda _: self.fill_combo(data_drop=self.bar_data_drop, column_drop=self.bar_column_drop))

        self.bar_title_label = tkinter.Label(self.bar_frame, text="Graph Title:", font=self.make_button_font)
        self.bar_title_label.grid(row=3, column=0)

        self.bar_title_textbox = tkinter.Entry(self.bar_frame)
        self.bar_title_textbox.grid(row=3, column=1)

        self.bar_x_label = tkinter.Label(self.bar_frame, text="X Axis Title:", font=self.make_button_font)
        self.bar_x_label.grid(row=4, column=0)

        self.bar_x_textbox = tkinter.Entry(self.bar_frame)
        self.bar_x_textbox.grid(row=4, column=1)

        self.bar_ytick_label = tkinter.Label(self.bar_frame, text="Size of Y Ticks:", font=self.make_button_font)
        self.bar_ytick_label.grid(row=5, column=0)

        self.bar_ytick_size_textbox = tkinter.Entry(self.bar_frame)
        self.bar_ytick_size_textbox.grid(row=5, column=1)

        self.bar_color_label = tkinter.Label(self.bar_frame, text="Graph Color:", font=self.make_button_font)
        self.bar_color_label.grid(row=6, column=0)

        self.color_frame = tkinter.Frame(self.bar_frame)
        self.color_frame.grid(row=6, column=1)

        self.bar_color_red_label = tkinter.Label(self.color_frame, text="Red", font=self.make_button_font)
        self.bar_color_red_label.grid(row=0, column=0, padx=1)

        self.bar_color_red = tkinter.Entry(self.color_frame)
        self.bar_color_red.grid(row=0, column=1, padx=1)

        self.bar_color_green = tkinter.Entry(self.color_frame)
        self.bar_color_green.grid(row=0, column=2, padx=1)

        self.bar_color_blue = tkinter.Entry(self.color_frame)
        self.bar_color_blue.grid(row=0, column=3, padx=1)

        self.color_frame.grid_configure(row=6)

        self.bar_opacity_label = tkinter.Label(self.bar_frame, text="Color Opacity", font=self.make_button_font)
        self.bar_opacity_label.grid(row=7, column=0)

        self.bar_opacity_slide = tkinter.Scale(self.bar_frame, from_=0, to=100, orient="horizontal")
        self.bar_opacity_slide.grid(row=7, column=1)




        self.to_start_bar_button = tkinter.Button(self.bar_frame, text="To Start Page", font=self.make_button_font, command=self.make_start)
        self.to_start_bar_button.grid(row=10, column=0)

        self.make_bar_button = tkinter.Button(self.bar_frame, text="Make Bar Graph", font=self.make_button_font, command=self.make_bar)
        self.make_bar_button.grid(row=10, column=1)

        if self.current_frame:
            self.current_frame.grid_forget()
            self.current_frame.destroy()

        self.current_frame = self.bar_frame
        self.fit_frame()

    def fit_frame(self):
        self.current_frame.grid(row=0, column=0)

    def fill_combo(self, data_drop : ttk.Combobox, column_drop: ttk.Combobox):
        column_drop.set("")
        dataset = data_dict[data_drop.get()]
        column_drop["values"] = list(dataset.columns)
    
    def bar_data_choice(self):
        return data_dict[self.bar_data_drop.get()][self.bar_column_drop.get()]

    def make_bar(self, data: pd.Series = None, title: str = "Untitled", x_name: str = "x", font_size: int = 5, opacity: float = .5,
             sorted: bool = True, color: typing.Union[tuple, str] = (.1, .3, .7)):
        print("Histogram")
        data = self.bar_data_choice()
        data = data.astype(dtype="float")
        if sorted:
            data = data.sort_values()
        plt.barh(data.index, data, color=color, alpha=opacity)
        plt.grid()
        plt.xscale("linear")
        plt.xlabel(x_name)
        plt.title(title)
        plt.yticks(fontsize=font_size)
        plt.show()

    def make_scatter(self, data_x: pd.Series, data_y: pd.Series, title: str = "Untitled", x_name: str = 'x', font_size: int = 4,
                    y_name: str = 'y', reg_line: bool = True, point_opacity: float = .5, line_opacity: float = .5,
                    point_color: typing.Union[tuple, str] = (.1, .3, .7), line_color: typing.Union[tuple, str] = (0, 0, 0)):
        print("Scatter")
        if len(data_x) > len(data_y):
            data_x = data_x[data_y.index]
        else:
            data_y = data_y.loc[data_x.index]
        data_x, data_y = data_x.astype(dtype="float"), data_y.astype(dtype="float")
        coef = np.polyfit(data_x, data_y, 1)
        poly_fn = np.poly1d(coef)
        for i, txt in enumerate(data_x.index):
            plt.annotate(f"   {txt}", (data_x.iloc[i], data_y.iloc[i]), fontsize=font_size)
        plt.grid()
        plt.title(title)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.xscale("linear")
        plt.yscale("linear")
        plt.plot(data_x, data_y, 'o', color=point_color, alpha=point_opacity)
        if reg_line:
            plt.plot(data_x, poly_fn(data_x), color=line_color, alpha=line_opacity)
        plt.show()

if __name__ == "__main__":
    pass