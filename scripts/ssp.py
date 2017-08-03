# SSP regions

# https://tntcat.iiasa.ac.at/SspDb/dsd?Action=htmlpage&page=about

import pandas as pd
from shortcountrynames import to_name
from util import root, to_code

# Aggregation on the five region level.

# R5.2OECD = Includes the OECD 90 and EU member states and candidates.
oecd = """Albania, Australia, Austria, Belgium, Bosnia and Herzegovina,
Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland,
France, Germany, Greece, Guam, Hungary, Iceland, Ireland, Italy, Japan, Latvia,
Lithuania, Luxembourg, Malta, Montenegro, Netherlands, New Zealand, Norway,
Poland, Portugal, Puerto Rico, Romania, Serbia, Slovakia, Slovenia, Spain,
Sweden, Switzerland, The former Yugoslav Republic of Macedonia, Turkey,
United Kingdom, United States of America""".replace("\n", " ").split(", ")

# R5.2REF = Countries from the Reforming Economies of Eastern Europe and the
# Former Soviet Union.
ref = """Armenia, Azerbaijan, Belarus, Georgia, Kazakhstan, Kyrgyzstan,
Republic of Moldova, Russian Federation, Tajikistan, Turkmenistan, Ukraine,
Uzbekistan""".replace("\n", " ").split(", ")

# R5.2ASIA = The region includes most Asian countries with the exception of the
# Middle #East, Japan and Former Soviet Union states.
# China is incl. Hong Kong and Macao, excl. Taiwan
asia = """Afghanistan, Bangladesh, Bhutan, Brunei Darussalam, Cambodia, China,
Hong Kong, Macao, Democratic People's Republic of Korea, Fiji,
French Polynesia, India, Indonesia, Lao People's Democratic Republic, Malaysia,
Maldives, Micronesia (Fed. States of), Mongolia, Myanmar, Nepal, New Caledonia,
Pakistan, Papua New Guinea, Philippines, Republic of Korea, Samoa, Singapore,
Solomon Islands, Sri Lanka, Taiwan, Thailand, Timor-Leste, Vanuatu,
Viet Nam""".replace("\n", " ").split(", ")

# R5.2MAF = This region includes the countries of the Middle East and Africa.
maf = """Algeria, Angola, Bahrain, Benin, Botswana, Burkina Faso, Burundi,
Cameroon, Cape Verde, Central African Republic, Chad, Comoros, Congo,
Côte d`Ivoire, Democratic Republic of the Congo, Djibouti, Egypt,
Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea,
Guinea-Bissau, Iran (Islamic Republic of), Iraq, Israel, Jordan, Kenya,
Kuwait, Lebanon, Lesotho, Liberia, Libyan Arab Jamahiriya, Madagascar, Malawi,
Mali, Mauritania, Mauritius, Mayotte, Morocco, Mozambique, Namibia, Niger,
Nigeria, Occupied Palestinian Territory, Oman, Qatar, Rwanda, Réunion,
Saudi Arabia, Senegal, Sierra Leone, Somalia, South Africa, South Sudan,
Sudan, Swaziland, Syrian Arab Republic, Togo, Tunisia, Uganda,
United Arab Emirates, United Republic of Tanzania, Western Sahara, Yemen,
Zambia, Zimbabwe""".replace("\n", " ").split(", ")

# R5.2LAM = This region includes the countries of Latin America and the
# Caribbean.
lam = """Argentina, Aruba, Bahamas, Barbados, Belize,
Bolivia (Plurinational State of), Brazil, Chile, Colombia, Costa Rica, Cuba,
Dominican Republic, Ecuador, El Salvador, French Guiana, Grenada, Guadeloupe,
Guatemala, Guyana, Haiti, Honduras, Jamaica, Martinique, Mexico, Nicaragua,
Panama, Paraguay, Peru, Suriname, Trinidad and Tobago,
United States Virgin Islands, Uruguay,
Venezuela (Bolivarian Republic of)""".replace("\n", " ").split(", ")

oecd = [(to_code(name), name, "OECD") for name in oecd]
ref = [(to_code(name), name, "REF") for name in ref]
asia = [(to_code(name), name, "ASIA") for name in asia]
maf = [(to_code(name), name, "MAF") for name in maf]
lam = [(to_code(name), name, "LAM") for name in lam]

countries = oecd + ref + asia + maf + lam

df = pd.DataFrame(countries, columns=["Code", "Name", "Region"])
df = df.set_index("Code")
df.Name = [to_name(code) for code in df.index]

df.to_csv(root / "data/ssp.csv")
