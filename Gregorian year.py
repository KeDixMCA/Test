year = int(input("Enter a year: "))

#
# Put your code here.
#
if year < 1582:
    print("Not within the Gregorian")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")
    
