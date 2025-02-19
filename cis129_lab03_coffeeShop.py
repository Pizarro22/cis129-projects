print('My Coffee and Muffin Shop')
coffeePrice = 5.00
muffinPrice = 4.00
taxRate = 0.06
# Figuring out the prices to go with the numbers put in
# and I almost forgot the rate/ $0.78 cents was 6% first
coffeeNum = int(input("Number of coffees bought? "))
muffinsNum = int(input("Number of muffins bought? "))
coffeeTotal = coffeeNum * coffeePrice
muffinTotal = muffinsNum * muffinPrice
# 1 times 5 dollars will be 5 bucks
# 2 times 4 dollars will be 8 bucks
C_and_M = coffeeTotal + muffinTotal
Tax = C_and_M * taxRate
Total = C_and_M + Tax
print('--------------------')
print('My Coffee and Muffin Shop Receipt')
print("Total: $"(Total)) #??? line 18
# How in the world do I do this last part...
