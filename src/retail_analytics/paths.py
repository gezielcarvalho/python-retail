"""Shared filesystem paths used by the retail analytics package."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
DEFAULT_DATASET_PATH = DATA_DIR / "dataset.csv"
