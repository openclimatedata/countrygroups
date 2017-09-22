from pathlib import Path

root = Path(__file__).parents[1]

from goodtables import validate
from goodtables.cli import _print_report

report = validate(
    str(root / "datapackage.json"),
    table_limit=40
)
_print_report(report)
