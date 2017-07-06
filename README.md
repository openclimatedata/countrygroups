Data Package with groups in the United Nations Framework Convention on Climate Change (UNFCCC).

## Data

### Members of the UNFCCC

<data/unfccc.csv>

Currently, there are 197 Parties (196 States and the European Union) to the United
Nations Framework Convention on Climate Change.
The CSV file contains a list of them and their [status of ratification](http://unfccc.int/essential_background/convention/status_of_ratification/items/2631.php).
Included are country codes, dates of Signature, Ratification, Acceptance,
Accession, Approval, or Succession to the Convention, and Entry into Force.

For an explanation of the legal terms of ratification instruments see
<https://treaties.un.org/Pages/Overview.aspx?path=overview/glossary/page1_en.xml>

### Annex I parties

<data/annex-one.csv>

Parties listed in Annex I of the convention are classified as industrialized (developed) countries and "economies in transition".

### Non-Annex I parties

<data/non-annex-one.csv>

Members of the UNFCCC not part of Annex I.


## Preparation

The `Makefile` used to generate the CSV files requires Python3 and will
automatically install its dependencies into a Virtualenv when run with

```shell
make
```

