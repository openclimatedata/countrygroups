[![PyPI](https://img.shields.io/pypi/v/countrygroups.svg)](https://pypi.org/project/countrygroups/)
[![npm](https://img.shields.io/npm/v/countrygroups.svg)](https://www.npmjs.com/package/countrygroups)


Data Package, Python and JavaScript module with country groups.

## Data Package

The Data Package contains the lists used to build the language modules and can
be loaded with respective [language tools](http://frictionlessdata.io/software/).
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

for member in EUROPEAN_UNION:
    print(member)
```

## JavaScript Module

The JavaScript module can be installed with npm:

```
npm install countrygroups
```

It contains arrays with three-letter codes:

```js
var EU = require("countrygroups").EUROPEAN_UNION

console.log(EU)
```

## Data

### Members of the UNFCCC

[data/unfccc.csv](data/unfccc.csv)

Currently, there are 197 Parties (196 States and the European Union) to the United
Nations Framework Convention on Climate Change.
The CSV file contains a list of them and their [status of ratification](http://unfccc.int/essential_background/convention/status_of_ratification/items/2631.php).
Included are country codes, dates of Signature, Ratification, Acceptance,
Accession, Approval, or Succession to the Convention, and Entry into Force.

For an explanation of the legal terms of ratification instruments see
<https://treaties.un.org/Pages/Overview.aspx?path=overview/glossary/page1_en.xml>

### UNFCCC Annex I parties

[data/annex-one.csv](data/annex-one.csv)
[data/annex-one-kaz.csv](data/annex-one.csv)

Parties listed in Annex I of the UNFCCC classified as industrialized (developed) countries and "economies in transition".
After ratifying the Kyoto Protocol Kazakhstan is considered an Annex I Party for the
purposes of the Protocol but remains to be a non-Annex I Party for the purposes of the Convention, the second version includes Kazakhstan.

### UNFCCC Non-Annex I parties

[data/non-annex-one.csv](data/non-annex-one.csv)

Members of the UNFCCC not part of Annex I.

### Least Developed Countries (LDCs)

[data/ldcs.csv](data/ldcs.csv)

[data/graduated-ldcs.csv](data/graduated-ldcs.csv)

The list of Least Developed Countries (LDCs) is taken from
<https://www.un.org/development/desa/dpad/least-developed-country-category/ldcs-at-a-glance.html>
Available are current LDCs and graduated countries.

### Landlocked Developing Countries (LLDCs)

[data/lldcs.csv](data/lldcs.csv)

<http://unohrlls.org/about-lldcs/>

<http://unohrlls.org/about-lldcs/country-profiles/>

### Small Island Developing States (SIDS)

[data/sids.csv](data/sids.csv)

[data/sids-non-un-or-regional-commissions-associates.csv](data/sids-non-un-or-regional-commissions-associates.csv)

List of Small Island Developing States (SIDS) and list of Non-UN Members/Associate Members of Regional Commissions, sourced from
<https://sustainabledevelopment.un.org/topics/sids/list>.

### European Union member states

[data/european-union.csv](data/european-union.csv)

The data is sourced from <https://europa.eu/european-union/about-eu/countries/member-countries_en>.

### G20 members

[data/g20.csv](data/g20.csv)

### Organisation for Economic Co-operation and Development (OECD)

[data/oecd.csv](data/oecd.csv)

Members of the Convention on the Organisation for Economic Co-operation and Development (OECD) and dates on which they deposited their instruments of ratification, sourced from <http://www.oecd.org/about/membersandpartners/list-oecd-member-countries.htm>.

### BRICS

[data/brics.csv](data/brics.csv)

### Umbrella group

[data/umbrella.csv](data/umbrella.csv)

### OPEC

[data/opec.csv](data/opec.csv)

### AOSIS

[data/aosis.csv](data/aosis.csv)

### Environmental Integrity Group (EIG)

[data/eig.csv](data/eig.csv)

### G77

[data/g77.csv](data/g77.csv)

### Arab Group

[data/arab-group.csv](data/arab-group.csv)

### UN Regional Groups

[data/un-regional-groups.csv](data/un-regional-groups.csv)

### IPCC AR5 Region definitions

[data/ar5.csv](data/ar5.csv)

### International Maritime Organization

[data/imo.csv](data/imo.csv)

### SSP (Shared Socioeconomic Pathways) Database Region Definitions

[data/ssp.csv](data/ssp.csv)

### UN Statistical Division Geographical Regions

[data/unstats-geographical-regions.json](data/unstats-geographical-regions.json)


## Preparation

The `Makefile` used to generate the CSV files requires Python3 and will
automatically install its dependencies into a Virtualenv when run with

```shell
make
```

