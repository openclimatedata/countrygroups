# Latin American and Caribbean Group (GRULAC)

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

import pandas as pd
from util import to_code, root


countries = """Antigua and Barbuda
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
Saint Vincent and the
Grenadines
Suriname
Trinidad and Tobago
Uruguay
Venezuela (Bolivarian Republic of)""".splitlines()

index = [to_code(country) for country in countries]
grulac = pd. DataFrame({"Name": countries}, index=index)
grulac.index.name = "Code"

grulac.to_csv(root / "data/grulac.csv")

assert len(grulac) == 34
