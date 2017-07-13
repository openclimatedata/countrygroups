# Asia-Pacific Group

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

import pandas as pd
from util import to_code, root


countries = """Afghanistan
Bahrain
Bangladesh
Bhutan
Brunei Darussalam
Cambodia
China
Cyprus
Democratic People's Republic of Korea
Fiji
India
Indonesia
Iran (Islamic Republic of)
Iraq
Japan
Jordan
Kazakhstan
Kiribati
Kuwait
Kyrgyzstan
Lao People's Republic
Lebanon
Malaysia
Maldives
Marshall Islands
Micronesia (Federated States of)
Mongolia
Myanmar
Nauru
Nepal
Oman
Pakistan
Palau
Papua New Guinea
Philippines
Qatar
Republic of Korea
Samoa
Saudi Arabia
Singapore
Solomon Islands
Sri Lanka
Syrian Arab Republic
Tajikistan
Thailand
Timor-Leste
Tonga
Turkey
Turkmenistan
Tuvalu
United Arab Emirates
Uzbekistan
Vanuatu
Vietnam
Yemen""".splitlines()

index = [to_code(country) for country in countries]
asia_pacific = pd. DataFrame({"Name": countries}, index=index)
asia_pacific.index.name = "Code"

asia_pacific.to_csv(root / "data/asia-pacific-group.csv")

assert len(asia_pacific) == 55
