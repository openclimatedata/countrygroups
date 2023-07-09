# Montreal Protocol Groupings

import requests
import json
from lxml import html
from util import root, to_code

# Basic A5 / nonA5 split
url = "https://ozone.unep.org/classification-parties"

page = requests.get(url)
tree = html.fromstring(page.content)


class Countries:
    def __init__(self, names):
        self.country_names = names
        self.fixup()
        self.codes = sorted([to_code(x) for x in self.country_names])

    def fixup(self):
        self.country_names = [
            x if x != "Eswatini (the Kingdom of)" else "Eswatini"
            for x in self.country_names
        ]

    def remove_subset(self, subset):
        return sorted(list(set(self.codes).difference(subset.codes)))


# None of the elements in this path have ids
lists = tree.xpath("//table//tbody//tr//td//ol")
a5_ol = lists[0]
non_a5_ol = lists[1]

a5 = Countries([x.text for x in a5_ol])
non_a5 = Countries([x.text for x in non_a5_ol])

# Deeper splits from Decision XVIII/2

# https://ozone.unep.org/treaties/montreal-protocol/meetings/twenty-eighth-meeting-parties/decisions/decision-xxviii2-decision-related-amendment-phasing-down-hydrofluorocarbons
# This is just text, too fragile to parse.
non_a5_exceptions = Countries(
    ["Belarus", "Kazakhstan", "Russian Federation", "Tajikistan", "Uzbekistan"]
)
a5_group_2 = Countries(
    [
        "Bahrain",
        "India",
        "the Islamic Republic of Iran",
        "Iraq",
        "Kuwait",
        "Oman",
        "Pakistan",
        "Qatar",
        "Saudi Arabia",
        "United Arab Emirates",
    ]
)

result = {
    "ARTICLE_5": {"GROUP_1": a5.remove_subset(a5_group_2), "GROUP_2": a5_group_2.codes},
    "NON_ARTICLE_5": {
        "NON_ARTICLE_5_MAIN_GROUP": non_a5.remove_subset(non_a5_exceptions),
        "NON_ARTICLE_5_EXCEPTIONS": non_a5_exceptions.codes,
    },
}
with open(str(root / "data/montreal_protocol_countries.json"), "w") as f:
    json.dump(result, f, indent=4, sort_keys=True)

assert len(result["ARTICLE_5"]["GROUP_1"]) + len(result["ARTICLE_5"]["GROUP_2"]) == 148
assert len(result["NON_ARTICLE_5"]["NON_ARTICLE_5_MAIN_GROUP"]) + len(result["NON_ARTICLE_5"]["NON_ARTICLE_5_EXCEPTIONS"]) == 50
