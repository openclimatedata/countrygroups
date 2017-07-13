# Eastern European Group

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

import pandas as pd
from util import to_code, root


countries = """Albania
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

index = [to_code(country) for country in countries]
eastern_european = pd. DataFrame({"Name": countries}, index=index)
eastern_european.index.name = "Code"

eastern_european.to_csv(root / "data/eastern-european-group.csv")

assert len(eastern_european) == 23
