# Western European and Others Group (WEOG)

# http://www.un.org/depts/DGACM/RegionalGroups.shtml

from util import to_csv


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
United States of America"""

weog = to_csv(countries, "weog.csv")

assert len(weog) == 29
