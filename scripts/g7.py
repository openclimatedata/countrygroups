# G20

import os

import pandas as pd

from util import to_code

path = os.path.dirname(os.path.realpath(__file__))

# https://en.wikipedia.org/wiki/G7
members = """Canada
France
Germany
Italy
Japan
United Kingdom
United States
European Union
"""

g7 = []

for member in members.splitlines():
  g7.append((to_code(member), member))

df = pd.DataFrame(g7, columns=["Code", "Name"])

assert len(df) == 7 + 1  # plus EU
assert all(df.Code.unique())
assert all(df.Name.unique())

df.to_csv(os.path.join(path, "../data/g7.csv"), index=False)
