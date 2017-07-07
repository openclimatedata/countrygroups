import os
import pandas as pd

from pandas_datapackage_reader import read_datapackage


path = os.path.dirname(os.path.realpath(__file__))

dp = read_datapackage(os.path.join(path, "../datapackage.json"))

out = '''"""
unfccc_groups
-------------

"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


'''

for name, df in sorted(dp.items()):
    if isinstance(df.index, pd.RangeIndex):
        continue
    group_id = name.replace("-", "_").upper()
    members = df.index.tolist()
    out += "{} = [\n".format(group_id)
    for idx, item in enumerate(members):
        out += '    "{}"'.format(item)
        if idx < len(members) - 1:
            out += ",\n"
        else:
            out += "\n"
    out += "]\n\n"

with open(os.path.join(path, "../unfccc_groups/__init__.py"), "w") as f:
    f.write(out)
