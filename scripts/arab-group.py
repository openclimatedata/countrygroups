# Arab Group

# http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php

from util import to_csv


countries = [
    "Algeria",
    "Bahrain",
    "Comoros",
    "Djibouti",
    "Egypt",
    "Iraq",
    "Jordan",
    "Kuwait",
    "Lebanon",
    "Libya",
    "Morocco",
    "Mauritania",
    "Oman",
    "Palestine",
    "Qatar",
    "Saudi Arabia",
    "Somalia",
    "Sudan",
    "Syria",
    "Tunisia",
    "United Arab Emirates",
    "Yemen"
]

arabgroup = to_csv(countries, "arab-group.csv")

assert len(arabgroup) == 22
