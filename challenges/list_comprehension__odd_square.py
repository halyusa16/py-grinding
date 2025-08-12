# Write a single list comprehension to create a new list that contains the squares of all odd numbers from 1 to 20.
# Your final list should look like this: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361].

# i want to do square multiple for numbers in range(21) if its an odd numbers
square_odd = [x ** 2 for x in range(21) if x % 2 == 1]

print(square_odd)
