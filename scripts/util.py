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
        return to_alpha_3(name)


def to_short_name(code):
    if code == "EUU":
        return "European Union"
    else:
        return countries.get(alpha_3=code).name
