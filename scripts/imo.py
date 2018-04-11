# International Maritime Organization

import pandas as pd
import requests

from countrynames import to_alpha_3, to_name
from lxml import etree, html
from util import root


url = "http://www.imo.org/en/About/Membership/Pages/MemberStates.aspx"

page = requests.get(url)
tree = html.fromstring(page.content)

member_states = tree.xpath('//div[contains(@class, "ms-rtestate-field")]')
table = member_states[0].find("table")
df = pd.read_html(etree.tostring(table))[0]
df = df.rename(columns={0: "Name", 1: "Year"})

df = df.iloc[:173]

df["Name"] = df["Name"].apply(str.replace, args=("\u200b", ""))
df["Year"] = df["Year"].apply(str.replace, args=("\u200b", ""))


df.index = df["Name"].apply(to_alpha_3)
df.index.name = "Code"

assert len(df) == 173

df.to_csv(root / "data/imo.csv")
