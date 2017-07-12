# Small Island Developing States Non-UN or Associates

import os

import pandas as pd

from util import to_code, to_short_name


path = os.path.dirname(os.path.realpath(__file__))

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

non_un = []

for party in non_un_or_associates.splitlines():
    code = to_code(party)
    try:
        name = to_short_name(code)
    except KeyError:
        name = party
    non_un.append((code, name))

non_un_df = pd.DataFrame(non_un, columns=["Code", "Name"])

assert len(non_un_df) == 20
assert len(non_un_df.Code.unique()) == len(non_un_df)
assert len(non_un_df.Name.unique()) == len(non_un_df)

non_un_df.to_csv(os.path.join(path, "../data/sids-non-un-or-regional-commissions-associates.csv"), index=False)
