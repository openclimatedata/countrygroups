# OECD members

import os

import pandas as pd

from util import to_code, to_short_name

path = os.path.dirname(os.path.realpath(__file__))

url = "http://www.oecd.org/about/membersandpartners/list-oecd-member-countries.htm"

oecd = pd.read_html(url)[1]

oecd = oecd.iloc[1:-1, 1:3]

oecd.columns = ["Name", "Ratification"]

oecd.index = oecd.Name.apply(to_code)
oecd.index.name = "Code"

oecd.Name = [to_short_name(code) for code in oecd.index]

oecd.Ratification = pd.to_datetime(oecd.Ratification)

oecd.to_csv(os.path.join(path, "../data/oecd.csv"))

assert len(oecd) == 35
assert len(oecd.index.unique()) == len(oecd)
assert len(oecd.Name.unique()) == len(oecd)
