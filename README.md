# ChordCrossCounter

## Overview

ChordCrossCounter is a Python project that efficiently counts the number of intersections between chords on a circle. The algorithm takes a list of radii and identifiers as input and returns the total number of intersections.

## How it Works

The algorithm presented effectively counts the chord intersections in a circular layout.
Initializing variables to track intersections and active chords is the first step. Subsequently,
iterating over the chord list, it determines the beginning and ending positions. It counts the
number of active chords when it comes across a start point and determines the intersections
that chord contributed when it comes across an end point. The arrangement of active chords
determines these intersections. The number of active chords is modified in accordance with
each iteration. Call the count_intersections function after supplying the list of radian measures
and chord identifiers to utilize the algorithm. Iterating through the chords, the chords once and
performing constant-time operations for each chord, the algorithm provides efficient
performance with a time complexity of O(n).
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

