print("Welcome to the ticket age checker")
height = int(input("Enter you height = "))

if height >= 120:
    print("You can ride")
    age = int(input("Enter you age = "))
    if age < 12:
        bill = 5
        print("Child Tickets are 5$")
    elif age <= 18:
        bill = 7
        print("Young Tickets are 7$")
    elif age >= 45 and age <= 55:
        print("Free ride for you")
    else:
        bill = 12
        print("Adult Tickets are 12$")
    photo = input("Do you want a photo taken while riding? Y or N. ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("you can't ride")