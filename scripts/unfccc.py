# UNFCCC signatures and ratification

import re
import pandas as pd

from shortcountrynames import to_name
from util import to_code, root


def get_kind(datestring):
    if datestring.endswith(" A"):
        return "Acceptance"
    elif datestring.endswith(" a"):
        return "Accession"
    elif datestring.endswith(" AA"):
        return "Approval"
    elif datestring.endswith(" d"):
        return "Succession"
    else:
        return "Ratification"


def get_date_only(datestring):
    if datestring[-1] in ["a", "A", "d"]:
        return datestring[:-2]
    elif datestring.endswith(" AA"):
        return datestring[:-3]
    else:
        return datestring


url = ("http://unfccc.int/essential_background/convention/"
       "status_of_ratification/items/2631.php")

print(url)

df = pd.read_html(url, attrs={'class': "unfccc_table"})[0]

df = df.iloc[1:]
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(1))
df.columns.name = None


# Remove (6)(7) etc.
def remove_numbers(name):
    p = re.compile('\(\d\)')
    return p.sub("", name)
df.Participant = df.Participant.apply(remove_numbers)

df.index = df.Participant.apply(to_code)
df.index.name = "Code"

# Check that all rows have an index.
assert all(~df.index.isnull())

df["Participant"] = [to_name(i) for i in df.index]

# Check that all rows have a name.
assert all(~df.Participant.isnull())

# "Ratification  Acceptance (A)  Accession (a)  Approval (AA)  Succession (d)"
df["Kind"] = df.iloc[:, 2].apply(get_kind)

# Check that all rows have the kind of ratification set.
assert all(~df.Kind.isnull())

df.iloc[:, 2] = pd.to_datetime(df.iloc[:, 2].apply(get_date_only))

# Replace Uzbekistan's "---" Signature value.
df.set_value("UZB", "Signature", None)
df.Signature = pd.to_datetime(df.Signature)
df["Entry into force"] = pd.to_datetime(df["Entry into force"])

df = df.rename(columns={
    "Entry into force": "Entry-Into-Force",
    df.columns[2]: "Ratification-Acceptance-Accession-Approval-Succession"
})

df = df[[
    'Participant',
    'Signature',
    'Ratification-Acceptance-Accession-Approval-Succession',
    'Kind',
    'Entry-Into-Force',
]]

assert len(df) == 197
assert sum(~df.Signature.isnull()) == 165
assert len(df.Participant.unique()) == len(df)
df.to_csv(root / "data/unfccc.csv")
