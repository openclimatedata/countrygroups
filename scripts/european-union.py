# European Union Member States

import pandas as pd
import requests

from countrynames import to_alpha_3, to_name
from lxml import html
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

df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0))
df = df.rename(columns={"Countries": "Name", "Year of entry": "Member-Since"})
df.index = df["Name"].apply(to_alpha_3)
df.index.name = "Code"

df["Member-Since"] = df["Member-Since"].fillna(method="ffill")
df["Member-Since"] = pd.to_datetime(df["Member-Since"], dayfirst=True)

df = df[["Name", "Member-Since"]]

df = df.sort_values("Name")

assert len(df) == 28

# Normalize names to ISO standard.
df.Name = [to_name(i) for i in df.index]

df.to_csv(root / "data/european-union.csv")
