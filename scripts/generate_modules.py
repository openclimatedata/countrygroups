"""
Generate Python and JavaScript modules with ISO identifier codes of groups
listed in Data Package.
"""

import pandas as pd
import pprint

from  pathlib import Path
from pandas_datapackage_reader import read_datapackage


root = Path(__file__).parents[1]

dp = read_datapackage(root / "datapackage.json")

codes = []

py_out = '''"""
countrygroups
-------------

"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


'''

js_out = '''// Country Groups

'''

py_submodules = []

def create_submodule(name, df):
    py_submodule_out = '"""\ncountrygroups.{}\n--------------'.format(
        name) + len(name) * "-" + '\n"""'
    py_submodule_out += "\n\n"
    grouped = df.groupby("Region")
    for region, group in grouped:
        var_name = region.replace("-", "_").replace(" ", "_").upper()
        py_submodule_out += "{} = [\n".format(var_name)
        members = sorted(group.index.tolist())
        for idx, member in enumerate(members):
            item_line = '    "{}"'.format(member)
            py_submodule_out += item_line
            if idx < len(members) - 1:
                py_submodule_out += ",\n"
            else:
                py_submodule_out += "\n"
        py_submodule_out += "]\n\n"

    modulename = name.replace("-", "_")
    with open(root / "countrygroups" / (modulename + ".py"), "w") as f:
        f.write(py_submodule_out)

for name, df in sorted(dp.items()):
    if "subregions" in df.metadata:
        create_submodule(name, df)
        continue

    if isinstance(df.index, pd.RangeIndex):
        continue
    group_id = name.replace("-", "_").upper()
    members = sorted(df.index.tolist())
    for member in members:
        if member not in codes:
            codes.append(member)
    py_out += "{} = [\n".format(group_id)
    js_out += "exports.{} = [\n".format(group_id)
    for idx, item in enumerate(members):
        item_line = '    "{}"'.format(item)
        py_out += item_line
        js_out += item_line
        if idx < len(members) - 1:
            py_out += ",\n"
            js_out += ",\n"
        else:
            py_out += "\n"
            js_out += "\n"
    py_out += "]\n\n"
    js_out += "]\n\n"


with open(root / "countrygroups/__init__.py", "w") as f:
    f.write(py_out)

with open(root / "index.js", "w") as f:
    f.write(js_out)
