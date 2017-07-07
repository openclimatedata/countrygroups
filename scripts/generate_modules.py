"""
Generate Python and JavaScript modules with ISO identifier codes of groups
listed in Data Package.
"""

import os
import pandas as pd

from pandas_datapackage_reader import read_datapackage


path = os.path.dirname(os.path.realpath(__file__))

dp = read_datapackage(os.path.join(path, "../datapackage.json"))

py_out = '''"""
unfccc_groups
-------------

"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


'''

js_out = '''
// UNFCCC Groups
'''

for name, df in sorted(dp.items()):
    if isinstance(df.index, pd.RangeIndex):
        continue
    group_id = name.replace("-", "_").upper()
    members = sorted(df.index.tolist())
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

with open(os.path.join(path, "../unfccc_groups/__init__.py"), "w") as f:
    f.write(py_out)

with open(os.path.join(path, "../index.js"), "w") as f:
    f.write(js_out)
