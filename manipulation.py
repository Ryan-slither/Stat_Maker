import matplotlib.pyplot as plt
import pandas as pd
import typing

def make_bar(data: pd.Series, title: str = "Untitled", x_name: str = "x", font_size: int = 5,
              sorted: bool = True, color: typing.Union[tuple, str] = (.1, 1, .1)):
    print("Histogram")
    data = data.astype(dtype="float")
    if sorted:
        data = data.sort_values()
    plt.barh(data.index, data, color=color)
    plt.xlabel(x_name)
    plt.title(title)
    plt.yticks(fontsize=font_size)
    plt.show()

def make_scatter(data: pd.Series, title: str = "Untitled", x_name: str = "x",
              sorted: bool = True, color: typing.Union[tuple, str] = (.1, 1, .1)):
    print("Scatter")
    data = data.astype(dtype="float")
    if sorted:
        data = data.sort_values()
    

if __name__ == "__main__":
    pass