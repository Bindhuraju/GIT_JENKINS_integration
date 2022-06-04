print("Enter a number between 1 to 100")
n = int(input())
if n%2==0 and (n in range(2,6) or n>20 ):
    print("Not weird")
else:
    print("weird")