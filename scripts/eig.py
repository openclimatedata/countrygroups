# Environmental Integrity Group (EIG)

# http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php

import pandas as pd
from util import to_code, root


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

eig.to_csv(root / "data/eig.csv")

assert len(eig) == 5
