"""Utility functions for parsing common data formats."""

import csv
import io
import json
from urllib.parse import parse_qs, urlsplit


def parse_number_list(raw_text: str):
    """Convert a comma-separated string of numbers into a list of ints."""
    return [int(part.strip()) for part in raw_text.split(',') if part.strip()]


def parse_csv_rows(raw_csv: str):
    """Parse a CSV string into a list of dictionaries."""
    reader = csv.DictReader(io.StringIO(raw_csv.strip()))
    return list(reader)


def parse_json_text(raw_text: str):
    """Safely parse JSON into a Python object."""
    return json.loads(raw_text)


def parse_query_params(url: str):
    """Parse query-string parameters from a URL into a dictionary."""
    parsed = urlsplit(url)
    params = parse_qs(parsed.query)
    return {key: values[0] if len(values) == 1 else values for key, values in params.items()}


if __name__ == "__main__":
    print(parse_number_list("10, 20, 30, 40"))
    print(parse_csv_rows("name,age\nAlice,25\nBob,30"))
    print(parse_json_text('{"name": "Alice", "active": true}'))
    print(parse_query_params("https://example.com/search?q=python&lang=en&tag=django&tag=flask"))
