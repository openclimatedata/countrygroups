# OECD members

import pandas as pd

from shortcountrynames import to_name
from util import to_code, root


url = ("http://www.oecd.org/about/membersandpartners/"
       "list-oecd-member-countries.htm")

oecd = pd.read_html(url)[1]

oecd = oecd.iloc[1:-1, 1:3]

oecd.columns = ["Name", "Ratification"]

oecd.index = oecd.Name.apply(to_code)
oecd.index.name = "Code"

oecd.Name = [to_name(code) for code in oecd.index]

oecd.Ratification = pd.to_datetime(oecd.Ratification)

oecd.to_csv(root / "data/oecd.csv")

assert len(oecd) == 36
assert len(oecd.index.unique()) == len(oecd)
assert len(oecd.Name.unique()) == len(oecd)
