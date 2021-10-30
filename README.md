[![PyPI](https://img.shields.io/pypi/v/countrygroups.svg)](https://pypi.org/project/countrygroups/)
[![npm](https://img.shields.io/npm/v/countrygroups.svg)](https://www.npmjs.com/package/countrygroups)

Data Package, Python and JavaScript module with country groups.

## Data Package

The Data Package contains the lists as CSV or JSON file used to build the
language modules and can be loaded with the respective
[language tools](http://frictionlessdata.io/software/).
Some lists contain additional information like date of joining etc.

## Python Module

The Python module can be installed from
[PyPI](https://pypi.org/project/countrygroups/):

```
pip install countrygroups
```

It contains lists with three-letter codes:

```py
from countrygroups import EUROPEAN_UNION

print(EUROPEAN_UNION)

# =>
# ['AUT', 'BEL', 'BGR', 'CYP', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA',
#  'GRC', 'HRV', 'HUN', 'IRL', 'ITA', 'LTU', 'LUX', 'LVA', 'MLT', 'NLD', 'POL',
#  'PRT', 'ROU', 'SVK', 'SVN', 'SWE']

print(EUROPEAN_UNION.names)

# =>
# ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
#   'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland',
#   'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
#   'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']
```

## JavaScript Module

The JavaScript module can be installed with npm:

```
npm install countrygroups
```

It contains arrays with three-letter codes:

```js
var g7 = require("countrygroups").G7

console.log(g7) // => [ 'CAN', 'DEU', 'EUU', 'FRA', 'GBR', 'ITA', 'JPN', 'USA' ]
```

## Data

### UNFCCC Annex I parties (ANNEX_ONE)

[data/annex-one.csv](data/annex-one.csv)

Sources:
    [List of Annex I Parties to the Convention](http://unfccc.int/parties_and_observers/parties/annex_i/items/2774.php)


### UNFCCC Annex I parties incl. Kazakhstan (ANNEX_ONE_KAZ)

[data/annex-one-kaz.csv](data/annex-one-kaz.csv)

Sources:
    [Greenhouse gas inventory submissions from non-Annex I Parties](https://unfccc.int/process/transparency-and-reporting/greenhouse-gas-data/greenhouse-gas-data-unfccc/greenhouse-gas-inventory-submissions-from-non-annex-i-parties)


### Alliance of Small Island States (AOSIS) (AOSIS)

[data/aosis.csv](data/aosis.csv)

Sources:
    [AOSIS - Members](http://aosis.org/about/members/)


### Regional groups for the IPCC AR5 report (AR5)

[data/ar5.csv](data/ar5.csv)

Sources:
    [AR5 Region Definitions](https://tntcat.iiasa.ac.at/AR5DB/dsd?Action=htmlpage&page=about)


### Arab Group in the UNFCCC (ARAB_GROUP)

[data/arab-group.csv](data/arab-group.csv)

Sources:
    [UNFCCC - Party Groupings](https://unfccc.int/party-groupings)


### BRICS (Brazil, Russia, India, China and South Africa) (BRICS)

[data/brics.csv](data/brics.csv)

Sources:
    -

### Environmental Integrity Group (EIG)

[data/eig.csv](data/eig.csv)

Sources:
    [UNFCCC - Party Groupings](https://unfccc.int/party-groupings)


### European Union (EU) (EUROPEAN_UNION)

[data/european-union.csv](data/european-union.csv)

Sources:
    [EU member countries in brief](https://europa.eu/european-union/about-eu/countries/member-countries_en)


### G20 members (G20)

[data/g20.csv](data/g20.csv)

Sources:
    -

### G7 members (G7)

[data/g7.csv](data/g7.csv)

Sources:
    -

### G77 members (G77)

[data/g77.csv](data/g77.csv)

Sources:
    [The Member States of the Group of 77](http://www.g77.org/doc/members.html)


### Countries graduated from Least Developed Countries (LDCs) (GRADUATED_LDCS)

[data/graduated-ldcs.csv](data/graduated-ldcs.csv)

Sources:
    [LDCs at a Glance](https://www.un.org/development/desa/dpad/least-developed-country-category/ldcs-at-a-glance.html)


### International Maritime Organization (IMO)

[data/imo.csv](data/imo.csv)

Sources:
    [UN Treaty Collection - Convention on the International Maritime Organization](https://treaties.un.org/pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XII-1&chapter=12&clang=_en)


### Least Developed Countries (LDCs) (LDC)

[data/ldc.csv](data/ldc.csv)

Sources:
    [LDCs at a Glance: List of all LDCs in PDF format, (updated June 2017)](https://www.un.org/development/desa/dpad/wp-content/uploads/sites/45/publication/ldc_list.pdf)


### Landlocked Developing Countries (LLDCs) (LLDC)

[data/lldc.csv](data/lldc.csv)

Sources:
    [UN-OHRLLS: Landlocked Developing Countries](http://unohrlls.org/about-lldcs/country-profiles/)


### UNFCCC Non-Annex I parties (NON_ANNEX_ONE)

[data/non-annex-one.csv](data/non-annex-one.csv)

Sources:
    [List of Non-Annex I Parties to the Convention](http://unfccc.int/parties_and_observers/parties/non_annex_i/items/2833.php)


### Organisation for Economic Co-operation and Development (OECD) (OECD)

[data/oecd.csv](data/oecd.csv)

Sources:
    [List of OECD Member countries - Ratification of the Convention on the OECD](http://www.oecd.org/about/membersandpartners/list-oecd-member-countries.htm)


### OPEC members (OPEC)

[data/opec.csv](data/opec.csv)

Sources:
    [OPEC - Member Countries](http://www.opec.org/opec_web/en/about_us/25.htm)


### Small Island Developing States (SIDS) (SIDS)

[data/sids.csv](data/sids.csv)

Sources:
    [Small Island Developing States, List of SIDS](https://sustainabledevelopment.un.org/topics/sids/list)


### Montreal Protocol

[data/montreal_protocol_countries.json]

[data/montreal_protocol_high_ambient_temp.csv]

Sources:
    [Article 5 / Non-Article 5 status](https://ozone.unep.org/classification-parties)
    [Group 1 and 2 and high-ambient-temperature classification](https://ozone.unep.org/treaties/montreal-protocol/meetings/twenty-eighth-meeting-parties/decisions/decision-xxviii2-decision-related-amendment-phasing-down-hydrofluorocarbons)

### Non-UN Members/Associate Members of Regional Commissions of SIDS (SIDS_NON_UN_OR_REGIONAL_COMMISSIONS_ASSOCIATES)

[data/sids-non-un-or-regional-commissions-associates.csv](data/sids-non-un-or-regional-commissions-associates.csv)

Sources:
    [Small Island Developing States, List of SIDS](https://sustainabledevelopment.un.org/topics/sids/list)


### Regional groups for the Shared Socioeconomic Pathways (SSPs) (SSP)

[data/ssp.csv](data/ssp.csv)

Sources:
    -

### Umbrella group (UMBRELLA)

[data/umbrella.csv](data/umbrella.csv)

Sources:
    [UN Climate Change Party Groupings](http://unfccc.int/parties_and_observers/parties/negotiating_groups/items/2714.php)


### UN Regional Groups of Member States (UN_REGIONAL_GROUPS)

[data/un-regional-groups.csv](data/un-regional-groups.csv)

Sources:
    [United Nations Regional Groups of Member States](http://www.un.org/depts/DGACM/RegionalGroups.shtml)


### Members of the UNFCCC (UNFCCC)

[data/unfccc.csv](data/unfccc.csv)

Sources:
    [Status of Ratification of the Convention](http://unfccc.int/essential_background/convention/status_of_ratification/items/2631.php)


### UN Statistical Division Geographical Regions (UNSTATS_GEOGRAPHICAL_REGIONS)

[data/unstats-geographical-regions.json](data/unstats-geographical-regions.json)

Sources:
    [UN Statistics Division - Standard country or area codes for statistical use (M49)](https://unstats.un.org/unsd/methodology/m49/)


## Preparation

The `Makefile` used to generate the CSV files requires Python3 and will
automatically install its dependencies into a Virtualenv when run with

```shell
make
```

