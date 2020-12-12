# OECD members

import pandas as pd

import requests

from lxml import etree, html
from util import root, to_code
from shortcountrynames import to_name

url = "http://www.oecd.org/about/members-and-partners/"

page = requests.get(url)
tree = html.fromstring(page.content)

members = tree.xpath('//div[@id="members"]')[0]

name_year = []

for member in members.xpath('.//div[@class="country-list__row"]'):
    name = member.xpath(".//a[@class='country-list__country']")[0].text
    year_div = member.xpath(".//div[@class='country-list__year']")[0]
    year = list(year_div.itertext())[-1].strip()
    name_year.append((name, year))

oecd = pd.DataFrame.from_records(name_year)

oecd.columns = ["Name", "Accession"]
oecd["Code"] = oecd.Name.apply(to_code)
oecd = oecd[['Code','Name', "Accession"]]

assert len(oecd) == 37
assert len(oecd.index.unique()) == len(oecd)
assert len(oecd.Name.unique()) == len(oecd)

oecd.to_csv(root / "data/oecd.csv", index=False)
