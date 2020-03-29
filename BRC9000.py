from datetime import datetime

# gives date AND time
now = datetime.now()

# we only need the date
curmon = int(now.strftime ("%m"))
curday = int(now.strftime ("%d"))
curyear = int(now.strftime ("%y"))

# mm/dd/YY cuz I'm an American 
date_string = now.strftime("%m/%d/%Y")

print("Is Mount & Blade II: Bannerlord out yet?")
print("Today's date is " + date_string + ".")	
print("Calculating...") #keeps the user at the edge of their seat

if curyear == 20 and curmon == 3 and curday == 31:
    print ("YES POGGERS")
elif curyear == 20 and curmon >= 4:
    print ("YES POGGERS")
elif curyear > 20:
    print ("YES! It's BEEN out!")
else: 
    print ("no :(")
