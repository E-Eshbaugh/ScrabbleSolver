# Hooks methods for Scrabble word extensions
# @author : Nathaniel Garner
# @author : Ethan Eshbaugh
# 4/24/2025

from typing import List
from data import WORD_ENTRIES

# mapping for scores (used in anagrams.py as well)
LETTER_SCORES = {
    **dict.fromkeys(list("AEIOULNSTRaeioulnstr"), 1),
    **dict.fromkeys(list("DGdg"), 2),
    **dict.fromkeys(list("BCMPbcmp"), 3),
    **dict.fromkeys(list("FHVWYfhvwy"), 4),
    **dict.fromkeys(list("Kk"), 5),
    **dict.fromkeys(list("JXjx"), 8),
    **dict.fromkeys(list("QZqz"), 10),
}


def score_word(word: str) -> int:
    return sum(LETTER_SCORES.get(ch, 0) for ch in word)


def find_hooks(word: str) -> List[str]:

    # input 
    word = word.lower().strip()
    if not word:
        return []

    target_len = len(word) + 1
    results = set()

    # fidn extensions
    for entry in WORD_ENTRIES:
        w = entry["word"].lower()
        if entry["length"] == target_len and (w.startswith(word) or w.endswith(word)):
            results.add(w)

    # Sort by score descending, then alphabetically
    return sorted(results, key=lambda w: (-score_word(w), w))
