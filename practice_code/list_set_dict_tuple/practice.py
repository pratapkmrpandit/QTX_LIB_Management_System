# List (it is )
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Add
fruits.append("mango")
print("After append:", fruits)

# Access & Slice
print("First fruit:", fruits[0])
print("Fruit from first index to 2 index [1:3]:", fruits[1:3])

# Iterate
for fruit in fruits:
    print("Fruit:", fruit)


# Set
numbers = {1, 2, 3, 4, 5}
print("\nSet:", numbers)

# Add
numbers.add(6)
print("After add:", numbers)

# Remove duplicates automatically
numbers.update([2, 3, 7])
print("After update:", numbers)

# Set operations
evens = {2, 4, 6, 8}
print("Union:", numbers | evens)
print("Intersection:", numbers & evens)
print("Difference:", numbers - evens)


# Dictionary
student = {
    "name": "Alice",
    "age": 20,
    "marks": [85, 90, 92]
}
print("\nDictionary:", student)

# Access
print("Name:", student["name"])
print("Marks:", student.get("marks"))

# Add/Update
student["grade"] = "A"
student["age"] = 21
print("Updated dict:", student)

# Iterate
for key, value in student.items():
    print(f"{key} -> {value}")


# Tuples
coordinates = (10.5, 20.7)
print("\nTuple:", coordinates)

# Access
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Unpacking
x, y = coordinates
print(f"Unpacked -> x: {x}, y: {y}")

# Tuples are immutable 
