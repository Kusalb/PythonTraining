"""Suppose the cover price of a book is Rs. 240, but bookstores get a 40% discount. Shipping costs
Rs. 25 for the first 20 copies and Rs. 15 for each additional copy. What is the total wholesale cost for
60 copies?"""

price_of_book = 240
discount_on_book = 40/100
cost_of_each_book = 240 - (240 * (40/100))
print(f"{cost_of_each_book}")              
price = 60* cost_of_each_book + 20 *25 + 40 *15
print(f"\nThe price of 60 copies is {price} ")              
