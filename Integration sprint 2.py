#Holly Rodusky
#this program will allow people to choose a travel destination
print("Hello!",end=' ')
print("Thank you for using my program")
print("This will help you decide on a vacation destination")
#I cannot use this naturally in my program so I'm placing it at the beginning
#Student Assistant Andrew helped me with this
print("Here is an example of the mod operator:", "5 % 2", 5%2)
#I want to calculate the maximum travel and hotel cost the user is willing to spend
#I will use addition
print("---------------------------------------------")

#I also want to determine how many days the user wants to stay.
print("Lets calculate your maximum cost and stay")
airfair=float(input("Enter the maximum amount you are willing to spend on airfair and or gas: "))
hotel=float(input("Enter the total maximum amount you are willing to spend on a hotel/airbnb: "))
hours=float(input("Enter the maximum hours you are willing to travel: "))
days=float(input("Enter the amount of days you want to spend: "))
totalCost= airfair + hotel
print("---------------------------------------------")

print("Cost of airfair/gas: ",format(airfair,".2f"),sep='')
print("Cost of hotel: ",format(hotel,".2f"),sep='')
print("Days you will spend in the destination: ",days)
print("Total hours to get to destination: ",hours)
print("Total cost:$",format(totalCost,".2f"),sep='')
print("---------------------------------------------")

#Now I will divide the total cost by day to get a cost per day
#I will get the estimated average cost with floor division
costPerDay= totalCost/days
estimateCostPerDay= totalCost//days
print("Calculated below is the estimated and actual cost per day")
print("The estimated cost per day is: $",format(estimateCostPerDay,".2f"),sep="")
print("The total cost per day will be: $",format(costPerDay,".2f"),sep="")
print("---------------------------------------------")

#I will use subtraction to account for rainy days or delayed flights
print("Now you will take into account if you lose a day on your trip")
missedDays=int(input("Enter the amount of days you think you may lose due to rain or a delayed flight: "))
totalMissedDays= days - missedDays
print("This is how many days you'll actually have:",totalMissedDays)
print("---------------------------------------------")

#I want the user to see how far they are willing to travel in the area in realtion to their hotel
#I will use the exponent opperator and the area of a circle formula (A=3.14159*r**2)
print("Next you will calulate the area you can cover, with your hotel as the center")               
distance=float(input("How many miles are you willing to travel from the distance of your hotel: "))
pi=float(3.14159)
area= pi * distance**2
miles= 'mi.'
print("The total area you can travel, with your hotel as the center point is:",format(area,".2f") + " " + miles)
print("---------------------------------------------")

#now i will figure out how far they want to travel
print("Next you will determine how far you want to travel")
distanceFromHome= float(input("How many miles do you want to travel from home:"))
if (distanceFromHome>=200) and (distanceFromHome<=3000):
    print("You should fly domestic!")
elif (distanceFromHome<=199) and (distanceFromHome>=1):
    print("You should drive!")
else:
    print("You should fly international!")
print("Are you excited yet" + "?"*3)
print("---------------------------------------------")

#we need to determine what states/countries the user is interested in
print("Now we will deterimine the destination")
#I will give options by domestic and international
#this will be based on their preference for weather and season
weather=input("Are you looking for warm or cold weather?: ")
idealTime=input("What is the ideal season you want to go?: ")

if (weather == 'warm') and (idealTime != 'fall','autum','winter'):
    if (distanceFromHome>=1) and (distanceFromHome<=3000):
        print("Florida, Maine, Massachusetts, Hawaii, California, and New York may interest you!")
    else:
        print ("London, Peru, Canada, Jamaica, Japan, and Italy may interest you!")
elif (weather == 'warm') and (idealTime == 'fall','autum','winter'):
    if (distanceFromHome>=1) and (distanceFromHome<=3000):
        print("Florida, California, Hawaii, Texas, and Arizona may interest you!")
    else:
        print("Aruba, Mexico, The Bahamas, Colombia, and Indonesia may interest you!")
elif (weather == 'cold') and (idealTime != 'fall','autum','winter'):
    if (distanceFromHome>=1) and (distanceFromHome<=3000):
        print("Colorado, Alaska, Michigan, Oregon, and Illinois may interest you!")
    else:
        print("Iceland, Austrailia, South Africa, Canada, and Chile may interest you!")
elif (weather == 'cold') and (idealTime == 'fall','autum','winter'):
    if (distanceFromHome>=1) and (distanceFromHome<=3000):
        print("Vermont, Maryland, New Jersey, Ohio, and Washington may interest you!")
    else:
        print("Amsterdam, Greece, Sweeden, Switzerland, and Poland may interest you!")
print("Yay! now we have narrowed it down a bit!")    
       
#I will determine what the user wants to do while on vacation through with two options
print("---------------------------------------------")
print("Let's find one activity that could be fun while on vacation")
print("Option 1 is go downtown/the city, and option 2 is go to the beach/going outside")
optionOne = True
while optionOne:
    userOption=input("What would you like to do?: ")
    if userOption != True:
        print("You made a great choice, the beach it is!")
    else:
        print("Great, you should go downtown to the city!")
    optionOne=False

#I will calculate a budget for food now
print("---------------------------------------------")
def calculateCost(MealperPerson,whoIsGoing):
    result= ((MealperPerson * 3)* whoIsGoing)
    return result

def main():
    MealperPerson= float(input("what is the maximum cost you are willing to spend on one meal?: "))
    whoIsGoing=int(input("How many people are you bringing on the trip, including yourself?: "))
    result=calculateCost(MealperPerson,whoIsGoing)
    print("Three meals per person, for everyone is a total of:$",format(result,'.2f'),sep='')
main()

#I will take a break from the program to make sure the user is paying attention
#this code was in pogil 10
print("---------------------------------------------")
print("You deserve a fun break from planning your vacation!")
star=input("What is your favorite color?: ")
for row in range (4):
    for column in range(6):
        print(star + " ",end=' ')
    print()

resume= input("Wasn't that cool? Now let's continue...press enter")

#I will see what the method of transportation they would like
print("---------------------------------------------")

#i will determine if they are traveling for business or pleasure
travelType=input("Is this trip for a fun vacation?: ")
if (travelType == "yes" or "y") or (travelType == (not("no" or "n"))):
    print("You should check out tourist spots at the visitors center for your destination!")
else:
    print("You should check out hotels in the business districts!")



    



    

    
