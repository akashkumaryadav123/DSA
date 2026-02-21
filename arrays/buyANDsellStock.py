prices =[]
profit=0
buy=prices[0]
for num in range(1,len(prices)):
    sell=prices[num]
    buy=min(buy,prices[num])
    print(sell,buy)
    if sell-buy>profit:
        profit=sell-buy
print(profit)

