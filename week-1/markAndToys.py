def maximumToys(prices, k):
    total = 0
    maxToys = 0
    maxPrice = 0
    sortedPrices = []
    for i in range(len(prices)):
        if prices[i] > maxPrice:
            maxPrice = prices[i]
    countArray = [0] * (maxPrice + 1)
    for i in range(len(prices)):
        countArray[prices[i]] += 1
    for i in range(len(countArray)):
        for j in range(countArray[i]):
            sortedPrices.append(i)
    i = 0
    while(i < len(sortedPrices) and total + sortedPrices[i] <= k):
        total += sortedPrices[i]
        maxToys += 1
        i += 1
    print(maxToys)
    return maxToys
maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)