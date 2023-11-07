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

# Algorithm relies on tables being sorted by the key
fruits.sort()
kinds.sort()

fruit_idx = 0
for kind_id, food_name in kinds:
    while fruit_idx < len(fruits):
        if fruits[fruit_idx][0] == kind_id:
            print(fruits[fruit_idx][1], food_name)
        else:
            break
        fruit_idx += 1

# need to use the same hash partition function and mod on both tables
# end up with pairs of partitions with same keys on both sides (i.e. all tuples with
# "A" are in the same partition)
# both tables go over the network but only exactly once.
