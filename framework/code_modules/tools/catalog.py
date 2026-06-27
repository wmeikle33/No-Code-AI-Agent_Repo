import csv
from pathlib import Path

CATALOG_PATH = Path(__file__).resolve().parents[2] / "knowledge" / "product_catalog.csv"

def search_catalog(query: str) -> list[dict]:
    query = query.lower()
    with CATALOG_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    return [
        row for row in rows
        if query in row["name"].lower()
        or query in row["category"].lower()
        or query in row["description"].lower()
    ]
