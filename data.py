import pandas as pd
import typing

# Formatting of population data
population = pd.read_csv("./pop_chg20-22.csv")[["NAME", "ESTIMATESBASE2020", "PPOPCHG_2020", "PPOPCHG_2021", "PPOPCHG_2022"]]
population = population.set_index("NAME").astype("float")

# Formatting of gdp and economy data
gdp = pd.read_csv("./gdp_economy.csv")[["GeoName", "Description", "2020", "2021", "2022"]]
gdp = gdp[gdp["Description"].str.contains("dollar GDP")].set_index("GeoName").drop(["Description"], axis=1).astype("float")

# Formatting of crime data
# Arrests per 100,000 residents
crime = pd.read_csv("./crime_1973.csv").rename({"Unnamed: 0": "State"}, axis=1).set_index("State")

def change_in_data(data: pd.DataFrame, col1: str, col2: str):
    data[f"change_{col1}-{col2}"] = pd.Series((data[col2] - data[col1]) / data[col2])

if __name__ == "__main__":
    print(gdp.to_markdown())