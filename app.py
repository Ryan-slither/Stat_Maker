import tkinter
from tkinter import font as tkfont
from tkinter import ttk, messagebox
import data
import matplotlib.pyplot as plt
import pandas as pd
import typing
import numpy as np

data_dict = {"GDP": data.gdp, "Population": data.population, "Crime": data.crime}

class Window:
    def __init__(self, tkwindow: tkinter.Tk):
        self.root = tkwindow
        self.current_frame = None

        # Font Creation
        self.title_font = tkfont.Font(family="Helvetica", size=36)
        self.button_font = tkfont.Font(family="Helvetica", size=24, weight="normal")
        self.make_button_font = tkfont.Font(family="Helvetica", size=12, weight="normal")

        # Bar Settings
        self.bar_title = "Untitled"
        self.bar_x = "x"
        self.bar_tick_size = 5
        self.bar_red = 0
        self.bar_green = 0
        self.bar_blue = 0
        self.bar_opacity = 0
        self.bar_sort = tkinter.IntVar()

        self.make_start()
    
    def make_start(self):
        self.start_frame = tkinter.Frame(self.root, bg="light blue", relief="solid", borderwidth=4)

        self.root.columnconfigure(0, weight=1)

        self.start_label = tkinter.Label(self.start_frame, text="Stat Maker", font=self.title_font, bg="light blue")
        self.start_label.grid(row=0, column=0, sticky="nsew", pady=15)

        self.bar_button = tkinter.Button(self.start_frame, text="Bar Graph", font=self.button_font, command=self.make_bar_page)
        self.bar_button.grid(row=1, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_button = tkinter.Button(self.start_frame, text="Scatter Plot", font=self.button_font, command=self.make_scatter_page)
        self.scatter_button.grid(row=2, column=0, sticky="nsew", padx=5, pady=2)

        self.data_button = tkinter.Button(self.start_frame, text="Data", font=self.button_font, command=self.make_data_page)
        self.data_button.grid(row=3, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_button = tkinter.Button(self.start_frame, text="Exit", font=self.button_font, command=self.exit_window)
        self.scatter_button.grid(row=4, column=0, sticky="nsew", padx=5, pady=2)

        if self.current_frame:
            self.current_frame.grid_forget()
            self.current_frame.destroy()

        self.current_frame = self.start_frame
        self.fit_frame()

    def make_bar_page(self):
        self.bar_frame = tkinter.Frame(self.root, bg="light salmon", relief="solid", borderwidth=4)

        self.bar_label = tkinter.Label(self.bar_frame, text="Bar Settings", font=self.title_font, bg="light salmon")
        self.bar_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=2)

        self.bar_data_drop_label = tkinter.Label(self.bar_frame, text="Dataset:", font=self.make_button_font, bg="light salmon")
        self.bar_data_drop_label.grid(row=1, column=0, sticky="nsew", padx=5, pady=2)

        self.bar_data_drop = ttk.Combobox(self.bar_frame, values=list(data_dict.keys()))
        self.bar_data_drop.grid(row=1, column=1, sticky="nsew", padx=5, pady=2)

        self.bar_column_drop_label = tkinter.Label(self.bar_frame, text="Data Column:", font=self.make_button_font, bg="light salmon")
        self.bar_column_drop_label.grid(row=2, column=0, sticky="nsew", padx=5, pady=2)

        self.bar_column_drop = ttk.Combobox(self.bar_frame, values=[])
        self.bar_column_drop.grid(row=2, column=1, sticky="nsew", padx=5, pady=2)

        self.bar_data_drop.bind("<<ComboboxSelected>>", lambda _: self.fill_combo(data_drop=self.bar_data_drop, column_drop=self.bar_column_drop))

        self.bar_title_label = tkinter.Label(self.bar_frame, text="Graph Title:", font=self.make_button_font, bg="light salmon")
        self.bar_title_label.grid(row=3, column=0, sticky="nsew", padx=5, pady=2)

        self.bar_title_textbox = tkinter.Entry(self.bar_frame)
        self.bar_title_textbox.grid(row=3, column=1, sticky="nsew", padx=5, pady=2)

        self.bar_x_label = tkinter.Label(self.bar_frame, text="X Axis Title:", font=self.make_button_font, bg="light salmon")
        self.bar_x_label.grid(row=4, column=0, sticky="nsew", padx=5, pady=2)

        self.bar_x_textbox = tkinter.Entry(self.bar_frame)
        self.bar_x_textbox.grid(row=4, column=1, sticky="nsew", padx=5, pady=2)

        self.bar_ytick_label = tkinter.Label(self.bar_frame, text="Size of Y Ticks:", font=self.make_button_font, bg="light salmon")
        self.bar_ytick_label.grid(row=5, column=0, sticky="nsew", padx=5, pady=2)

        self.bar_ytick_size_textbox = tkinter.Entry(self.bar_frame, width=5)
        self.bar_ytick_size_textbox.insert(0, '5')
        self.bar_ytick_size_textbox.grid(row=5, column=1, sticky="nsew", padx=5, pady=2)

        self.bar_color_label = tkinter.Label(self.bar_frame, text="Graph Color (0-255):", font=self.make_button_font, bg="light salmon")
        self.bar_color_label.grid(row=6, column=0, sticky="nsew", padx=5, pady=2)

        self.color_frame = tkinter.Frame(self.bar_frame, bg="light salmon")
        self.color_frame.grid(row=6, column=1, sticky="nsew", padx=5, pady=2)

        self.bar_color_red_label = tkinter.Label(self.color_frame, text="Red", font=self.make_button_font, bg="light salmon")
        self.bar_color_red_label.grid(row=0, column=0, padx=1, sticky="nsew", pady=2)

        self.bar_color_red = tkinter.Entry(self.color_frame, width=3)
        self.bar_color_red.insert(0, '50')
        self.bar_color_red.grid(row=0, column=1, padx=1, sticky="nsew", pady=2)

        self.bar_color_green_label = tkinter.Label(self.color_frame, text="Green", font=self.make_button_font, bg="light salmon")
        self.bar_color_green_label.grid(row=0, column=2, padx=1, sticky="nsew", pady=2)

        self.bar_color_green = tkinter.Entry(self.color_frame, width=3)
        self.bar_color_green.insert(0, '50')
        self.bar_color_green.grid(row=0, column=3, padx=1, sticky="nsew", pady=2)

        self.bar_color_blue_label = tkinter.Label(self.color_frame, text="Blue", font=self.make_button_font, bg="light salmon")
        self.bar_color_blue_label.grid(row=0, column=4, padx=1, sticky="nsew", pady=2)

        self.bar_color_blue = tkinter.Entry(self.color_frame, width=3)
        self.bar_color_blue.insert(0, '100')
        self.bar_color_blue.grid(row=0, column=5, padx=1, sticky="nsew", pady=2)

        self.bar_opacity_label = tkinter.Label(self.bar_frame, text="Color Opacity:", font=self.make_button_font, bg="light salmon")
        self.bar_opacity_label.grid(row=7, column=0, sticky="nsew", padx=5, pady=2)

        self.bar_opacity_slide = tkinter.Scale(self.bar_frame, from_=100, to=0, orient="horizontal", length=200, bg="light salmon", highlightthickness=0)
        self.bar_opacity_slide.set(100)
        self.bar_opacity_slide.grid(row=7, column=1, sticky="nsew", padx=5)

        self.bar_sorted_label = tkinter.Label(self.bar_frame, text="Sort Data:", font=self.make_button_font, bg="light salmon")
        self.bar_sorted_label.grid(row=8, column=0, sticky="nsew", padx=5, pady=2)

        self.bar_sorted_check = tkinter.Checkbutton(self.bar_frame, width=5, variable=self.bar_sort, onvalue=1, offvalue=0, bg="light salmon")
        self.bar_sorted_check.select()
        self.bar_sorted_check.grid(row=8, column=1, sticky="nsew", padx=5, pady=2)

        self.to_start_bar_button = tkinter.Button(self.bar_frame, text="To Start Page", font=self.make_button_font, command=self.make_start)
        self.to_start_bar_button.grid(row=9, column=0, sticky="nsew", padx=5, pady=2)

        self.make_bar_button = tkinter.Button(self.bar_frame, text="Make Bar Graph", font=self.make_button_font, command=self.get_bar_settings)
        self.make_bar_button.grid(row=9, column=1, sticky="nsew", pady=2)

        if self.current_frame:
            self.current_frame.grid_forget()
            self.current_frame.destroy()

        self.current_frame = self.bar_frame
        self.fit_frame()

    def make_scatter_page(self):
        pass

    def make_data_page(self):
        pass

    def exit_window(self):
        self.root.destroy()
        plt.close('all')

    def fit_frame(self):
        self.current_frame.grid(row=0, column=0, columnspan=10, rowspan=10, sticky="nsew")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.current_frame.columnconfigure(0, weight=1)

    def fill_combo(self, data_drop : ttk.Combobox, column_drop: ttk.Combobox):
        column_drop.set("")
        dataset = data_dict[data_drop.get()]
        column_drop["values"] = list(dataset.columns)
    
    def bar_data_choice(self):
        return data_dict[self.bar_data_drop.get()][self.bar_column_drop.get()]

    def get_bar_settings(self):
        self.bar_title = self.bar_title_textbox.get()
        self.bar_x = self.bar_x_textbox.get()
        self.bar_opacity = self.bar_opacity_slide.get()

        try:
            self.bar_tick_size = int(self.bar_ytick_size_textbox.get())
            self.bar_red = int(self.bar_color_red.get())
            self.bar_green = int(self.bar_color_green.get())
            self.bar_blue = int(self.bar_color_blue.get())
        except ValueError:
            messagebox.showerror(title="Input Error", message="At least one of your settings contains characters where numbers should be, "
                                                              "or is empty and needs to be filled (tick size or color amounts)")
            return
        
        self.make_bar(title=self.bar_title, x_name=self.bar_x, font_size=self.bar_tick_size,
                      opacity=self.bar_opacity/100, sorted=self.bar_sort.get(), color=(self.bar_red/255, self.bar_green/255, self.bar_blue/255))

    def make_bar(self, title: str = "Untitled", x_name: str = "x", font_size: int = 5, opacity: float = .5,
             sorted: bool = True, color: tuple = (.1, .3, .7)):
        plt.close()
        print("Histogram")
        data = self.bar_data_choice().copy()
        data = data.astype(dtype="float")
        if sorted:
            data = data.sort_values()
        plt.barh(data.index, data, color=color, alpha=opacity)
        plt.grid(visible=True)
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