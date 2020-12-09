# European Union Member States

import pandas as pd

from shortcountrynames import to_name
from countrynames import to_code_3
from util import root


def get_date(item):
    # Get only part matching date, can be written as
    # <strong>EU member country</strong>: since 1 January 1995
    # <strong>EU member country since</strong>: 1 January 1958
    # <strong>EU member country since</strong> 1 January 1973
    return item.find(
        'p[1]').text_content().rsplit(":")[-1].rsplit(
        "since")[-1].strip().replace("\xa0", " ").replace(
        " - More information on Brexit", "")


url = "https://europa.eu/european-union/about-eu/countries_en"

df = pd.read_html(url, match="Belgium")[1]
df["Year of entry"] = df["Year of entry"].ffill()

df = df.rename(columns={"Countries": "Name", "Year of entry": "Member-Since"})
df.index = df["Name"].apply(to_code_3)
df.index.name = "Code"
df = df.reset_index().dropna().set_index("Code")

df["Member-Since"] = pd.to_datetime(df["Member-Since"], dayfirst=True)

df = df[["Name", "Member-Since"]]

df = df.sort_values("Name")

assert len(df) == 27

# Normalize names to ISO standard.
df.Name = [to_name(i) for i in df.index]

df.to_csv(root / "data/european-union.csv")
