# AR5 Region definitons
# https://tntcat.iiasa.ac.at/SspDb/dsd?Action=htmlpage&page=about#v2

import pandas as pd

from shortcountrynames import to_name
from util import root, to_code

# R32ANUZ = This region includes Australia and New Zealand.
anuz = """Australia, New Zealand"""

# R32BRA = Brazil. 
bra = """Brazil"""

# R32CAN = Canada.
can = """Canada"""

# R32CAS = This region includes the countries of Central Asia.
cas = """Armenia, Azerbaijan, Georgia, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan"""

# R32CHN = China (Mainland, Hongkong, Macao; excl. Taiwan)
chn = """China, China, Hong Kong SAR, China, Macao SAR"""

# R32EEU = Eastern Europe (excl. former Soviet Union and EU member states).
eeu = """Albania, Bosnia & Herzegovina, Croatia, Montenegro, Serbia, Macedonia"""

# R32EEU-FSU = Eastern Europe, former Soviet Union (excl. Russia and EU members)
eeufsu = """Belarus, Republic of Moldova, Ukraine"""

# R32EFTA = This region includes Iceland, Norway, Switzerland
efta = """Iceland, Norway, Switzerland"""

# R32EU12-H = New EU member states that joined as of 2004 - high income.
eu12h = """Cyprus, Czech Republic, Estonia, Hungary, Malta, Poland, Slovakia, Slovenia"""

# R32EU12-M = New EU member states that joined as of 2004 - medium income.
eu12m = """Bulgaria, Latvia, Lithuania, Romania"""

# R32EU15 = This region includes European Union member states that joined prior to 2004.
eu15 = """Austria, Belgium, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, United Kingdom"""

# R32IDN = Indonesia
idn = """Indonesia"""

# R32IND = India
ind = """India"""

# R32JPN = Japan
jpn = """Japan"""

# R32KOR = Republic of Korea
kor = """South Korea"""

# R32LAM-L = This region includes the countries of Latin America (excl. Brazil, Mexico) - low income
laml = """Belize, Guatemala, Haiti, Honduras, Nicaragua"""

# R32LAM-M = This region includes the countries of Latin America (excl. Brazil, Mexico) - medium and high income.
lamm = """Antigua & Barbuda, Argentina, Bahamas, Barbados, Bermuda, Bolivia (Plurinational State of), Chile, Colombia, Costa Rica, Cuba, Dominica, Dominican Republic, Ecuador, El Salvador, French Guiana, Grenada, Guadeloupe, Guyana, Jamaica, Martinique, Netherlands Antilles, Panama, Paraguay, Peru, Saint Kitts & Nevis, Saint Lucia, Saint Vincent & the Grenadines, Suriname, Trinidad & Tobago, Uruguay, Venezuela"""

# R32MEA-H = This region includes the countries of Middle East Asia - high income.
meah = """Bahrain, Israel, Kuwait, Oman, Qatar, Saudi Arabia, United Arab Emirates"""

# R32MEA-M = This region includes the countries of Middle East Asia - low and medium income.
meam = """Iran, Iraq, Jordan, Lebanon, Palestine, Syria, Yemen"""

# R32MEX = Mexico
mex = """Mexico"""

# R32NAF = This region includes the countries of North Africa.
naf = """Algeria, Egypt, Libyan Arab Jamahiriya, Morocco, Tunisia, Western Sahara"""

# R32OAS-CPA = This region includes the countries of Other Asia - former Centrally Planned Asia.
oascpa = """Cambodia, Laos, Mongolia, Viet Nam"""

# R32OAS-L = This region includes the countries of Other Asia - low income.
oasl = """Bangladesh, North Korea, Fiji, Micronesia, Myanmar, Nepal, Papua New Guinea, Philippines, Samoa, Solomon Islands, Timor-Leste, Tonga, Vanuatu"""

# R32OAS-M = This region includes the countries of Other Asia - medium and high income.
oasm = """Bhutan, Brunei Darussalam, French Polynesia, Guam, Malaysia, Maldives, New Caledonia, Singapore, Sri Lanka, Thailand"""

# R32PAK = Pakistan, Afghanistan
pak = """Pakistan, Afghanistan"""

# R32RUS = Russia
rus = """Russia"""

# R32SAF = South Africa
saf = """South Africa"""

# R32SSA-L = This region includes the countries of Subsahara Africa (excl. South Africa) - low income.
ssal = """Benin, Burkina Faso, Burundi, Cameroon, Cape Verde, Central African Republic, Chad, Comoros, Congo, Côte d`Ivoire, Democratic Republic of the Congo, Djibouti, Eritrea, Ethiopia, Gambia, Ghana, Guinea, Guinea-Bissau, Kenya, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mozambique, Niger, Nigeria, Rwanda, Sao Tome and Principe, Senegal, Sierra Leone, Somalia, South Sudan, Sudan, Swaziland, Togo, Uganda, United Republic of Tanzania, Zambia, Zimbabwe"""

# R32SSA-M = This region includes the countries of Subsahara Africa (excl. South Africa) - medium and high income.
ssam = """Angola, Botswana, Equatorial Guinea, Gabon, Mauritius, Mayotte, Namibia, Réunion, Seychelles"""

# R32TUR = Turkey
tur = """Turkey"""

# R32TWN = Taiwan
twn = """Taiwan"""

# R32USA = United States of America. Includes:
usa = """Puerto Rico, United States Virgin Islands, United States of America """


ar32 = {"anuz" : anuz, "bra" : bra, "can" : can, "cas" : cas, "chn" : chn, "eeu" : eeu, "eeu-fsu" : eeufsu, "efta" : efta, "eu12-h" : eu12h, "eu12-m" : eu12m, "eu15" : eu15, "idn" : idn, "ind" : ind, "jpn" : jpn, "kor" : kor, "lam-l" : laml, "lam-m" : lamm, "mea-h" : meah, "mea-m" : meam, "mex" : mex, "naf" : naf, "oas-cpa" : oascpa, "oas-l" : oasl, "oas-m" : oasm, "pak" : pak, "rus" : rus, "saf" : saf, "ssa-l" : ssal, "ssa-m" : ssam, "tur" : tur, "twn" : twn, "usa" : usa} 

records = []
for key, countries in ar32.items():
    items = [(to_code(name), name, key.upper())
             for name in countries.replace("\n", " ").split(", ")]
    records = records + items

df = pd.DataFrame(records, columns=["Code", "Name", "Region"])
df = df.set_index("Code")
df.Name = [to_name(code) if len(code) == 3 else df.loc[code].Name
           for code in df.index]
df = df.sort_values(["Region", "Name"])
df.to_csv(root / "data/ar32.csv")
