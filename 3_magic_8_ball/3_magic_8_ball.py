## 3. Magic 8 Ball

## Name of person 

name = "Isabelle"

# Determining question

question = ""

# Determing answer 

answer = ""

## Generating a random number 

import random 

random_number = random.randint(1,12)

print(random_number)

## Control flow of program

if random_number == 1:
    answer = "Yes, definitely"
elif random_number == 2:
    answer = "It is decidely so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Try again"
elif random_number == 11:
    answer = "What do you think?"
elif random_number == 12:
    answer = "50/50"
else:
    answer = "Error"

## Putting program in action

if name == "":
    print(str(question))
else: 
    print(str(name) +  " asks: " + str(question))

if question == "":
    print("Ask a question!")
else:
    print("Magic 8-Ball's answer: " + str(answer))