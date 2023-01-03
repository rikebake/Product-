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

# pull the name and price out of product through FOR
for p in product:
	print(p)

with open('product.txt','w') as file:
	for p in product:
		file.write(p[0] + ',' + p[1] + '\n' )

with open('product.csv','w', encoding = 'utf-8') as file:  # utf-8 is the most common "encoding" to avoid error due to Chinese
	#file.write('item,price\n')  # adding header in the table, English is ok
	file.write('項目,價格\n')  # Chinese causing error 

	for p in product:
		file.write(p[0] + ',' + p[1] + '\n' )
