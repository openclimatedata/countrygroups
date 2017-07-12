# Graduated from LDCs

import pandas as pd
from countrynames import to_alpha_3
from util import root


# From Factsheets linked at
# https://www.un.org/development/desa/dpad/
# least-developed-country-category/ldcs-at-a-glance.html
graduated = [
    ("Botswana", 1971, 1994),
    ("Maldives", 1971, 2011),
    ("Cabo Verde", 1977, 2007),
    ("Samoa", 1971, 2014),
    ("Equatorial Guinea", 1982, 2017),
]

grad_df = pd.DataFrame(
    graduated,
    columns=["Name", "Year-Of-Inclusion", "Graduation"]
)
grad_df.index = grad_df.Name.apply(to_alpha_3)
grad_df.index.name = "Code"

grad_df.to_csv(root / "data/graduated-ldcs.csv")
