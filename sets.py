A = {2, 4, 6, 23, 8, 10}
B = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

# Operations with methods
union = A.union(B) # set_a | set_b
intersection = A.intersection(B) # set_a & set_b

difference_a = A.difference(B) # set_a - set_b
difference_b = B.difference(A) # set_b - set_a
symmetric_difference_a = A.symmetric_difference(B) # set_a ^ set_b
symmetric_difference_b = B.symmetric_difference(A) # set_b ^ set_a

operations = [
    symmetric_difference_a == symmetric_difference_b,  # True
    difference_a == difference_b,  # False
    difference_a | difference_b == symmetric_difference_a,  # True
    difference_b | difference_a == symmetric_difference_b,  # True
    intersection | symmetric_difference_a == union,  # True
    difference_a & difference_b == set()  # True
]

# Subsets and Supersets
sub_A = {2, 4, 6}
AA = {2, 4, 6, 2, 6, 4, 2, 6, 2, 4, 2, 2, 6, 6, 4, 4}

subset_f = A.issubset(B)  # False
subset_t = sub_A.issubset(A)  # True

superset_f = A.issuperset(B)  # False
superset_t = A.issuperset(sub_A)  # True

# Equality
equal_f = A == B  # False
equal_t = sub_A == AA  # True

# Disjoint
disjoint = A.isdisjoint(B)  # True => null intersection

results = {
    "Subsets": (subset_f, subset_t),
    "Supersets": (superset_f, superset_t),
    "Equalities": (equal_f, equal_t),
    "Disjoint": disjoint
}


# Proper Subset
proper_subset = sub_A < A  # True => sub_A is a proper subset of A, because A contains elements that are not in sub_A

# Proper Superset
proper_superset = A > sub_A  # True => A is a proper superset of sub_A, because A contains elements that are not in sub_A

# Cartesian Product
cartesian_product = {(a, b) for a in A for b in B} # set_a x set_b

# Cardinality
cardinality_A = len(A)
cardinality_B = len(B)

# Power Set - All possible subsets of a set
def power_set(s):
    ls = list(s)
    p_setlist = []
    count = 1 << len(ls)  # same as 2**len(s)
    for i in range(count):
        subset = {ls[j] for j in range(len(ls)) if i & (1 << j)}
        p_setlist.append(subset)
    return p_setlist

power_set_A = power_set(A)
