
def unify(x, y, sub=None):
    if sub is None:
        sub = {}

    if x == y:
        return sub

    if isinstance(x, str) and x.islower():
        sub[x] = y
        return sub

    if isinstance(y, str) and y.islower():
        sub[y] = x
        return sub

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            sub = unify(a, b, sub)
            if sub is None:
                return None
        return sub

    return None


A = ("Drives", "x", "Car")
B = ("Drives", "Rudra", "y")

result = unify(A, B)

if result is not None:
    print("Unification Successful")
    print("Substitution:", result)
else:
    print("Unification Failed")
