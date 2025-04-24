# helper functions to connect to the database and log searches
# @author : Ethan Eshbaugh
# 4/24/2025

import csv
from pathlib import Path
from typing import Any, Dict, List

# ——— Load word list from CSV ———
_WORDS_CSV = Path(__file__).parent / "hash_dictionary.csv"

WORD_ENTRIES: List[Dict[str, Any]] = []
with _WORDS_CSV.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # each row has: word, hash, length
        WORD_ENTRIES.append({
            "word": row["word"],
            "hash": row.get("hash", ""),
            "length": int(row["length"]),
        })


# ——— Prepare search log CSV ———
_LOG_CSV = Path(__file__).parent / "search_log.csv"

# If it doesn't exist yet, create it with headers
if not _LOG_CSV.exists():
    with _LOG_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["term", "mode", "searched_at"])


def log_search(term: str, mode: str, timestamp: str) -> None:
    """
    Append a new line to search_log.csv.
    
    Args:
        term: The input string the user searched for.
        mode: 'anagram' or 'hook'.
        timestamp: ISO-format timestamp (e.g. from datetime.now().isoformat()).
    """
    with _LOG_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([term, mode, timestamp])