firstside = int(input("Enter the first side"))
secondside = int(input("Enter second side "))
thirdside = int(input("Enter third side "))

if firstside == thirdside and secondside == thirdside:
    print("The triangle is equilateral")

else:
    print("The triangle is not equilateral")