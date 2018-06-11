import json

from pathlib import Path

root = Path(__file__).parents[1]

metadata = json.load(open(root / "datapackage.json"))

out = []

for item in sorted(metadata["resources"], ):
    name = item["name"]
    title = item["title"]
    path = item["path"]
    if "description" in item:
        description = item["description"]
    else:
        description = ""
    if "sources" in item:
        sources = ""
        for source in item["sources"]:
            sources += f"[{source['title']}]({source['path']})\n"
    else:
        sources = "-"
    template = f"""
### {title}

[{path}]({path})
{description}
Sources:
    {sources}"""

    out.append(template)

print("\n".join(out))
