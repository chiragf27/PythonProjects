import random
names_str = input("Enter names separated by comma")
names = names_str.split(",")
no_per = len(names)
rand_choice = random.randint(0, no_per-1)
bill_payer = names[rand_choice]
print(f"{bill_payer} is going to pay the bill")