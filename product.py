# 記帳program >> 2D list 
product = []
while True:
	name = input('input the item name ')
	if name == 'q':
		break
	price = input('input the price ')
	# <<<to build the small list>>>
	
	#p = []
	#p.append(name)
	#p.append(price)
	
	#<<< small list completed >>>
	product.append([name,price]) # put the small list into big list
print(product)

print(product[0][0]) # the 1st box of Product then the 1st element of the 1st box
print(product[1][1])

