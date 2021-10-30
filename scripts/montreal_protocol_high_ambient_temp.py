# Montreal Protocol High Ambient Temperature Exemption countries
# These are all Article 5 countries but they are split across Article 5 Group 1 and 2.


import requests
from lxml import html
from util import root, to_code
import pandas as pd

# Basic A5 / nonA5 split
url = "https://ozone.unep.org/treaties/montreal-protocol/meetings/twenty-eighth-meeting-parties/decisions/decision-xxviii2-decision-related-amendment-phasing-down-hydrofluorocarbons"

page = requests.get(url)
tree = html.fromstring(page.content)

# The list of countries is in a paragraph following a <p><strong> title
e = tree.xpath('.//p/strong[text()="Appendix II: List of countries operating under the high-ambient-temperature exemption"]')[0]
high_amb_list = [x.strip() for x in e.getparent().getnext().text.split(',')]

df = pd.DataFrame({"Code": [to_code(x) for x in high_amb_list], "Name": high_amb_list})

assert len(df) == 34

df.to_csv(root / "data/montreal_protocol_high_ambient_temp.csv")
