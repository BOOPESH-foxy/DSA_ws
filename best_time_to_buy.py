prices = [7,6,4,3,1]
minPrice = 100
profit = 0
for i in range(len(prices)):
    minPrice = min(prices[i],minPrice)
    profit = max(profit,prices[i]-minPrice)
print(profit)