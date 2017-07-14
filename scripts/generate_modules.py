"""
Generate Python and JavaScript modules with ISO identifier codes of groups
listed in Data Package.
"""

import os
import pandas as pd
import pprint

from pandas_datapackage_reader import read_datapackage


path = os.path.dirname(os.path.realpath(__file__))

dp = read_datapackage(os.path.join(path, "../datapackage.json"))
sn = read_datapackage("https://github.com/rgieseke/shortcountrynames")
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

for name, df in sorted(dp.items()):
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

shortnames = pprint.pformat(
    sn.loc[codes].to_dict(orient="dict")["Name"], indent=4)[1:-1]
py_out += "shortnames = {\n "
py_out += shortnames
py_out += "\n}\n"
js_out += "exports.shortnames = {\n "
js_out += shortnames
js_out += "\n}\n"

with open(os.path.join(path, "../countrygroups/__init__.py"), "w") as f:
    f.write(py_out)

with open(os.path.join(path, "../index.js"), "w") as f:
    f.write(js_out)
