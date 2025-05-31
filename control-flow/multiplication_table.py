#Get number from user
number = int(input("Enter a number to see its multiplication table: "))


#Iterating Multiplacation table
for Y in range(1, 11):
    print(f"{number} * {Y} = {number * Y}")
