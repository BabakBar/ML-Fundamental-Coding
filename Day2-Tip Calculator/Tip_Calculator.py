print("Welcome to tip calculator!")
bill = float(input("What was the total bills? $"))
percent = int(input("How much tip would you give? 10, 12, or 15 percent?"))
people = int(input("How many people to split the bill?"))
result = (bill *(1+percent/100))/people
print("Each person should pay: result$")
