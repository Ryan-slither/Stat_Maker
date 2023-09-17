import tkinter
from tkinter import font as tkfont
from tkinter import ttk, messagebox
import data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_dict = {"GDP": data.gdp, "Population": data.population, "Crime": data.crime}

class Window:
    def __init__(self, tkwindow: tkinter.Tk):
        self.root = tkwindow
        self.current_frame = None

        # Font Creation
        self.title_font = tkfont.Font(family="Helvetica", size=36)
        self.header_font = self.make_button_font = tkfont.Font(family="Helvetica", size=12, weight="normal", underline=True)
        self.button_font = tkfont.Font(family="Helvetica", size=24, weight="normal")
        self.make_button_font = tkfont.Font(family="Helvetica", size=12, weight="normal")
        self.text_box_font = tkfont.Font(family="Helvetica", size=5, weight="bold")

        # Bar Settings
        self.bar_title = "Untitled"
        self.bar_x = 'x'
        self.bar_tick_size = 5
        self.bar_red = 0
        self.bar_green = 0
        self.bar_blue = 0
        self.bar_opacity = 0
        self.bar_sort = tkinter.IntVar()

        # Scatter Settings
        self.scatter_title = "Untitled"
        self.scatter_x = 'x'
        self.scatter_y = 'y'
        self.scatter_tick_size = 5
        self.scatter_red = 0
        self.scatter_green = 0
        self.scatter_blue = 0
        self.scatter_opacity = 0
        self.scatter_point_opacity = 0
        self.scatter_red_point = 0
        self.scatter_green_point = 0
        self.scatter_blue_point = 0
        self.scatter_line = tkinter.IntVar()

        # Create Start Page
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
        self.to_start_bar_button.grid(row=9, column=0, sticky="nsw", padx=5, pady=2)

        self.make_bar_button = tkinter.Button(self.bar_frame, text="Make Bar Graph", font=self.make_button_font, command=self.get_bar_settings)
        self.make_bar_button.grid(row=9, column=1, sticky="nse", padx=5, pady=2)

        if self.current_frame:
            self.current_frame.grid_forget()
            self.current_frame.destroy()

        self.current_frame = self.bar_frame
        self.fit_frame()

    def make_scatter_page(self):
        self.scatter_frame = tkinter.Frame(self.root, bg="light green", relief="solid", borderwidth=4)

        self.scatter_label = tkinter.Label(self.scatter_frame, text="Scatter Settings", font=self.title_font, bg="light green")
        self.scatter_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=2)

        self.scatter_data_drop_labelx = tkinter.Label(self.scatter_frame, text="Dataset X:", font=self.make_button_font, bg="light green")
        self.scatter_data_drop_labelx.grid(row=1, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_data_dropx = ttk.Combobox(self.scatter_frame, values=list(data_dict.keys()))
        self.scatter_data_dropx.grid(row=1, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_column_drop_labelx = tkinter.Label(self.scatter_frame, text="Data Column X:", font=self.make_button_font, bg="light green")
        self.scatter_column_drop_labelx.grid(row=2, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_column_dropx = ttk.Combobox(self.scatter_frame, values=[])
        self.scatter_column_dropx.grid(row=2, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_data_dropx.bind("<<ComboboxSelected>>", lambda _: self.fill_combo(data_drop=self.scatter_data_dropx, column_drop=self.scatter_column_dropx))

        self.scatter_data_drop_labely = tkinter.Label(self.scatter_frame, text="Dataset Y:", font=self.make_button_font, bg="light green")
        self.scatter_data_drop_labely.grid(row=3, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_data_dropy = ttk.Combobox(self.scatter_frame, values=list(data_dict.keys()))
        self.scatter_data_dropy.grid(row=3, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_column_drop_labely = tkinter.Label(self.scatter_frame, text="Data Column Y:", font=self.make_button_font, bg="light green")
        self.scatter_column_drop_labely.grid(row=4, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_column_dropy = ttk.Combobox(self.scatter_frame, values=[])
        self.scatter_column_dropy.grid(row=4, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_data_dropy.bind("<<ComboboxSelected>>", lambda _: self.fill_combo(data_drop=self.scatter_data_dropy, column_drop=self.scatter_column_dropy))

        self.scatter_title_label = tkinter.Label(self.scatter_frame, text="Graph Title:", font=self.make_button_font, bg="light green")
        self.scatter_title_label.grid(row=5, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_title_textbox = tkinter.Entry(self.scatter_frame)
        self.scatter_title_textbox.grid(row=5, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_x_label = tkinter.Label(self.scatter_frame, text="X Axis Title:", font=self.make_button_font, bg="light green")
        self.scatter_x_label.grid(row=6, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_x_textbox = tkinter.Entry(self.scatter_frame)
        self.scatter_x_textbox.grid(row=6, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_y_label = tkinter.Label(self.scatter_frame, text="Y Axis Title:", font=self.make_button_font, bg="light green")
        self.scatter_y_label.grid(row=7, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_y_textbox = tkinter.Entry(self.scatter_frame)
        self.scatter_y_textbox.grid(row=7, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_ytick_label = tkinter.Label(self.scatter_frame, text="Size of X and Y Ticks:", font=self.make_button_font, bg="light green")
        self.scatter_ytick_label.grid(row=8, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_ytick_size_textbox = tkinter.Entry(self.scatter_frame, width=5)
        self.scatter_ytick_size_textbox.insert(0, '5')
        self.scatter_ytick_size_textbox.grid(row=8, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_color_label = tkinter.Label(self.scatter_frame, text="Line Color (0-255):", font=self.make_button_font, bg="light green")
        self.scatter_color_label.grid(row=9, column=0, sticky="nsew", padx=5, pady=2)

        self.color_frame = tkinter.Frame(self.scatter_frame, bg="light green")
        self.color_frame.grid(row=9, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_color_red_label = tkinter.Label(self.color_frame, text="Red", font=self.make_button_font, bg="light green")
        self.scatter_color_red_label.grid(row=0, column=0, padx=1, sticky="nsew", pady=2)

        self.scatter_color_red = tkinter.Entry(self.color_frame, width=3)
        self.scatter_color_red.insert(0, '50')
        self.scatter_color_red.grid(row=0, column=1, padx=1, sticky="nsew", pady=2)

        self.scatter_color_green_label = tkinter.Label(self.color_frame, text="Green", font=self.make_button_font, bg="light green")
        self.scatter_color_green_label.grid(row=0, column=2, padx=1, sticky="nsew", pady=2)

        self.scatter_color_green = tkinter.Entry(self.color_frame, width=3)
        self.scatter_color_green.insert(0, '50')
        self.scatter_color_green.grid(row=0, column=3, padx=1, sticky="nsew", pady=2)

        self.scatter_color_blue_label = tkinter.Label(self.color_frame, text="Blue", font=self.make_button_font, bg="light green")
        self.scatter_color_blue_label.grid(row=0, column=4, padx=1, sticky="nsew", pady=2)

        self.scatter_color_blue = tkinter.Entry(self.color_frame, width=3)
        self.scatter_color_blue.insert(0, '100')
        self.scatter_color_blue.grid(row=0, column=5, padx=1, sticky="nsew", pady=2)

        self.scatter_color_label_point = tkinter.Label(self.scatter_frame, text="Point Color (0-255):", font=self.make_button_font, bg="light green")
        self.scatter_color_label_point.grid(row=10, column=0, sticky="nsew", padx=5, pady=2)

        self.color_frame_point = tkinter.Frame(self.scatter_frame, bg="light green")
        self.color_frame_point.grid(row=10, column=1, sticky="nsew", padx=5, pady=2)

        self.scatter_color_red_label_point = tkinter.Label(self.color_frame_point, text="Red", font=self.make_button_font, bg="light green")
        self.scatter_color_red_label_point.grid(row=0, column=0, padx=1, sticky="nsew", pady=2)

        self.scatter_color_red_point = tkinter.Entry(self.color_frame_point, width=3)
        self.scatter_color_red_point.insert(0, '50')
        self.scatter_color_red_point.grid(row=0, column=1, padx=1, sticky="nsew", pady=2)

        self.scatter_color_green_label_point = tkinter.Label(self.color_frame_point, text="Green", font=self.make_button_font, bg="light green")
        self.scatter_color_green_label_point.grid(row=0, column=2, padx=1, sticky="nsew", pady=2)

        self.scatter_color_green_point = tkinter.Entry(self.color_frame_point, width=3)
        self.scatter_color_green_point.insert(0, '50')
        self.scatter_color_green_point.grid(row=0, column=3, padx=1, sticky="nsew", pady=2)

        self.scatter_color_blue_label_point = tkinter.Label(self.color_frame_point, text="Blue", font=self.make_button_font, bg="light green")
        self.scatter_color_blue_label_point.grid(row=0, column=4, padx=1, sticky="nsew", pady=2)

        self.scatter_color_blue_point = tkinter.Entry(self.color_frame_point, width=3)
        self.scatter_color_blue_point.insert(0, '100')
        self.scatter_color_blue_point.grid(row=0, column=5, padx=1, sticky="nsew", pady=2)

        self.scatter_opacity_label = tkinter.Label(self.scatter_frame, text="Line Opacity:", font=self.make_button_font, bg="light green")
        self.scatter_opacity_label.grid(row=11, column=0, sticky="nsew", padx=5)

        self.scatter_opacity_slide = tkinter.Scale(self.scatter_frame, from_=100, to=0, orient="horizontal", length=200, bg="light green", highlightthickness=0)
        self.scatter_opacity_slide.set(100)
        self.scatter_opacity_slide.grid(row=11, column=1, sticky="nsew", padx=5)

        self.scatter_point_opacity_label = tkinter.Label(self.scatter_frame, text="Point Opacity:", font=self.make_button_font, bg="light green")
        self.scatter_point_opacity_label.grid(row=12, column=0, sticky="nsew", padx=5)

        self.scatter_point_opacity_slide = tkinter.Scale(self.scatter_frame, from_=100, to=0, orient="horizontal", length=200, bg="light green", highlightthickness=0)
        self.scatter_point_opacity_slide.set(100)
        self.scatter_point_opacity_slide.grid(row=12, column=1, sticky="nsew", padx=5)

        self.scatter_line_label = tkinter.Label(self.scatter_frame, text="Regression Line:", font=self.make_button_font, bg="light green")
        self.scatter_line_label.grid(row=14, column=0, sticky="nsew", padx=5, pady=2)

        self.scatter_line_check = tkinter.Checkbutton(self.scatter_frame, width=5, variable=self.scatter_line, onvalue=1, offvalue=0, bg="light green")
        self.scatter_line_check.select()
        self.scatter_line_check.grid(row=14, column=1, sticky="nsew", padx=5, pady=2)

        self.to_start_scatter_button = tkinter.Button(self.scatter_frame, text="To Start Page", font=self.make_button_font, command=self.make_start)
        self.to_start_scatter_button.grid(row=15, column=0, sticky="nsw", padx=5, pady=2)

        self.make_scatter_button = tkinter.Button(self.scatter_frame, text="Make Scatter Graph", font=self.make_button_font, command=self.get_scatter_settings)
        self.make_scatter_button.grid(row=15, column=1, sticky="nse", padx=5, pady=2)

        if self.current_frame:
            self.current_frame.grid_forget()
            self.current_frame.destroy()

        self.current_frame = self.scatter_frame
        self.fit_frame()

    def make_data_page(self):
        self.data_frame = tkinter.Frame(self.root, bg="light gray", relief="solid", borderwidth=4)

        self.data_label = tkinter.Label(self.data_frame, text="Data Manipulation", font=self.title_font, bg="light gray")
        self.data_label.grid(row=0, column=0, sticky="nsew", pady=15, columnspan=2)

        self.change_data_label = tkinter.Label(self.data_frame, text="Change Between Columns:", font=self.header_font, bg="light gray")
        self.change_data_label.grid(row=1, column=0, sticky="w", padx=5)

        self.change_data_button = tkinter.Button(self.data_frame, text="Create Change Data", font=self.make_button_font, command=self.change_data)
        self.change_data_button.grid(row=1, column=1, sticky="nsew", padx=5, pady=2)

        self.data_drop_label1 = tkinter.Label(self.data_frame, text="Dataset 1:", font=self.make_button_font, bg="light gray")
        self.data_drop_label1.grid(row=2, column=0, sticky="nsew", padx=5, pady=2)

        self.change_data_drop1 = ttk.Combobox(self.data_frame, values=list(data_dict.keys()))
        self.change_data_drop1.grid(row=2, column=1, sticky="nsew", padx=5, pady=2)

        self.change_column_drop_label1 = tkinter.Label(self.data_frame, text="Data Column 1:", font=self.make_button_font, bg="light gray")
        self.change_column_drop_label1.grid(row=3, column=0, sticky="nsew", padx=5, pady=2)

        self.change_column_drop1 = ttk.Combobox(self.data_frame, values=[])
        self.change_column_drop1.grid(row=3, column=1, sticky="nsew", padx=5, pady=2)

        self.change_data_drop1.bind("<<ComboboxSelected>>", lambda _: self.fill_combo(data_drop=self.change_data_drop1, column_drop=self.change_column_drop1))

        self.change_data_drop_label1 = tkinter.Label(self.data_frame, text="Dataset 2:", font=self.make_button_font, bg="light gray")
        self.change_data_drop_label1.grid(row=4, column=0, sticky="nsew", padx=5, pady=2)

        self.change_data_drop2 = ttk.Combobox(self.data_frame, values=list(data_dict.keys()))
        self.change_data_drop2.grid(row=4, column=1, sticky="nsew", padx=5, pady=2)

        self.change_column_drop_label2 = tkinter.Label(self.data_frame, text="Data Column 2:", font=self.make_button_font, bg="light gray")
        self.change_column_drop_label2.grid(row=5, column=0, sticky="nsew", padx=5, pady=2)

        self.change_column_drop2 = ttk.Combobox(self.data_frame, values=[])
        self.change_column_drop2.grid(row=5, column=1, sticky="nsew", padx=5, pady=2)

        self.change_data_drop2.bind("<<ComboboxSelected>>", lambda _: self.fill_combo(data_drop=self.change_data_drop2, column_drop=self.change_column_drop2))

        self.show_data_button1 = tkinter.Button(self.data_frame, text="Show Dataframe 1", font=self.make_button_font, command=lambda: self.show_data_text(drop=self.change_data_drop1))
        self.show_data_button1.grid(row=6, column=0, sticky="nsw", pady=2)
        
        self.show_data_button2 = tkinter.Button(self.data_frame, text="Show Dataframe 2", font=self.make_button_font, command=lambda: self.show_data_text(drop=self.change_data_drop2))
        self.show_data_button2.grid(row=6, column=1, sticky="nse", pady=2, padx=5)

        self.data_text = tkinter.Text(self.data_frame, font=self.text_box_font)
        self.data_text.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=2, padx=5)

        self.to_start_data_button = tkinter.Button(self.data_frame, text="To Start Page", font=self.make_button_font, command=self.make_start)
        self.to_start_data_button.grid(row=8, column=0, sticky="nsew", padx=5, pady=2, columnspan=2)

        if self.current_frame:
            self.current_frame.grid_forget()
            self.current_frame.destroy()

        self.current_frame = self.data_frame
        self.fit_frame()

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
        try:
            return data_dict[self.bar_data_drop.get()][self.bar_column_drop.get()]
        except KeyError:
            messagebox.showerror(title="Data Error", message="No data was found. Pick a valid data set or column")
    
    def scatter_data_choice(self):
        try:
            return (data_dict[self.scatter_data_dropx.get()][self.scatter_column_dropx.get()], data_dict[self.scatter_data_dropy.get()][self.scatter_column_dropy.get()])
        except KeyError:
            messagebox.showerror(title="Data Error", message="No data was found. Pick a valid data set or column")

    def show_data_text(self, drop: ttk.Combobox):
        try:
            data_to_show = data_dict[drop.get()].to_markdown()
        except KeyError:
            messagebox.showerror(title="Data Error", message="No data was found. Pick a valid data set or column")
            return

        self.data_text.delete("1.0", tkinter.END)
        self.data_text.insert("1.0", data_to_show)

    def change_data(self):
        try:
            dataframe = data_dict[self.change_data_drop1.get()]
            col1 = data_dict[self.change_data_drop1.get()][self.change_column_drop1.get()]
            col2 = data_dict[self.change_data_drop2.get()][self.change_column_drop2.get()]
        except KeyError:
            messagebox.showerror(title="Data Error", message="No data was found. Pick a valid data set or column")
            return
        
        data.change_in_data(dataframe, col1, col2)
        self.show_data_text(self.change_data_drop1)

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

    def get_scatter_settings(self):
        self.scatter_title = self.scatter_title_textbox.get()
        self.scatter_x = self.scatter_x_textbox.get()
        self.scatter_y = self.scatter_y_textbox.get()
        self.scatter_opacity = self.scatter_opacity_slide.get()
        self.scatter_point_opacity = self.scatter_point_opacity_slide.get()

        try:
            self.scatter_tick_size = int(self.scatter_ytick_size_textbox.get())
            self.scatter_red = int(self.scatter_color_red.get())
            self.scatter_green = int(self.scatter_color_green.get())
            self.scatter_blue = int(self.scatter_color_blue.get())
            self.scatter_red_point = int(self.scatter_color_red_point.get())
            self.scatter_green_point = int(self.scatter_color_green_point.get())
            self.scatter_blue_point = int(self.scatter_color_blue_point.get())
        except ValueError:
            messagebox.showerror(title="Input Error", message="At least one of your settings contains characters where numbers should be, "
                                                              "or is empty and needs to be filled (tick size or color amounts)")
            return
        
        self.make_scatter(title=self.scatter_title, x_name=self.scatter_x, y_name=self.scatter_y, font_size=self.scatter_tick_size,
                      line_opacity=self.scatter_opacity/100, point_opacity=self.scatter_point_opacity/100, 
                      reg_line=self.scatter_line.get(), line_color=(self.scatter_red/255, self.scatter_green/255, self.scatter_blue/255), 
                      point_color=(self.scatter_red_point/255, self.scatter_green_point/255, self.scatter_blue_point/255))

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

    def make_scatter(self, title: str = "Untitled", x_name: str = 'x', font_size: int = 4,
                    y_name: str = 'y', reg_line: bool = True, point_opacity: float = .5, line_opacity: float = .5,
                    point_color: tuple = (.1, .3, .7), line_color: tuple = (0, 0, 0)):
        plt.close()
        print("Scatter")
        data_x, data_y = self.scatter_data_choice()[0].copy(), self.scatter_data_choice()[1].copy()
        if len(data_x) > len(data_y):
            data_x = data_x[data_y.index]
        else:
            data_y = data_y.loc[data_x.index]
        data_x, data_y = data_x.astype(dtype="float"), data_y.astype(dtype="float")
        coef = np.polyfit(data_x, data_y, 1)
        poly_fn = np.poly1d(coef)
        for i, txt in enumerate(data_x.index):
            plt.annotate(f"   {txt}", (data_x.iloc[i], data_y.iloc[i]), fontsize=font_size)
        plt.grid(visible=True)
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