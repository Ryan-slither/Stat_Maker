import manipulation
import data

if __name__ == "__main__":
    manipulation.make_bar(data.gdp["2022"], x_name="GDP (millions of current dollars)", title="GDP per State in 2022", color=(.2, .3, .4))
    manipulation.make_bar(data.population["PPOPCHG_2022"], x_name="Population (%)",title="Population Change per State (2022)")