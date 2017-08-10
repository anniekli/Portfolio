import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
# print(countries[1])
# print(countries)

# Start your search algorithm here.
print("You are on the run from the authorities in multiple countries!")
print("Find out which countries have you on their 'WANTED' list, and which ones are safe!")
choice = input("Which country would you like to escape to?")
#
# i = 1
#
# for country in countries:
#     if choice == country:
#         print(choice + " is on the list!")
#     else:
#         if i == length:
#             print(choice + " is not on the list!")
#         else:
#             i += 1
lowerBound = 0
upperBound = 31
midpoint = 16

# def midpoint_eqn():
#     midpoint = ((lowerBound + upperBound)/2)

while lowerBound != upperBound:
    if (choice > countries[midpoint]) and (choice != countries[upperBound]):
        lowerBound = (midpoint + 1)
        # print(midpoint)
        midpoint = ((lowerBound + upperBound)//2)
        # print(str(midpoint) + " greater")
    elif (choice < countries[midpoint]) and (choice != countries[lowerBound]):
        upperBound = (midpoint - 1)
        # print(midpoint)
        midpoint = ((lowerBound + upperBound)//2)
        # print(str(midpoint) + " less")
    else:
        print("You are on " + choice + "'s 'WANTED' list! Choose another country!")
        break;
if (lowerBound == upperBound):
    print("You are not on " + choice + "'s 'WANTED' list! You can go here!")
