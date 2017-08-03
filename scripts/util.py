import pandas as pd

from pathlib import Path
from countrynames import to_alpha_3
from pycountry import countries


root = Path(__file__).parents[1]


def to_code(name):
    if name.lower() == "european union":
        return "EUU"
    elif name.lower().startswith("united kingdom of great"):
        return "GBR"
    else:
        return to_alpha_3(name, fuzzy=True)


def to_csv(list_or_str, csvname):
    """
    Converts a list or a string with newline delimited countries to a CSV file
    in `data`.
    """
    if isinstance(list_or_str, str):
        countries = list_or_str.splitlines()
    else:
        countries = list_or_str
    index = [to_code(country) for country in countries]
    df = pd. DataFrame({"Name": countries}, index=index)
    df.index.name = "Code"

    df.to_csv(root / "data" / csvname)
    return df
