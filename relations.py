A = {1, 2, 3}
B = {(1, 2), (2, 3), (3, 1)}

def is_reflexive(A, R) -> bool: # noqa
    """
    Check if a relation is reflexive, i.e. if every element in a set is related to itself.
    """
    for x in A:
        if (x, x) not in R:
            return False
    return True


def is_irreflexive(A, R) -> bool: # noqa
    """
    Check if a relation is irreflexive, i.e. if no element in a set is related to itself.
    """
    for x in A:
        if (x, x) in R:
            return False
    return True


def is_non_reflexive(A, R) -> bool: # noqa
    """
    Check if a relation is non-reflexive, i.e. if not every element in a set is related to itself.
    """
    for x in A:
        if (x, x) in R:
            return True
    return False


def is_symmetric(R) -> bool: # noqa
    """
    Check if a relation is symmetric, i.e. if for every (x, y) in R, there is a (y, x) in R.
    """
    for x, y in R:
        if (y, x) not in R:
            return False
    return True

def is_asymmetric(R) -> bool:  # noqa
    """
    Check if a relation is asymmetric, i.e. if for every (x, y) in R, (y, x) is not in R.
    """
    for x, y in R:
        if (y, x) in R:
            return False
    return True


def is_antisymmetric(R) -> bool: # noqa
    """
    Check if a relation is antisymmetric, i.e. if for every (x, y) in R, there is no (y, x) in R.
    """
    for x, y in R:
        if (y, x) in R and x != y:
            return False
    return True


print("Reflexive:", is_reflexive(A, B))  # False, because (1, 1), (2, 2), and (3, 3) are missing
print("Irreflexive:", is_irreflexive(A, B)) # True, because (1, 1), (2, 2), and (3, 3) are missing
print("Non-reflexive:", is_non_reflexive(A, B)) # False, because e.g. (1, 1) is missing
print("Symmetric:", is_symmetric(B)) # False, because e.g. (3, 1) is missing, but (1, 3) is present
print("Asymmetric:", is_asymmetric(B)) # False, because e.g. (1, 2) is missing, but (2, 1) is present
print("Antisymmetric:", is_antisymmetric(B)) # True, because there is no (y, x) in R for every (x, y) in R
