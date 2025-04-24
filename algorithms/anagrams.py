# Anagram methods for Scrabble word finder
# @author : Nathaniel Garner
# @author : Ethan Eshbaugh
# 4/24/2025

import string
import itertools
from collections import defaultdict
from data import WORD_ENTRIES
from algorithms.hooks import score_word

# Build hash map for fast lookup [O(1)]
_HASH_MAP: dict[str, list[str]] = defaultdict(list)
for entry in WORD_ENTRIES:
    _HASH_MAP[entry["hash"]].append(entry["word"])


def find_anagrams(rack: str) -> list[str]:

    # input
    rack = rack.lower().strip()
    if len(rack) != 7:
        return []

    n = len(rack)
    seen_hashes: set[str] = set()

    for substring in range(1, 1 << n):
        subset = [rack[i] for i in range(n) if (substring >> i) & 1]

        # handle blanks by expanding into a pool of all letters
        pools = [(string.ascii_lowercase if ch == '_' else ch) for ch in subset]
        for prod in itertools.product(*pools):
            signature = ''.join(sorted(prod))
            seen_hashes.add(signature)

    results: set[str] = set()

    for hash in seen_hashes:
        results.update(_HASH_MAP.get(hash, []))

    # Sort by score descending then alphabetically
    return sorted(results, key=lambda w: (-score_word(w), w))