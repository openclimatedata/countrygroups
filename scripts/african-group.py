# African Group

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

from util import to_csv

countries = """Algeria
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
Zimbabwe"""

african_group = to_csv(countries, "african-group.csv")

assert len(african_group) == 54
