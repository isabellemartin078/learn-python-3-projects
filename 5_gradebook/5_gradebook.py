## 5. Gradebook

# Creating a list of subjects 

subjects = ["physics", "calculus", "poetry", "history"]

# Creating a list of grades

grades = [98, 97, 85, 88]

# Creating 2D list of subjects and grades

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

## Updating with computer science subject and grade

gradebook.append(["computer science", 100])

print(gradebook)

## Updating with visual arts subject and grade

gradebook.append(["visual arts", 93])

print(gradebook)

### Modifying the gradebook

# Modifying visual arts grade

gradebook[-1][-1] = 98

print(gradebook)

# Deleting grade from poetry class

gradebook[2].remove(85)

print(gradebook)

# Adding pass / fail grade to poetry class

gradebook[2].append("Pass")

print(gradebook)