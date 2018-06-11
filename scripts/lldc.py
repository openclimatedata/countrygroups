# Landlocked Developing Countries (LLDCs)

import pandas as pd
from shortcountrynames import to_name
from util import root, to_code

# From http://unohrlls.org/about-lldcs/country-profiles/
lldc_string = """Botswana
Mali
Burkina Faso
Niger
Burundi
Rwanda
Central African Republic
South Sudan
Chad
Swaziland
Ethiopia
Uganda
Lesotho
Zambia
Malawi
Zimbabwe
Afghanistan
Mongolia
Bhutan
Nepal
Kazakhstan
Tajikistan
Kyrgyzstan
Turkmenistan
Lao People’s Democratic Republic
Uzbekistan
Armenia
Republic of Moldova
Azerbaijan
The Former Yugoslav Republic of Macedonia
Bolivia
Paraguay
"""

lldcs = []

for name in lldc_string.splitlines():
    code = to_code(name)
    iso_name = to_name(code)
    lldcs.append((code, iso_name))

assert len(lldcs) == 16 + 10 + 4 + 2

df = pd.DataFrame(lldcs, columns=["Code", "Name"])
df = df.sort_values("Name")
df.to_csv(root / "data/lldc.csv", index=False)
