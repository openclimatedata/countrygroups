# G20

from util import to_csv

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
United States"""

g20 = to_csv(members, "g20.csv")

assert len(g20) == 20
assert all(g20.index.unique())
assert all(g20.Name.unique())
