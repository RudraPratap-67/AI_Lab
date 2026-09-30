room = {"A": "DIRTY", "B": "DIRTY"}    # create rooms + set conditions
pos = "A"                              # place vacuum
memory = []                            # memory table of all steps

while not (room["A"] == room["B"] == "CLEAN"):    # goal check
    other = "B" if pos == "A" else "A"

    if room[pos] == "DIRTY":                      # check current room
        room[pos] = "CLEAN"                       # SUCK
        action = "SUCK"

    elif room[other] == "DIRTY":                  # check other room
        pos = other                               # MOVE
        action = "MOVE"

    memory.append((len(memory) + 1, pos, action, room["A"], room["B"]))   # store step

print("Step | Pos | Action | A     | B")          # show memory table
for row in memory:
    print(*row, sep=" | ")

print("Goal achieved")
