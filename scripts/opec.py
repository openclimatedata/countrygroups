# OPEC countries

from util import to_csv


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

opec = to_csv(countries, "opec.csv")

assert len(opec) == 14
