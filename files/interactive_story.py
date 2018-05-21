def YesNo(answer): #Allows the user to enter 'y', 'Y', or and case of 'yes' to return a 'Y' other wise returns 'N'
	if (answer.upper() == "Y") | (answer.upper() == "YES"):
		return "Y"
	else:
		return "N"

def cornerStore(): #This is the first third of the story
	print "You walk to the corner store for stuff in the middle of the night. An armed man comes in and holds the cashier at gunpoint. "
	answer = raw_input("Would you like to save him? (y/n)")
	if YesNo(answer) == "Y":
		Hero()
		stayOrLeave()
	else:
	 Bystander()
	 cornerStore()
	
	
def Hero():
	print
	print "You hit the armed man and he runs out of the store, fleeing the scene."
	
def Bystander():
	print
	print "You see the cashier get killed and the armed man finds you hiding and takes you out to his car to 'tie off loose ends'."
	print "DEAD"
	
def stayOrLeave():
	print
	print "You have the choice to either chase him or let him run away."
	answer = raw_input("Would you like to chase him? (y/n)")
	if YesNo(answer) == "Y":
		chaseHim()
		stayOrLeave()
	else:
		waitForCops()
	runTowardsHome()
		
def chaseHim():
	print
	print "You run after him, but you don't look both ways before crossing the street and get hit by a car."
print "DEAD"
def waitForCops():
	print
	print "You wait for the police to come and take you and the cashier down to the station for questioning, but you find out the cops are dirty. "

def runTowardsHome():
	print
	print "You decide to run out of the police department and run towards your home. You're afraid you're being followed, so you take an alternate route. As you walk onto your street you think to yourself \"Should I go home and possibly put my family in danger, or should I go rogue and become the real life Ethan Hunt or James Bond?\ "
	answer = raw_input("Do you want to go home? (y/n)")
	if YesNo(answer) == "Y":
		PossibleDanger()
	else:
		goRogue()
		
def PossibleDanger():
	print
	print "You head back into your house and go in to check on your family and everything is safe for now... But will it stay that way?"
	print "TO BE CONTINUED"

def goRogue():
	print
	print "You put a note explaining everything to your family under the door and then you leave. You give yourself one goal.. Find and exterminate the people that can hurt your family... John Wick style..."
	print "The End"
	
cornerStore() #Initilized the running of the program
