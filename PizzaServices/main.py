print("Welcome to pizza services")
size = input("Enter size S/M/L")
pepperoni = input("Want pepperoni? Y\N")
cheese = input("want extra cheese? Y/N")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1
print(f"Total bill is ${bill}")