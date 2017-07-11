# Environmental Integrity Group (EIG)

# http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php

import os
import pandas as pd
from util import to_code


path = os.path.dirname(os.path.realpath(__file__))

countries = [
    "Mexico",
    "Liechtenstein",
    "Monaco",
    "Republic of Korea",
    "Switzerland"
]

index = [to_code(country) for country in countries]
eig = pd. DataFrame({"Name": countries}, index=index)
eig.index.name = "Code"

eig.to_csv(os.path.join(path, "../data/eig.csv"))

assert len(eig) == 5
