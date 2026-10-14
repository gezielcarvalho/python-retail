# Architecture

The project combines notebook-led exploration with reusable Python package modules.

- `Q01`–`Q10` notebooks answer discrete business questions and generate visual narratives.
- `src/retail_analytics/` contains shared data I/O, transforms, paths, and plotting utilities.
- `tests/` contains automated checks for reusable logic.
- `data/dataset.csv` is the tracked analytical input.
- `images/` contains exported visualization artifacts.
- `scripts/strip_notebook_outputs.py` supports notebook hygiene.

The repository is an analytics showcase, not a deployed service. A future CLI or dashboard remains roadmap work rather than current architecture.
