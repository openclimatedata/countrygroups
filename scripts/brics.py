# BRICS


from util import to_csv

countries = ["Brazil", "Russian Federation", "India", "China", "South Africa"]

brics = to_csv(countries, "brics.csv")

assert len(brics) == 5
assert len(brics.index.unique()) == len(brics)
assert len(brics.Name.unique()) == len(brics)
