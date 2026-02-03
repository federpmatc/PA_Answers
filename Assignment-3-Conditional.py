# Fix the mistakes in this code and test based on the description below
# If a student has 3 or more unexecused absences he/she is dropped from class 
# If I enter 3 I should see the message "You will be dropped from class" 
# If I enter 0 I should see the message "You are awesome!!! Keep up the great work" 
# If I enter 1 I should see the message "Make sure to let your instructor know if you're going to miss any classes" 

print("\n"*20)
absences = input('how many unexecused absences? ')

#HINT: THe next line should take into account that user entered a string...you will need to treat absences as a number

try:
    daysMissed = int(absences)
except:
     print('try entering an integer')
     exit()
else:
     print(f'You entered {daysMissed} absences')

if daysMissed >= 3:
	print("You will be dropped")
elif daysMissed >= 1:
    print("Make sure3 to let your instructor know if you're going to miss any classes")
else :
    print("You are awesome!!! Keep up the great work")	     
	      
