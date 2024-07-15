"""
Maintain a fixed window size of k and slide this window across the range of values.
* Adhere to the rule: As the window slides, one element exits, reducing the window's sum, 
* while another element enters, increasing the window's sum.
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
