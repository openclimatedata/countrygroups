# Small Island Developing States Non-UN or Associates

from util import to_csv


# From https://sustainabledevelopment.un.org/topics/sids/list
non_un_or_associates = """American Samoa
Anguilla
Aruba
Bermuda
British Virgin Islands
Cayman Islands
Commonwealth of Northern Marianas
Cook Islands
Curacao
French Polynesia
Guadeloupe
Guam
Martinique
Montserrat
New Caledonia
Niue
Puerto Rico
Sint Maarten
Turks and Caicos Islands
U.S. Virgin Islands"""

non_un = to_csv(
    non_un_or_associates,
    "sids-non-un-or-regional-commissions-associates.csv"
)

assert len(non_un) == 20
assert len(non_un.index.unique()) == len(non_un)
assert len(non_un.Name.unique()) == len(non_un)
