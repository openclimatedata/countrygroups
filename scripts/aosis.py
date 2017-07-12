# AOSIS

import pandas as pd
from util import to_code, root


countries = [
    "Antigua and Barbuda",
    "Bahamas",
    "Barbados",
    "Belize",
    "Cape Verde",
    "Comoros",
    "Cook Islands",
    "Cuba",
    "Dominica",
    "Dominican Republic",
    "Fiji",
    "Federated States of Micronesia",
    "Grenada",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Jamaica",
    "Kiribati",
    "Maldives",
    "Marshall Islands",
    "Mauritius",
    "Nauru",
    "Niue",
    "Palau",
    "Papua New Guinea",
    "Samoa",
    "Singapore",
    "Seychelles",
    "Sao Tome and Principe",
    "Solomon Islands",
    "St. Kitts and Nevis",
    "St. Lucia",
    "St. Vincent and the Grenadines",
    "Suriname",
    "Timor-Leste",
    "Tonga",
    "Trinidad and Tobago",
    "Tuvalu",
    "Vanuatu"
]

# Observers:
# American Samoa
# Netherlands Antilles
# Guam
# U.S. Virgin Islands
# Puerto Rico


index = [to_code(country) for country in countries]
aosis = pd. DataFrame({"Name": countries}, index=index)
aosis.index.name = "Code"

aosis.to_csv(root / "data/aosis.csv")

assert len(aosis) == 44 - 5  # 44 States and observers
