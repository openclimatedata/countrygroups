# LDCs

import os

import pandas as pd
from countrynames import to_alpha_3, to_name


path = os.path.dirname(os.path.realpath(__file__))

# Copied from
# https://www.un.org/development/desa/dpad/wp-content/uploads/
# sites/45/publication/ldc_list.pdf
ldc_string = """Afghanistan (1971)
Angola (1994)
Bangladesh (1975)
Benin (1971)
Bhutan (1971)
Burkina Faso (1971)
Burundi   (1971)
Cambodia (1991)
Central African Republic (1975)
Chad (1971)
Comoros (1977)
Democratic Republic of the Congo (1991)
Djibouti (1982)
Eritrea (1994)
Ethiopia (1971)
Gambia (1975)
Guinea   (1971)
Guinea-Bissau   (1981)
Haiti (1971)
Kiribati (1986)
Lao People’s Democratic Republic (1971)
Lesotho   (1971)
Liberia (1990)
Madagascar (1991)
Malawi   (1971)
Mali   (1971)
Mauritania (1986)
Mozambique (1988)
Myanmar (1987)
Nepal   (1971)
Niger   (1971)
Rwanda (1971)
Sao Tome and Principe (1982)
Senegal (2000)
Sierra Leone (1982)
Solomon Islands (1991)
Somalia (1971)
South Sudan (2012)
Sudan   (1971)
Timor-Leste (2003)
Togo (1982)
Tuvalu (1986)
Uganda (1971)
United Republic of Tanzania (1971)
Vanuatu (1985)
Yemen (1971)
Zambia (1991)
"""

ldcs = []

for line in ldc_string.splitlines():
    name, inclusion = line.split("(")
    name = name.strip()
    inclusion = inclusion[:-1]
    code = to_alpha_3(name)
    iso_name = to_name(code)
    ldcs.append((code, iso_name, inclusion))

df = pd.DataFrame(ldcs, columns=["Code", "Name", "Year-Of-Inclusion"])
df = df.sort_values("Name")
df.to_csv(os.path.join(path, "../data/ldcs.csv"), index=False)
