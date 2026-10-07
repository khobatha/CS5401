# Recursive edit distance

This example computes the minimum number of single-character insertions, deletions, and substitutions needed to transform one string into another. It uses the recursive implementation from the course screenshot.

Requires Python 3; no external dependencies.

Run from the repository root:

```bash
python3 live-coding/edit-distance/edit_distance.py
```

The example compares `a cat!` with `the cats!` and prints `4`.

This version recomputes subproblems, making it a starting point for discussing memoization and dynamic programming. Use short strings for live demonstrations.

## Version 2: caching (memoization)

`edit_distance_cached.py` stores each subproblem's result in a dictionary keyed by `(m, n)`. Repeated calls for the same prefixes reuse the stored result. A fresh cache is created for each call to `computeEditDistance`.

```bash
python3 live-coding/edit-distance/edit_distance_cached.py
```

The same example prints `4`. Compare the two files to see the cache lookup and storage added to the original recursion.

For string lengths m and n, there are at most `(m + 1) * (n + 1)` subproblems, giving O((m + 1)(n + 1)) time and cache space. The implementation still uses recursion and is subject to Python's recursion depth limit.
