print("Welcome to Tip Calculator")
bill = float(input("What is the total bill amount?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15"))
people = int(input("How many people to split the bill?"))
tip = tip/100 * bill
total_bill = tip + bill
share = total_bill/people
final_bill = round(share, 2) 
#or you can use
final_bill = "{:.2f}".format(share)
print(f"Each person should pay ${final_bill}")