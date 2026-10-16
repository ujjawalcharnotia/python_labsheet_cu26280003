s = {1, 2}
power_set = {frozenset()}
for x in s:
    new_sets = set()
    for subset in power_set:
        new_sets.add(subset | {x})
    power_set.update(new_sets)
print("Power set:", power_set)