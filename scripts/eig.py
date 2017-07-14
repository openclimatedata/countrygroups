# Environmental Integrity Group (EIG)

# http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php

from util import to_csv


countries = [
    "Mexico",
    "Liechtenstein",
    "Monaco",
    "Republic of Korea",
    "Switzerland"
]

eig = to_csv(countries, "eig.csv")

assert len(eig) == 5
