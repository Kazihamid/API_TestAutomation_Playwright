import json
from pathlib import Path

TEST_DATA_DIR = Path(__file__).resolve().parent.parent / "test_data"


def load_json(relative_path):
    with open(TEST_DATA_DIR / relative_path, encoding="utf-8") as f:
        return json.load(f)
