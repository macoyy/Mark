# Rañada, Mark Stephen M. 
# BSIT - 2C
# Problem 1 #

order = int(input("Please enter number of doughnuts: "))

prize = 12.75
totalPrize = float(order*prize)

if order >= 120:
	newDiscount = int((order/120)*2)
	if newDiscount < 20:
		discPrize = totalPrize * (newDiscount / 100)
		newTotal = totalPrize - discPrize
		print ( "\n Discount : ", newDiscount , "%")
		print ( " Total Prize : P ", newTotal)
	if newDiscount >= 20: 
		newDiscount = 20
		discPrize = totalPrize * (newDiscount / 100)
		newTotal = totalPrize - discPrize
		print ( "\n Discount : ", newDiscount , "%")
		print ( " Total Prize : P ", newTotal)

else:
	print ( "\n Quantity of Doughnuts purchased: " , order , "pcs")
	print ( " Total Prize : ", totalPrize)
