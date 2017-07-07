Data Package with groups in the United Nations Framework Convention on Climate Change (UNFCCC).

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

### EU member states

[data/eu-member-states.csv](data/eu-member-states.csv)

The data is sourced from <https://europa.eu/european-union/about-eu/countries/member-countries_en>
and turned into a simple CSV file.

### G20 members

[data/g20.csv](data/g20.csv)

### Organisation for Economic Co-operation and Development (OECD)

[data/oecd.csv](data/oecd.csv)

Members of the Convention on the Organisation for Economic Co-operation and Development (OECD) and dates on which they deposited their instruments of ratification, sourced from <http://www.oecd.org/about/membersandpartners/list-oecd-member-countries.htm>.


## Preparation

The `Makefile` used to generate the CSV files requires Python3 and will
automatically install its dependencies into a Virtualenv when run with

```shell
make
```

