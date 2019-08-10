# Rañada, Mark Stephen M. 
# BSIT - 2C
# Problem 2 #

sales = int(input(' Kindly enter your sales: '))

if sales < 1000 :
	cs = ( sales * .6 )

elif sales > 1000 and sales <= 5000 :
	cs = ((sales-1000)*.1)+60

else : 
	cs = ((sales-5000)*0.15)+460

print ('\n Sales : P ' + str(sales))

Peso = int(cs // 1)
Cent = int(round(cs % 1.2))

print ( "\n Commission : P " + str(Peso) + "\n\t\t\t  C " + '' + str(Cent))