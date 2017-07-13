# Arab Group

# http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php

import os
import pandas as pd
from util import to_code


path = os.path.dirname(os.path.realpath(__file__))

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

index = [to_code(country) for country in countries]
arabgroup = pd. DataFrame({"Name": countries}, index=index)
arabgroup.index.name = "Code"

arabgroup.to_csv(os.path.join(path, "../data/arab-group.csv"))

assert len(arabgroup) == 22
