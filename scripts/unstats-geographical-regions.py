import yaml
import json

from util import root, to_code

regions = yaml.load(
    open(str(root / "archive/unstats-geographical-regions.yaml")), Loader=yaml.FullLoader)


def convert_names(subgroup):
    if isinstance(subgroup, dict):
        for k in list(subgroup.keys()):
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
        subgroup.sort(key=lambda x: x if isinstance(x, str)
                      else list(x.keys())[0])

    return(subgroup)


for key in list(regions.keys()):
    new_name = key.replace(' ', '_').replace('-', '_').upper()
    regions[new_name] = convert_names(regions.pop(key))

json.dump(
    regions,
    open(str(root / "data/unstats-geographical-regions.json"), "w"),
    indent=4,
    sort_keys=True
)
