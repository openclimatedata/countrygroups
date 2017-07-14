# Umbrella group

from util import to_csv


# http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php
# "The Umbrella Group is a loose coalition of non-EU developed countries
# which formed following the adoption of the Kyoto Protocol. Although there is
# no formal list, the Group is usually made up of [...]"

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

to_csv(countries, "umbrella.csv")
