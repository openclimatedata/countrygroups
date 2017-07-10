# Umbrella group

import os
import pandas as pd
from util import to_code


path = os.path.dirname(os.path.realpath(__file__))

# "The Umbrella Group is a loose coalition of non-EU developed countries
# which formed following the adoption of the Kyoto Protocol. Although there is
# no formal list, the Group is usually made up of [...]"

# http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php

countries = [
    "Australia",
    "Canada",
    "Japan",
    "Kazakhstan",
    "New Zealand",
    "Norway",
    "Russian Federation",
    "Ukraine",
    "United States"
]

index = [to_code(country) for country in countries]
umbrella = pd. DataFrame({"Name": countries}, index=index)
umbrella.index.name = "Code"

umbrella.to_csv(os.path.join(path, "../data/umbrella.csv"))
