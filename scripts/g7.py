# G7

from util import to_csv

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

g7 = to_csv(members, "g7.csv")

assert len(g7) == 7 + 1  # plus EU
assert all(g7.index.unique())
assert all(g7.Name.unique())
