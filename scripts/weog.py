# Latin American and Caribbean Group (GRULAC)Western European and Others Group (WEOG)

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

import pandas as pd
from util import to_code, root


countries = """Andorra
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

index = [to_code(country) for country in countries]
weog = pd. DataFrame({"Name": countries}, index=index)
weog.index.name = "Code"

weog.to_csv(root / "data/weog.csv")

assert len(weog) == 29
