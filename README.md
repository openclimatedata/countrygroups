Data Package, Python and JavaScript module with country groups, especially those in the United Nations Framework Convention on Climate Change (UNFCCC).

## Data Package

The Data Package contains the lists used to build the language modules and can
be loaded with respective [language tools](http://frictionlessdata.io/tools/).
Some lists contain additional information like data of joining etc.

## Python Module

The Python module contains lists with three-letter codes and a dictionary
mapping to short names: `shortnames`.

```py
from countrygroups import EUROPEAN_UNION, shortnames

for member in EUROPEAN_UNION:
    print(shortnames[member])
```

## JavaScript Module

The module contains arrays with three-letter codes and an object mapping to
short names: `shortnames`

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

### Annex I parties

[data/annex-one.csv](data/annex-one.csv)

Parties listed in Annex I of the convention are classified as industrialized (developed) countries and "economies in transition".

### Non-Annex I parties

[data/non-annex-one.csv](data/non-annex-one.csv)

Members of the UNFCCC not part of Annex I.

### Least Developed Countries (LDCs)

[data/ldcs.csv](data/ldcs.csv)

[data/graduated-ldcs.csv](data/graduated-ldcs.csv)

The list of Least Developed Countries (LDCs) is taken from
<https://www.un.org/development/desa/dpad/least-developed-country-category/ldcs-at-a-glance.html>
and turned into CSV files for current LDCs and graduated countries.

### Small Island Developing States (SIDS)

[data/sids.csv](data/sids.csv)

[data/sids-non-un-or-regional-commissions-associates.csv](data/sids-non-un-or-regional-commissions-associates.csv)

List of Small Island Developing States (SIDS) and list of Non-UN Members/Associate Members of Regional Commissions as CSV files, sourced from
<https://sustainabledevelopment.un.org/topics/sids/list>.

### European Union member states

[data/european-union.csv](data/european-union.csv)

The data is sourced from <https://europa.eu/european-union/about-eu/countries/member-countries_en>
and turned into a simple CSV file.

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

[data/arab-group.csv](arab-group.csv)

### African Group

[data/african-group.csv](african-group.csv)

### Asia-Pacific Group

[data/asia-pacific-group.csv](asia-pacific-group.csv)

### Eastern European Group

[data/eastern-european-group.csv](data/eastern-european-group.csv)

### Latin American and Caribbean Group (GRULAC)

[data/grulac.csv](data/grulac.csv)

### Western European and Others Group (WEOG)

[data/weog.csv](data/weog.csv)


## Preparation

The `Makefile` used to generate the CSV files requires Python3 and will
automatically install its dependencies into a Virtualenv when run with

```shell
make
```

