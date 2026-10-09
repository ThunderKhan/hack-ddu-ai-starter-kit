"""Execute every saved notebook code cell in a separate headless namespace.

Smoke test for the exact self-contained code participants see in Colab.
No network, secrets, notebook server, or notebook-specific package required.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")


def run_notebook(path: Path) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__track_a_smoke__", "__file__": str(path)}
    executed = 0
    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        source = cell.get("source", [])
        code = "".join(source) if isinstance(source, list) else source
        exec(compile(code, f"{path.name}:cell-{executed + 1}", "exec"), namespace)
        executed += 1
    if executed < 2:
        raise AssertionError(f"{path}: expected at least two executable cells")
    print(f"OK: {path.name} ({executed} executed code cells)")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    for name in ("digit_detective", "campus_message_router"):
        run_notebook(root / "notebooks" / f"{name}.ipynb")
