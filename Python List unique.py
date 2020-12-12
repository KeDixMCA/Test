myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#

uniqueList =[]
for i in myList:
    if i not in uniqueList:
        uniqueList.append(i)

myList = uniqueList[:]
print(uniqueList)
    
print("The list with unique elements only:")
print(myList)
