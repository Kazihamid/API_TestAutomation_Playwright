import json
from pathlib import Path

import pytest

TEST_DATA_DIR = Path(__file__).resolve().parent.parent / "test_data"


def load_json(relative_path):
    with open(TEST_DATA_DIR / relative_path, encoding="utf-8") as f:
        return json.load(f)


def load_payload(relative_path):
    """Loads a request body; skips the test if the file is still marked _incomplete."""
    payload = load_json(relative_path)
    if "_incomplete" in payload:
        pytest.skip(payload["_incomplete"])
    return payload
