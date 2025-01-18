# set = is a collection of un-indexed, unordered. no duplicate values
# faster than list, if we need to check that sth is in the set or not

utensils = {'knife', 'knife', 'spoon', 'fork'}
dishes = {'bowl', 'plate', 'cup'}


utensils.add('napkin')
utensils.remove('knife')

dinner_set = utensils.union(dishes)
utensils.update(dishes)

print(dinner_set.difference(dishes))
print(dinner_set.intersection(utensils))

for x in utensils:
    print(x)                   # it will print knife only once

utensils.clear()
