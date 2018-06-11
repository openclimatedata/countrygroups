# International Maritime Organization

import pandas as pd
import requests

from lxml import etree, html
from util import root, to_code
from shortcountrynames import to_name


url = "http://www.imo.org/en/About/Membership/Pages/MemberStates.aspx"

url = ("https://treaties.un.org/pages/ViewDetails.aspx?"
       "src=TREATY&mtdsg_no=XII-1&chapter=12&clang=_en")

page = requests.get(url)
tree = html.fromstring(page.content)

member_states = tree.xpath('//table[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_tblgrid"]')
table = member_states[0]
df = pd.read_html(etree.tostring(table), skiprows=1)[0]

df = df.rename(columns={0: "Name", 2: "Date"})
df = df.drop(1, axis=1)

df.index = df["Name"].apply(to_code)
df.index.name = "Code"
df.Name = [to_name(i) for i in df.index]

def parse_date(datestring):
    datestring = datestring.rsplit(" ", 1)[0]
    return pd.to_datetime(datestring)

df.Date = df.Date.apply(parse_date)

assert len(df) == 174

df.to_csv(root / "data/imo.csv")
