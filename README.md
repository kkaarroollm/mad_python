### Discrete Mathematics in Python

---
### **1. Sets** ([`sets.py`](./sets.py))

Master fundamental set theory operations with Python! This module implements key set operations and properties.

#### **Operations Supported:**

- **Union:** Combine all elements from two sets.
- **Intersection:** Extract common elements from two sets.
- **Difference:** Find elements in one set that are not in the other.
- **Complement:** Identify elements not present in a given set.
- **Symmetric Difference:** Find elements that belong to either set but not both.
- **Cartesian Product:** Form ordered pairs of elements from two sets.
- **Power Set:** Generate all subsets of a set. Implemented using bit manipulation.
- **Cardinality:** Calculate the number of elements in a set.
- **Subset / Superset:** Check if one set is a subset or superset of another.
- **Proper Subset / Proper Superset:** Verify strict subset or superset relations.

### **2. Relations** ([`relations.py`](./relations.py))

**Binary relations**: tuple(x, y)

#### **What is a Relation?**
For a given set \( A \), a relation \( R \) from \( A \) to \( A \) is defined as a subset of the Cartesian product \( A x A \). This module provides tools to determine and analyze various types of relations.

#### **Types of Relations:**

- **Reflexive:** Each element is related to itself.
- **Irreflexive:** No element is related to itself.
- **Non-reflexive:** Not every element is related to itself.
- **Symmetric:** If \( x \) is related to \( y \), then \( y \) is related to \( x \).
- **Antisymmetric:** If \( x \) is related to \( y \) and \( y \) is related to \( x \), then \( x = y \).
- **Asymmetric:** If \( x \) is related to \( y \), then \( y \) is not related
- **Transitive:** If \( x \) is related to \( y \) and \( y \) is related to \( z \), then \( x \) is related to \( z \).
- **Connectedness:** Every pair of elements is related and no element is related to itself.

---

