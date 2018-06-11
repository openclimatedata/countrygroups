import json

from pathlib import Path

root = Path(__file__).parents[1]

metadata = json.load(open(root / "datapackage.json"))

out = []

for item in sorted(metadata["resources"], key=lambda k: k['name']):
    name = item["name"]
    title = item["title"]
    path = item["path"]
    if "sources" in item:
        sources = ""
        for source in item["sources"]:
            sources += f"[{source['title']}]({source['path']})\n"
    else:
        sources = "-"
    idx = name.upper().replace("-", "_")
    template = f"""
### {title} ({idx})

[{path}]({path})

Sources:
    {sources}"""

    out.append(template)

print("\n".join(out))
