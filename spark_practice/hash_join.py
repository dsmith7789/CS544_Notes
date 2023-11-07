# Hash Join example, for a single machine

# tuples are (kind id, name)
fruits = [
        ("B", "Yellow"),
        ("A", "Green"),
        ("C", "Orange"),
        ("A", "Red"),
        ("C", "Purple"),
        ("B", "Green")
        ]

# tuples are (kind_id, kind), assume kind_id does not allow duplicates
kinds = [
        ("A", "Apple"),
        ("B", "Banana"),
        ("C", "Carrot")
        ]

# Goal: print "Yellow Banana", "Green Apple", etc. (in any order). Use a hash join
kind_lookup = dict(kinds)   # turns kind table into a hash lookup
for kind_id, color in fruits:
    print(color, kind_lookup[kind_id])

# IMPORTANT: the whole hash table needs to fit in memory for this to work!
