import json
from pathlib import Path
import re

root = Path(__file__).resolve().parent
readme = root / "README.md"


def render(match):
    comment, name, template = match.group(1, 2, 3)
    data = json.loads((root / f"{name}.json").read_text())
    rows = [template.strip()]
    for length in sorted(data, key=int):
        rows.append(f"| {length} | {', '.join(data[length])} |")
    return comment + "\n\n" + "\n".join(rows)


pattern = (
    r"(<!-- template:(words|phrases)\n(.*?)\n-->)"
    r"(?:\n\n\|[^\n]*(?:\n\|[^\n]*)*)?"
)
readme.write_text(re.sub(pattern, render, readme.read_text(), flags=re.DOTALL))
