
rooms = {"A": "DIRTY", "B": "CLEAN"}
location = "A"
max_steps = 20
step = 0

print("Initial Environment State:", rooms)
print("-" * 40)

while step < max_steps and ("DIRTY" in rooms.values()):
    step += 1
    print(f"Step {step}: Vacuum is in Room {location}")
    if rooms[location] == "DIRTY":
        print(f"-> Action: SUCK (Cleaning Room {location})")
        rooms[location] = "CLEAN" 
    else:
        new_location = "B" if location == "A" else "A"
        print(f"-> Action: MOVE (Moving from Room {location} to Room {new_location})")
        location = new_location
    print(f"   Current Rooms Status: {rooms}\n")

print("Final Environment State:", rooms)