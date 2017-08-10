# AR5 Region definitons
# https://tntcat.iiasa.ac.at/AR5DB/dsd?Action=htmlpage&page=about

import pandas as pd

from shortcountrynames import to_name
from util import root, to_code

# OECD1990 = This region includes the OECD countries in 1990.
# Channel Islands was replaced with "Guernsey" and "Jersey"
oecd1990 = """Guernsey, Jersey, Aland Islands, Andorra, Australia, Austria,
Belgium, Canada, Denmark, Faroe Islands, Finland, France, Germany,
Gibraltar, Greece, Greenland, Guam, Guernsey,
Holy See (Vatican City State), Iceland, Ireland, Isle of Man, Italy,
Japan, Jersey, Liechtenstein, Luxembourg, Monaco, Netherlands,
New Zealand, Norway, Portugal, Saint Pierre and Miquelon, San Marino,
Spain, Svalbard and Jan Mayen, Sweden, Switzerland, Turkey,
United Kingdom, United States"""

# EIT = Economies in Transition. This region is sometimes also referred to as
# Reforming Ecomonies of Eastern Europe and the Former Soviet Union (REF).
# "Serbia and Montenegro" was removed from the list, both are included
# separately.
eit = """Albania, Armenia, Azerbaijan, Belarus, Bosnia and Herzegovina,
Bulgaria, Croatia, Cyprus, Czech Republic, Estonia, Georgia, Hungary,
Kazakhstan, Kyrgyzstan, Latvia, Lithuania, Macedonia, Malta,
Moldova (Republic of), Montenegro, Poland, Romania, Russian Federation,
Serbia, Slovakia, Slovenia, Tajikistan,
Turkmenistan, Ukraine, Uzbekistan"""

# ASIA = Non-OECD ASIA. The region includes most Asian countries with the
# exception of the Middle East, Japan and Former Soviet Union states.
asia = """Afghanistan, American Samoa, Bangladesh, Bhutan,
British Indian Ocean Territory, Brunei Darussalam, Cambodia, China,
Christmas Island, Cocos (Keeling) Islands, Cook Islands, Fiji,
French Polynesia, Heard Island and McDonald Islands, India, Indonesia,
Kiribati, Korea (Democratic People's Republic of),
Laos (People's Democratic Republic), Malaysia, Maldives, Marshall Islands,
Micronesia (Federated States of), Mongolia, Myanmar, Nauru, Nepal,
New Caledonia, Niue, Norfolk Island, Northern Mariana Islands, Pakistan,
Palau, Papua New Guinea, Philippines, Pitcairn, Samoa, Singapore,
Solomon Islands, South Korea, Sri Lanka, Thailand, Timor-Leste, Tokelau,
Tonga, Tuvalu, US Minor Outlying Islands, Vanuatu, Viet Nam,
Wallis and Futuna"""

# MAF = This region includes the countries of the Middle East and Africa.
maf = """Algeria, Angola, Bahrain, Benin, Botswana, Burkina Faso, Burundi,
Cameroon, Cape Verde, Central African Republic, Chad, Comoros, Congo,
Congo (The Democratic Republic of the), Cote d'Ivoire, Djibouti, Egypt,
Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea,
Guinea-Bissau, Iran, Iraq, Israel, Jordan, Kenya, Kuwait, Lebanon, Lesotho,
Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Mayotte,
Morocco, Mozambique, Namibia, Niger, Nigeria, Oman, Palestinian Territory,
Qatar, Reunion, Rwanda, Saint Helena, Sao Tome and Principe, Saudi Arabia,
Senegal, Seychelles, Sierra Leone, Somalia, South Africa, South Sudan,
Sudan, Swaziland, Syrian Arab Republic, Tanzania, Togo, Tunisia, Uganda,
United Arab Emirates, Western Sahara, Yemen, Zambia, Zimbabwe"""

# LAM = This region includes the countries of Latin America and the Caribbean.
lam = """Anguilla, Antarctica, Antigua and Barbuda, Argentina, Aruba,
Bahamas, Barbados, Belize, Bermuda, Bolivia, Bouvet Island, Brazil,
British Virgin Islands, Cayman Islands, Chile, Colombia, Costa Rica, Cuba,
Curacao, Dominica, Dominican Republic, Ecuador, El Salvador,
Falkland Islands (Malvinas), French Guiana, French Southern Territories,
Grenada, Guadeloupe, Guatemala, Guyana, Haiti, Honduras, Jamaica, Martinique,
Mexico, Montserrat, Netherlands Antilles, Nicaragua, Panama, Paraguay, Peru,
Puerto Rico, Saint Kitts and Nevis, Saint Lucia,
Saint Vincent and the Grenadines, Sint Maarten,
South Georgia and the South Sandwich Islands, Suriname, Trinidad and Tobago,
Turks and Caicos Islands, Uruguay, US Virgin Islands, Venezuela"""

ar5 = {
    "oecd1990": oecd1990, "eit": eit, "asia": asia, "maf": maf, "lam": lam
}

records = []
for key, countries in ar5.items():
    items = [(to_code(name), name, key.upper())
             for name in countries.replace("\n", " ").split(", ")]
    records = records + items

df = pd.DataFrame(records, columns=["Code", "Name", "Region"])
df = df.set_index("Code")
df.Name = [to_name(code) if len(code) == 3 else df.loc[code].Name
           for code in df.index]
df = df.sort_values(["Region", "Name"])
df.to_csv(root / "data/ar5.csv")
