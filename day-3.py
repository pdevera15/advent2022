import string

# mapping of letters (starting index 0)
alphabet = string.ascii_lowercase + string.ascii_uppercase
itemtypes = ""
container1 = ""
container2 = ""
sum = 0
with open("day-3-input.txt") as f:
  for line in f:
    rucksack = line.split()
    compartmentSize = len(rucksack[0]) / 2
    container1 = rucksack[0][0:int(compartmentSize)]
    container2 = rucksack[0][-int(compartmentSize):]
    for letter in container1:
      if container2.find(letter) != -1 and itemtypes.find(letter) == -1:
        itemtypes += letter
    for letter in itemtypes:
      sum += alphabet.find(letter) + 1
    itemtypes = ""
  print(sum)