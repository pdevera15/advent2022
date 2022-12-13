#!/usr/bin/python3

currentElves = 1
currentCalories = 0
currentMaxCalories = 0

# Open a file
fo = open("day-1-input.txt")
lines = fo.readlines
for line in fo:
  # If the line is blank, we've reached the end of an Elf's inventory
  if line.strip() == "":
    # Check if this Elf's total is the new maximum
    if currentMaxCalories < currentCalories:
      currentMaxCalories = currentCalories
    # Reset the current Elf's total and increment the Elf number
    currentElves += 1
    currentCalories = 0
  else:
    # Parse the Calories of the current food item and add it to the current
    currentCalories += int(line.strip())

print(currentMaxCalories)

# Close opened file
fo.close()