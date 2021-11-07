import random

def Game(comp,user):
    if comp == user:
        return None
    elif comp == 'w':
        if user == 'g':
            return False
        elif user == 's':
            return True 
    elif comp == 'g':
        if user == 's':
            return False
        elif user == 'w':
            return True
    elif comp == 's':
        if user == 'w':
            return False
        elif user == 'g':
            return True 
    elif comp != user:
        return ""
    


# comp = input("Computer Turn : Choose Water(w) Gun(g) Or Snake(s)")
comp = ""

randNo = random.randint(1,3)

if randNo == 1:
    comp = 'w'
elif randNo == 2:
    comp = 'g'
elif randNo == 3:
    comp = 's'

user = input("Your Turn : Choose Water(w) Gun(g) Or Snake(s) ")

a = Game(comp,user)

print("Computer Chose " , comp)
print("You Chose " , user)

if a == None:
    print("Game Tied")
elif a == False:
    print("You Loose")
elif a == True:
    print("You Win")
elif a == "":
    print("Invalid Input")
