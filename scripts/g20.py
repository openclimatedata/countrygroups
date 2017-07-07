# G20

import os

import pandas as pd

from util import to_code

path = os.path.dirname(os.path.realpath(__file__))

# https://en.wikipedia.org/wiki/G20
members = """Australia
Argentina
Brazil
Canada
China
European Union
France
Germany
India
Indonesia
Italy
Japan
Mexico
Russia
Saudi Arabia
South Africa
South Korea
Turkey
United Kingdom
United States
"""

g20_list = []

for member in members.splitlines():
  g20_list.append((to_code(member), member))

df = pd.DataFrame(g20_list, columns=["Code", "Name"])

assert len(df) == 20
assert all(df.Code.unique())
assert all(df.Name.unique())

df.to_csv(os.path.join(path, "../data/g20.csv"), index=False)
