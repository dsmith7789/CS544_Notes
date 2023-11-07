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
