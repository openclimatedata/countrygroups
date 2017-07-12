# European Union Member States

import pandas as pd
import requests

from countrynames import to_alpha_3, to_name
from lxml import html
from util import root


url = "https://europa.eu/european-union/about-eu/countries/member-countries_en"

page = requests.get(url)
tree = html.fromstring(page.content)

member_states = tree.xpath('//div[contains(@class, "member_state")]')

def get_date(item):
    # Get only part matching date, can be written as
    # <strong>EU member country</strong>: since 1 January 1995
    # <strong>EU member country since</strong>: 1 January 1958
    # <strong>EU member country since</strong> 1 January 1973
    return item.find(
        'p[1]').text_content().rsplit(":")[-1].rsplit(
        "since")[-1].strip().replace("\xa0", " ").replace(
        " - More information on Brexit", "")

members = {
    i.find('h2/a[1]').text: get_date(i) for i in member_states}

# Check if all dates start with digit.
assert all([i.split(" ")[0].isdigit() for i in members.values()])
# And end with digits.
assert all([i.split(" ")[2].isdigit() for i in members.values()])

df = pd.DataFrame.from_dict(members, orient="index").reset_index()
df.columns = ["Name", "Member since"]
df["Member since"] = pd.to_datetime(df["Member since"])
df.index = df["Name"].apply(to_alpha_3)
df.index.name = "Code"

# Normalize names to ISO standard.
df.Name = [to_name(i) for i in df.index]

df = df.sort_values("Name")

assert len(df) == 28

df.to_csv(root /  "data/european-union.csv")
