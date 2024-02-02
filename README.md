# ChordCrossCounter

## Overview

ChordCrossCounter is a Python project that efficiently counts the number of intersections between chords on a circle. The algorithm takes a list of radii and identifiers as input and returns the total number of intersections.

## How it Works

- Start with two counters: one for total intersections and one for active chords (chords currently "in play").
- Loop through each identifier:
  - If it starts with "s," a new chord begins, so increase the active chord count.
  - If it starts with "e," a chord ends, so calculate intersections and reduce active chords.
- For ending chords, calculate intersections using \(n \times (n-1) / 2\), where \(n\) is the active chord count. This reflects each new chord crossing all existing ones.
- Once all identifiers are processed, return the total intersection count.

The algorithm has a time complexity of O(n) and space complexity of O(n), making it efficient for large datasets.

## Usage

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

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/ChordCrossCounter.git
    cd ChordCrossCounter
    ```

2. **Run the script:**

    ```bash
    python chord_cross_counter.py
    ```

