# African Group

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

import pandas as pd
from util import to_code, root

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
Zimbabwe""".splitlines()

index = [to_code(country) for country in countries]
african_group = pd. DataFrame({"Name": countries}, index=index)
african_group.index.name = "Code"

african_group.to_csv(root / "data/african-group.csv")

assert len(african_group) == 54
