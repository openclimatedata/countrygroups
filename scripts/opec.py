# OPEC countries

import pandas as pd
from util import to_code, root


# http://www.opec.org/opec_web/en/about_us/25.htm
countries = [
 "Algeria",
 "Angola",
 "Ecuador",
 "Equatorial Guinea",
 "Gabon",
 "Iran",
 "Iraq",
 "Kuwait",
 "Libya",
 "Nigeria",
 "Qatar",
 "Saudi Arabia",
 "United Arab Emirates",
 "Venezuela"
]

index = [to_code(country) for country in countries]
opec = pd. DataFrame({"Name": countries}, index=index)
opec.index.name = "Code"

opec.to_csv(root / "data/opec.csv")

assert len(opec) == 14
