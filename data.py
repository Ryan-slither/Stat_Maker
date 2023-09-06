import pandas as pd

#Formatting of population data
population = pd.read_csv("./pop_chg20-22.csv")[["NAME", "ESTIMATESBASE2020", "PPOPCHG_2020", "PPOPCHG_2021", "PPOPCHG_2022"]]
population = population.set_index("NAME")

#Formatting of gdp and economy data
gdp = pd.read_csv("./gdp_economy.csv")[["GeoName", "Description", "2020", "2021", "2022"]]
gdp = gdp[gdp["Description"].str.contains("dollar GDP")].set_index("GeoName")

if __name__ == "__main__":
    pass