def isPrime(num):
#
# put your code here
#
    if num not in [2,3,5,7]:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 :
            return False
        else:
            return True
    else:
        return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
