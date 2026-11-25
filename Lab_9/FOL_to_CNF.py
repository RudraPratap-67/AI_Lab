
def cnf(e):
    if e[0] == "implies":
        e = ("or", ("not", e[1]), e[2])

    if e[0] == "not" and e[1][0] == "not":
        e = e[1][1]

    if e[0] == "not" and e[1][0] in ("and", "or"):
        op = "or" if e[1][0] == "and" else "and"
        e = (op, ("not", e[1][1]), ("not", e[1][2]))

    if e[0] in ("and", "or"):
        e = (e[0], cnf(e[1]), cnf(e[2]))

        if e[0] == "or":
            a, b = e[1], e[2]
            if a[0] == "and":
                return ("and", cnf(("or", a[1], b)),
                        cnf(("or", a[2], b)))
            if b[0] == "and":
                return ("and", cnf(("or", a, b[1])),
                        cnf(("or", a, b[2])))

    return e


def show(e):
    if e[0] == "not":
        return "NOT " + show(e[1])
    if e[0] in ("and", "or"):
        op = " AND " if e[0] == "and" else " OR "
        return "(" + show(e[1]) + op + show(e[2]) + ")"
    return e[0] + "(" + ", ".join(e[1:]) + ")"


statement = ("implies", ("Student", "x"),
             ("and", ("Book", "y"), ("Reads", "x", "y")))

print("Original FOL Statement:")
print("Student(x) -> (Book(y) AND Reads(x,y))")

result = cnf(statement)

print("\nFinal CNF Expression:")
print(show(result))
