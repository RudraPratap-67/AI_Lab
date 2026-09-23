MAX = 12

def linear_search(arr, key):
    for item in arr:
        if item == key:
            return True
    return False

n = int(input(f"Enter array length [MAX {MAX}]: "))
arr = []
print("ENTER ARRAY:")
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter value to search for: "))
found = linear_search(arr, key)
if found:
    print(f"Key {key} found in the array.")
else:
    print(f"Key {key} not found in the array.")