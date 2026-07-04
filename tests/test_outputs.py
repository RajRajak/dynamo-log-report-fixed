import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    with REPORT.open() as f:
        return json.load(f)


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and contains a JSON object."""
    assert REPORT.exists(), "/app/report.json was not created"
    data = load_report()
    assert isinstance(data, dict), "report.json must contain a JSON object"


def test_total_requests_is_correct():
    """Criterion 2: total_requests is the number of non-empty log records."""
    data = load_report()
    assert data.get("total_requests") == 6


def test_unique_ips_is_correct():
    """Criterion 3: unique_ips is the number of distinct client IP addresses."""
    data = load_report()
    assert data.get("unique_ips") == 3


def test_top_path_is_correct():
    """Criterion 4: top_path is the most frequently requested path."""
    data = load_report()
    assert data.get("top_path") == "/index.html"
