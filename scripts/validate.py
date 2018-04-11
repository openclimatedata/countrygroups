from pathlib import Path
from goodtables import validate
from goodtables.cli import _print_report

root = Path(__file__).parents[1]

report = validate(
    str(root / "datapackage.json"),
    table_limit=40
)
_print_report(report)
