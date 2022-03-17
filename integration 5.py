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
hours=int(input("Enter the maximum hours you are willing to travel: "))
days=int(input("Enter the amount of days you want to spend: "))
totalCost= airfair + hotel
print("Cost of airfair/gas: ",format(airfair,".2f"),sep='')
print("Cost of hotel: ",format(hotel,".2f"),sep='')
print("Days you will spend in the destination: ",days)
print("Total hours to get to destination: ",hours)
print("Total cost:$",format(totalCost,".2f"),sep='')

#Now I will divide the total cost by day to get a cost per day
#I will get the estimated average cost with floor division
costPerDay= totalCost/days
estimateCostPerDay= totalCost//days
print("Calculated below is the estimated and actual cost per day")
print("The estimated cost per day is: $",format(estimateCostPerDay,".2f"),sep="")
print("The total cost per day will be: $",format(costPerDay,".2f"),sep="")

#I will use subtraction to account for rainy days or delayed flights
print("Now you will take into account if you lose a day on your trip")
missedDays=int(input("Enter the amount of days you think you may lose due to rain or a delayed flight: "))
totalMissedDays= days - missedDays
print("This is how many days you'll actually have:",totalMissedDays)

#I want the user to see how far they are willing to travel in the area in realtion to their hotel
#I will use the exponent opperator and the area of a circle formula (A=3.14159*r**2)
print("Next you will calulate the area you can cover, with your hotel as the center")               
distance=float(input("How many miles are you willing to travel from the distance of your hotel: "))
pi=float(3.14159)
area= pi * distance**2
miles= 'mi.'
print("The total area you can travel, with your hotel as the center point is:",format(area,".2f") + " " + miles)

#now i will figure out how far they want to travel
print("Next you will determine how far you want to travel")
distanceFromHome= float(input("How many miles do you want to travel from home:"))
if (distanceFromHome>=200) and (distanceFromHome<=3000):
    print("You should fly domestic!")
elif (distance<=199) and (distanceFromHome>=1):
    print("You should drive!")
else:
    print("You should fly international!")
print("Are you excited yet" + "?"*3)

    
