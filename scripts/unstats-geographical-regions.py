import yaml
import json

from util import root, to_code

regions = yaml.load(
    open(str(root / "archive/unstats-geographical-regions.yaml")))

def convert_names(subgroup):
    if isinstance(subgroup, dict):
        for k, v in subgroup.items():
            new_name = k.replace(' ', '_').replace('-', '_').upper()
            subgroup[new_name] = convert_names(subgroup.pop(k))
    elif isinstance(subgroup, list):
        for idx, item in enumerate(subgroup):
            if isinstance(item, dict):
                subgroup[idx] = convert_names(subgroup[idx])
            else:
                if not to_code(item):
                    subgroup.pop(idx)
                else:
                    subgroup[idx] = to_code(item)
    return(subgroup)

for key, value in regions.items():
    new_name = key.replace(' ', '_').replace('-', '_').upper()
    del regions[key]
    regions[new_name] = convert_names(value)

json.dump(
    regions,
    open(str(root / "data/unstats-geographical-regions.json"), "w"),
    indent=4
)
