def dis(price, discount):
    finalPrice = price * (1 - discount/100)
    return round(finalPrice, 2)