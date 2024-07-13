def best_total_price(prices, k):
    if len(prices) < k:
        return 0
    
    total = sum(prices[:k])
    maxtotal = total
    
    for i in range(len(prices)-k):
        total -= prices[i]
        total += prices[i+k]
        maxtotal = max(maxtotal, total)
    
    return maxtotal
