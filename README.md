# CircularChordIntersector

This Python algorithm efficiently counts the number of intersections between chords on a circle. It works as follows:

- Start with two counters: one for total intersections and one for active chords (chords currently "in play").
- Loop through each identifier:
  - If it starts with "s," a new chord begins, so increase the active chord count.
  - If it starts with "e," a chord ends, so calculate intersections and reduce active chords.
- For ending chords, calculate intersections using \(n \times (n-1) / 2\), where \(n\) is the active chord count. This reflects each new chord crossing all existing ones.
- Once all identifiers are processed, return the total intersection count.

This algorithm takes linear time (O(n)) and space (O(n)) because:

- It visits each identifier once.
- Operations within each loop are constant time (e.g., checking start/end, updating counters).
- It uses only a fixed amount of extra memory for the counters.

In simpler terms, the algorithm efficiently counts chord intersections with growing datasets, making it ideal for large scenarios.

## How to Use

1. Define the radii (`rads`) and identifiers (`identifiers`) arrays according to your scenario.
2. Call the `count_intersections` function with the radii and identifiers as arguments.
3. The function will return the total number of intersections.
4. Print or use the result as needed.

```python
rads = [0.78, 1.47, 1.77, 3.92]
identifiers = ["s1", "s2", "e1", "e2"]
intersections = count_intersections(rads, identifiers)
print(f"Number of intersections: {intersections}")
```
