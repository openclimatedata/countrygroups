# Small Island Developing States

import pandas as pd

from util import to_code, to_short_name, root


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

sids_df = pd.DataFrame(sids, columns=["Code", "Name", "Region"])

assert len(sids_df) == 37
assert len(sids_df.Code.unique()) == len(sids_df)
assert len(sids_df.Name.unique()) == len(sids_df)

sids_df.to_csv(root / "data/sids.csv", index=False)
