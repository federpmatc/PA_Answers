#Figure out what the program below does
#Add Comments to it so that your instructor can tell that you understand what program does

#In this activity you will need to update the code to print out the total number of guesses

print('\n'*20)
names = [] #define an empty list
print("I'm thinking of someone's name, see if you can guess it")

name = input("Enter someone's name ")
names.append(name)

while name != "Pat":
	name = input("Nope! Guess again....Enter a name ")
	names.append(name)
	
for guesses in names:
	print("     " + guesses)

########## Add code to printout the number of guesses ###########################

print(f"It took you {len(names)} trys.  Here are the names that you guessed:")
for guesses in names:
	print("     " + guesses)

