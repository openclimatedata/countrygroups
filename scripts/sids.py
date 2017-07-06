# Small Island Developing States

import os

import pandas as pd

from util import to_code, to_short_name


path = os.path.dirname(os.path.realpath(__file__))

# From https://sustainabledevelopment.un.org/topics/sids/list

aims = """Cabo Verde
Comoros
Guinea-Bissau
Maldives
Mauritius
Sao Tomé and Principe
Seychelles
Singapore
"""

caribbean = """Antigua and Barbuda
Bahamas
Barbados
Belize
Cuba
Dominica
Dominican Republic
Grenada
Guyana
Haiti
Jamaica
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Suriname
Trinidad and Tobago"""

pacific = """Fiji
Kiribati
Marshall Islands
Micronesia (Federated States of)
Nauru
Palau
Papua New Guinea
Samoa
Solomon Islands
Timor-Leste
Tonga
Tuvalu
Vanuatu"""

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

sids = []

for party in aims.splitlines():
    code = to_code(party)
    name = to_short_name(code)
    sids.append((code, name,
        "Atlantic, Indian Ocean, Mediterranean and South China Sea (AIMS) "))

for party in caribbean.splitlines():
    code = to_code(party)
    name = to_short_name(code)
    sids.append((code, name, "Caribbean"))

for party in pacific.splitlines():
    code = to_code(party)
    name = to_short_name(code)
    sids.append((code, name, "Pacific"))

non_un = []

for party in non_un_or_associates.splitlines():
    code = to_code(party)
    try:
        name = to_short_name(code)
    except KeyError:
        name = party
    non_un.append((code, name))

sids_df = pd.DataFrame(sids, columns=["Code", "Name", "Region"])
non_un_df = pd.DataFrame(non_un, columns=["Code", "Name"])

assert len(sids_df) == 37
assert len(sids_df.Code.unique()) == len(sids_df)
assert len(sids_df.Name.unique()) == len(sids_df)

assert len(non_un_df) == 20
assert len(non_un_df.Code.unique()) == len(non_un_df)
assert len(non_un_df.Name.unique()) == len(non_un_df)

sids_df.to_csv(os.path.join(path, "../data/sids.csv"), index=False)
non_un_df.to_csv(os.path.join(path, "../data/sids-non-un-or-regional-commissions-associates.csv"), index=False)
