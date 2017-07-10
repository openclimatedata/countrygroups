# OPEC countries

import os
import pandas as pd
from util import to_code


path = os.path.dirname(os.path.realpath(__file__))

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

opec.to_csv(os.path.join(path, "../data/opec.csv"))

assert len(opec) == 14
