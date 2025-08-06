age = int(input("Enter your Age:"))
if age >= 18:
    print("Eligible to vote")
elif age > 0 and age < 18:
    print("Not Eligible to vote")
else:
    print("Incorrect input")    