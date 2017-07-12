# G20

import pandas as pd

from util import to_code, root

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

df.to_csv(root /  "data/g7.csv", index=False)
