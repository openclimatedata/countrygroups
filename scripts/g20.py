# G20

import pandas as pd

from util import to_code, root

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

df.to_csv(root / "data/g20.csv", index=False)
