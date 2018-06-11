"""
Generate Python and JavaScript modules with ISO identifier codes of groups
listed in Data Package.
"""

import json

from pathlib import Path
from pandas_datapackage_reader import read_datapackage
from yapf.yapflib.yapf_api import FormatCode

root = Path(__file__).parents[1]


dp = read_datapackage(root / "datapackage.json")
with open(root / "datapackage.json", "r") as f:
    metadata = json.load(f)

py_out = '''"""
countrygroups
-------------

"""

from shortcountrynames import to_name

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


class Group(list):
    def _add_dict_items(self, d):
        for k, v in d.items():
            v = Group(v)
            setattr(self, k, v)
            self += v

    def __init__(self, group):
        if isinstance(group, dict):
            self._add_dict_items(group)
        else:
            for v in group:
                if isinstance(v, dict):
                    self._add_dict_items(v)
                else:
                    self.append(v)

    @property
    def names(self):
        return sorted([to_name(item) for item in self])

'''

js_out = '''// Country Groups

'''

for resource in sorted(metadata["resources"], key=lambda x: x["name"]):
    if resource["format"] == "json":
        continue
    name = resource["name"]
    df = dp[name]
    if "subregions" in resource:
        members = {}
        df = df.reset_index().sort_values(["Region", "Code"]).set_index("Code")
        for code, region in df.Region.items():
            region = region.replace(' ', '_').replace('-', '_').upper()
            if region not in members:
                members[region] = [code]
            else:
                members[region].append(code)
    else:
        members = sorted(df.index.tolist())

    group_id = name.replace("-", "_").upper()
    py_out += "{} = Group({})\n\n".format(
        group_id, members)

    js_out += "exports.{} = {}\n\n".format(group_id, members)

nested_groups = [item for item in metadata["resources"]
                 if item["format"] == "json"]

for nested_group in nested_groups:
    group_id = nested_group["name"].replace("-", "_").upper()
    with open(nested_group["path"], "r") as f:
        data = f.read()
    py_out += "{} = Group({{{}}})\n".format(
        group_id, data[1:-2])
    js_out += "{} = {}\n\n".format(group_id, data)


with open(str(root / "py/countrygroups/__init__.py"), "w") as f:
    f.write(FormatCode(py_out)[0])

with open(str(root / "index.js"), "w") as f:
    f.write(js_out)
