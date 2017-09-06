# UN Regional Groups
# http://www.un.org/depts/DGACM/RegionalGroups.shtml

import pandas as pd

from shortcountrynames import to_name
from util import root, to_code


# African Group
african_group = """Algeria
Angola
Benin
Botswana
Burkina Faso
Burundi
Cabo Verde
Cameroon
Central African Republic
Chad
Comoros
Congo
Côte d'Ivoire
Democratic Republic of the Congo
Djibouti
Egypt
Equatorial Guinea
Eritrea
Ethiopia
Gabon
Gambia
Ghana
Guinea
Guinea-Bissau
Kenya
Lesotho
Liberia
Libya
Madagascar
Malawi
Mali
Mauritania
Mauritius
Morocco
Mozambique
Namibia
Niger
Nigeria
Rwanda
São Tomé and Príncipe
Senegal
Seychelles
Sierra Leone
Somalia
South Africa
South Sudan
Sudan
Swaziland
Togo
Tunisia
Uganda
United Republic of Tanzania
Zambia
Zimbabwe""".splitlines()

# Asia-Pacific Group
asia_pacific = """Afghanistan
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

# Eastern European Group
eastern_european = """Albania
Armenia
Azerbaijan
Belarus
Bosnia and Herzegovina
Bulgaria
Croatia
Czech Republic
Estonia
Georgia
Hungary
Latvia
Lithuania
Montenegro
Poland
Republic of Moldova
Romania
Russian Federation
Serbia
Slovakia
Slovenia
The former Yugoslav Republic of Macedonia
Ukraine""".splitlines()

# Latin American and Caribbean Group (GRULAC)
grulac = """Antigua and Barbuda
Argentina
Bahamas
Barbados
Belize
Bolivia (Plurinational State of)
Brazil
Chile
Colombia
Costa Rica
Cuba
Dominica
Dominican Republic
Ecuador
El Salvador
Grenada
Guatemala
Guyana
Haiti
Honduras
Jamaica
Mexico
Nicaragua
Panama
Paraguay
Peru
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Suriname
Trinidad and Tobago
Uruguay
Venezuela (Bolivarian Republic of)""".splitlines()

# Western European and Others Group (WEOG)
weog = """Andorra
Australia
Austria
Belgium
Canada
Denmark
Finland
France
Germany
Greece
Iceland
Ireland
Israel
Italy
Liechtenstein
Luxembourg
Malta
Monaco
Netherlands
New Zealand
Norway
Portugal
San Marino
Spain
Sweden
Switzerland
Turkey
United Kingdom
United States of America""".splitlines()

assert len(african_group) == 54
assert len(asia_pacific) == 55
assert len(eastern_european) == 23
assert len(grulac) == 33
assert len(weog) == 29

african_group = [
    (to_code(name), name, "African Group") for name in african_group]
asia_pacific = [
    (to_code(name), name, "Asia-Pacific Group") for name in asia_pacific]
eastern_european = [
    (to_code(name), name,
     "Eastern European Group") for name in eastern_european]
grulac = [(to_code(name), name, "GRULAC") for name in grulac]
weog = [(to_code(name), name, "WEOG") for name in weog]

countries = african_group + asia_pacific + eastern_european + grulac + weog

df = pd.DataFrame(countries, columns=["Code", "Name", "Region"])
df = df.set_index("Code")
df.Name = [to_name(code) for code in df.index]

df.to_csv(root / "data/un-regional-groups.csv")
