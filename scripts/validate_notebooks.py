"""Validate notebook structure without executing untrusted notebook code."""
import json
from pathlib import Path
import unittest


def validate(root: Path) -> list[str]:
    errors = []
    for name in ("digit_detective", "campus_message_router"):
        path = root / "notebooks" / f"{name}.ipynb"
        if not path.is_file():
            errors.append(f"Missing {path}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"Invalid JSON in {path}: {exc}")
            continue
        if data.get("nbformat") != 4:
            errors.append(f"{path} must be notebook format 4")
        if not any(cell.get("cell_type") == "markdown" for cell in data.get("cells", [])):
            errors.append(f"{path} must contain instructions")
        codes = [cell for cell in data.get("cells", []) if cell.get("cell_type") == "code"]
        if len(codes) < 2:
            errors.append(f"{path} needs executable starter and example cells")
        for cell in codes:
            if cell.get("outputs"):
                errors.append(f"{path} must not ship precomputed outputs")
            if cell.get("execution_count") is not None:
                errors.append(f"{path} execution counts must be cleared")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        raise SystemExit("\n".join(problems))
    print("Notebook structure validated.")
