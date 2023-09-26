group = set(["item 1", "item 2",4])

print(group)

group1 = frozenset(["one", True, 3])
group2 = set(["main", group1])

print(group2)
print( group1.issubset(group2) )
print( group2.issuperset(group1) )
print( group2.issuperset(group2) )
print( group2.issubset(group2) )

# comparing groups
gr1 = set([1,2,3,4,5])
gr2 = set([6,7,8,9])

gr1.isdisjoint(gr2) # It returns false only when the groups are different, means there is no element that exists in both