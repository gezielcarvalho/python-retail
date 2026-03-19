#!/usr/bin/env python3
"""Strip outputs and execution counters from Jupyter notebooks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove cell outputs and execution counts from notebook files."
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Notebook files to clean. If omitted, all root-level .ipynb files are scanned.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode. Exit with code 1 if any notebook would be modified.",
    )
    return parser.parse_args()


def resolve_targets(raw_paths: list[str]) -> list[Path]:
    if raw_paths:
        return [Path(path) for path in raw_paths]
    return sorted(Path.cwd().glob("*.ipynb"))


def strip_notebook(notebook: dict[str, Any]) -> bool:
    changed = False

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "code":
            continue

        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True

        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True

    metadata = notebook.get("metadata", {})
    if "widgets" in metadata:
        metadata.pop("widgets")
        changed = True

    return changed


def process_notebook(path: Path, check_only: bool) -> bool:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    changed = strip_notebook(notebook)

    if changed and not check_only:
        path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    return changed


def main() -> int:
    args = parse_args()
    targets = resolve_targets(args.files)

    if not targets:
        print("No notebook files found.")
        return 0

    missing_files = [path for path in targets if not path.exists()]
    if missing_files:
        missing_text = ", ".join(str(path) for path in missing_files)
        print(f"Notebook file not found: {missing_text}")
        return 2

    dirty_files: list[Path] = []

    for notebook_path in targets:
        if notebook_path.suffix != ".ipynb":
            continue

        if process_notebook(notebook_path, check_only=args.check):
            dirty_files.append(notebook_path)

    if args.check:
        if dirty_files:
            print("Notebooks with outputs detected:")
            for path in dirty_files:
                print(f"- {path}")
            return 1

        print("All notebooks are clean.")
        return 0

    if dirty_files:
        print("Notebook outputs removed from:")
        for path in dirty_files:
            print(f"- {path}")
    else:
        print("No notebook changes were needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
