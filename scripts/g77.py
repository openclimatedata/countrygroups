# G77

# http://www.g77.org/doc/members.html

import os

import pandas as pd
import requests

from util import to_code

from lxml import html


path = os.path.dirname(os.path.realpath(__file__))

# Use print version for simpler parsing.
url = "http://www.g77.org/doc/members_print.html"

page = requests.get(url)
tree = html.fromstring(page.content)

# Remove \r\n, \t and multiple whitespace.
members = [' '.join(item.text.split()) for item in tree.xpath("//ol/li")]
members = sorted(members)

index = [to_code(memeber) for memeber in members]
g77 = pd. DataFrame({"Name": members}, index=index)
g77.index.name = "Code"

g77.to_csv(os.path.join(path, "../data/g77.csv"))

assert len(g77) == 134
