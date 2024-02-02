#!/usr/bin/env python
# coding: utf-8

# In[30]:


from math import pi

def count_intersections(rads, identifiers):
    n = len(rads)
    intersections = 0
    active_chords = 0

    for i in range(n):
        if identifiers[i].startswith('s'):
            active_chords += 1
        else:
            intersections += active_chords * (active_chords - 1) // 2
            active_chords -= 1

    return intersections

rads = [0.78, 1.47, 1.77, 3.92]
identifiers = ["s1", "s2", "e1", "e2"]
intersections = count_intersections(rads, identifiers)
print(f"Number of intersections: {intersections}")

rads = [0.9, 1.3, 1.70, 2.92]
identifiers = ["s1", "e1", "s2", "e2"]
intersections = count_intersections(rads, identifiers)
print(f"Number of intersections: {intersections}")


# In[ ]:




