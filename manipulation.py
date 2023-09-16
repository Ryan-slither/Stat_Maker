

def make_bar(data: pd.Series, title: str = "Untitled", x_name: str = "x", font_size: int = 5, opacity: float = .5,
             sorted: bool = True, color: typing.Union[tuple, str] = (.1, .3, .7)):
    print("Histogram")
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

def make_scatter(data_x: pd.Series, data_y: pd.Series, title: str = "Untitled", x_name: str = 'x', font_size: int = 4,
                 y_name: str = 'y', sorted: bool = True, reg_line: bool = True, point_opacity: float = .5, line_opacity: float = .5,
                 point_color: typing.Union[tuple, str] = (.1, .3, .7), line_color: typing.Union[tuple, str] = (0, 0, 0)):
    print("Scatter")
    if len(data_x) > len(data_y):
        data_x = data_x[data_y.index]
    else:
        data_y = data_y.loc[data_x.index]
    data_x, data_y = data_x.astype(dtype="float"), data_y.astype(dtype="float")
    if sorted:
        data_x, data_y = data_x.sort_values(), data_y.sort_values()
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