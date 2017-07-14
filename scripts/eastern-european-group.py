# Eastern European Group

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

from util import to_csv


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
Ukraine"""

eastern_european = to_csv(countries, "eastern-european-group.csv")

assert len(eastern_european) == 23
