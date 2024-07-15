"""
Maintain a fixed window size of k and slide this window across the range of values.
*Adhere to the rule: As the window slides, one element exits while another enters.
The one exists reduces the window's sum, while the one enters enters, increases the window's sum.
"""
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
