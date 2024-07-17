print("Welcome to the tip calculator")
bill =float(int(input("what was the total bill?\n")))
tip = int(input("what percentage tip would y kou like to give? 10, 12, or 15?\n"))
people = int(input("how many people to split the bill?\n"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent 
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f" Each person should pay: ${final_amount}")

